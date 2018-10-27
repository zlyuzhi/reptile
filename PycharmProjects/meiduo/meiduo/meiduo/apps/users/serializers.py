import re
# import requests
from django_redis import get_redis_connection
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from users.models import User


class UserCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)  # 不接收客户端的数据，只向客户端输出
    token = serializers.CharField(read_only=True)
    username=serializers.CharField(max_length=20,min_length=5,error_messages=({
        'max_length':'长度太长了(5-20)',
        'min_length':'长度太短了(5-20)'
    }))
    password=serializers.CharField(write_only=True)
    password2=serializers.CharField(write_only=True)
    sms_code=serializers.CharField(write_only=True)
    mobile=serializers.CharField()
    allow=serializers.BooleanField(write_only=True)


    def validate_username(self,value):
        count =User.objects.filter(username=value).count()
        if count>0:
            raise serializers.ValidationError('用户名已经存在')
        return value

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError('前后密码不一致')

        #验证短信验证码
        sms_code_request=attrs.get('sms_code')
        mobile=attrs.get('mobile')
        redis_cli=get_redis_connection('sms_code')#从哪个缓存库
        sms_code_redis=redis_cli.get('sms_code'+mobile)
        print(sms_code_redis)
        if sms_code_redis is None:
            raise serializers.ValidationError('短信验证码已经过期')
        redis_cli.delete('sms_code'+mobile)
        if int(sms_code_redis) != int(sms_code_request):
            raise serializers.ValidationError('短信验证码错误')

        return attrs

    def validate_mobile(self,value):
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号码格式错误')
        count=User.objects.filter(mobile=value).count()
        if count>0:
            raise  serializers.ValidationError('手机号码已经存在')
        return value

    def validate_allow(self,value):
        if not value:
            raise serializers.ValidationError('请先阅读协议并同意')
        return value

    def create(self, validated_data):
        user=User()
        user.username=validated_data.get('username')
        user.set_password(validated_data.get('password'))
        user.mobile=validated_data.get('mobile')
        user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)  # header.payload.signature

        # 将token输出到客户端
        user.token = token

        return user