from rest_framework import serializers


class HerroInfoSerialize(serializers.Serializer):
    hname=serializers.CharField(max_length=20)


class BookInfoSerializer(serializers.Serializer):
    id =serializers.IntegerField(read_only=True)
    bread=serializers.IntegerField(min_value=0)
    btitle=serializers.CharField(max_length=30)

    #三种关系属性
    herroinfo_set =serializers.PrimaryKeyRelatedField(read_only=True,many=True)