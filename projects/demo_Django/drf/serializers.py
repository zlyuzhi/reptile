from datetime import date

from rest_framework import serializers

from index.models import *

#要求：发布日期必须是今年的

def pub_date(value):
    if value<date(2018,1,1):
        raise serializers.ValidationError('必须是今年出版的书籍')
    return value



class BookInfoSerializer(serializers.Serializer):
    #这只是定义序列化器，同时也是反序列的一层验证
    id = serializers.IntegerField(read_only=True)
    btitle=serializers.CharField(max_length=20)
    bpub_date=serializers.DateField(validators=[pub_date])
    bread=serializers.IntegerField(default=0)
    bcomment=serializers.IntegerField(default=0)

    def validate__btitle(self,value):
        if 'django' not in value.lower():
            raise serializers.ValidationError('图书不是关于Django的')
        return value

    def validate(self, attrs):
        #可以验证多个属性
        #要求：阅读量必须大评论量
        bread=attrs.get('bread')
        bcomment=attrs.get('bcomment')
        if all([bread,bcomment]):
            if bread<bcomment:
                raise serializers.ValidationError("阅读量必须大评论量")
        return attrs
    def create(self, validated_data):
        #validated_data===》验证通过后，数据保存在这此字典中
        #有返回值，所以要接收下
        book=BookInfo.objects.create(**validated_data)
        return book
    def update(self, instance, validated_data):
        instance.btitle = validated_data.get('btitle')
        instance.bpub_date = validated_data.get('bpub_date')
        if validated_data.get('bread'):
            instance.bread = validated_data.get('bread')
        if validated_data.get('bcomment'):
            instance.bcomment = validated_data.get('bcomment')

        instance.save()
        return instance


class HeroInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=HerroInfo
        fields='__all__'
        extra_kwargs={
            'hcomment':{
                'required':False,
                'max_length':200
            },
            'hbook':{
                'required':False
            }
        }
        def vaildate_hname(self,value):
            if not value.startswith('马'):
                raise serializers.ValidationError('必须姓马')
            return value
