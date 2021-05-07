from rest_framework import serializers


class AccountSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    is_superuser = serializers.BooleanField()
    is_staff = serializers.BooleanField()


class CredentialSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    user_set = AccountSerializers(read_only=True, many=True)


class ActivitySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    repo = serializers.CharField()
    grade = serializers.IntegerField(required=False,allow_null=True)



class ActivitiesUpdateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    grade = serializers.CharField()