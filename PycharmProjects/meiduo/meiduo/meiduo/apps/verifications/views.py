import random

from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from celery_tasks.sms.tasks import send_sms_code
from verifications import constants


class SMSCodeView(APIView):
    '''
    检查是否在60s内有发送记录
    生成短信验证码
    保存短信验证码与发送记录
    发送短信
    '''
    def get(self,request,mobile):
        #与redis建立链接(指定那个数据库)
        redis_cli =get_redis_connection('sms_code')
        ## 1.判断60秒内是不向指定手机号发过短信，如果发过，则抛异常,只需要判断标记存在么
        if redis_cli.get('sms_flag'+mobile):
            raise serializers.ValidationError('向此手机号发短信太频繁了')
        # 2.如果未发短信，则
        # 2.1随机生成6位数
        code =random.randint(100000,999999)
        print(code)

        # 2.2保存到redis：验证码，发送的标记
        # redis_cli.setex('sms_code_'+mobile,300,code)
        # redis_cli.setex('sms_flag_'+mobile,60,1)
        # 优化：pipeline管道
        radis_pipeline=redis_cli.pipeline()
        radis_pipeline.setex('sms_code'+mobile,constants.SMS_CODE_EXPIRES,code)
        radis_pipeline.setex('sms_flag'+mobile,constants.SMS_FLAG_EXPIRES,1)
        radis_pipeline.execute()

        # 2.3发短信：云通讯
        # CCP.sendTemplateSMS(mobile,code,constants.SMS_CODE_EXPIRES/60,1)
        # print(code)
        # 调用celery任务，执行耗时代码

        send_sms_code.delay(mobile,code,constants.SMS_CODE_EXPIRES/60,1)

        return Response({'message':'OK'})