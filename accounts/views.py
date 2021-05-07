from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User
from .serializers import AccountSerializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import CredentialSerializer
from .serializers import CourseSerializer
from .models import Courses
from django.core.exceptions import ObjectDoesNotExist
from .models import Activity
from .serializers import ActivitySerializer
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from .serializers import ActivitiesUpdateSerializer
from django.shortcuts import get_object_or_404
from .permissions import CreateActivityPermission,CoursePermissions,FilterStudentActivity



class AccountView(APIView):
    def post(self, request):
        serializer = AccountSerializers(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data = serializer.data

        user_exist = User.objects.filter(username=data["username"]).exists()

        if user_exist:
            return Response(status=status.HTTP_409_CONFLICT)

        user = User.objects.create_user(**data, password=request.data["password"])

        serializer = AccountSerializers(user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    def post(self, request):
        serializer = CredentialSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=request.data["username"], password=request.data["password"])

        if user:
            token = Token.objects.get_or_create(user=user)[0]
            return Response({"token": token.key})

        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


class CourseView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly,CoursePermissions]

    def post(self, request):
        serializer = CourseSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.data
        course = Courses.objects.get_or_create(**data)        

        serializer = CourseSerializer(course[0])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def put(self,request):
        data = request.data
        try:
            course = Courses.objects.get(id=data["course_id"])
            users = course.user_set.all()
            for user in users:
                course.user_set.remove(user)
            
            for user in data["user_ids"]:
                add_user = User.objects.get(id=user)
                course.user_set.add(add_user)

            serializer = CourseSerializer(course)

            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({'mensagem':'courses invalid or user_ids'},status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        course = Courses.objects.all()
        serializers = CourseSerializer(course, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

class ActivityView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,CreateActivityPermission]

    def get(self, request):
        user = request.user
        if user.is_staff == False:
            id = request.user.id
            course = Activity.objects.filter(user_id=id)
            serializers = ActivitySerializer(course, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        else:
            course = Activity.objects.all()
            serializers = ActivitySerializer(course, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)

    def post(self,request):
        user = request.user
        if user.is_staff == False and user.is_superuser == False: 
            serializer = ActivitySerializer(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            data = serializer.data

            data['grade'] = None
            id_user = request.user.id

            activity = Activity.objects.get_or_create(**data,user_id=id_user)

            serializer = ActivitySerializer(activity[0])
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request):

        serializers = ActivitiesUpdateSerializer(request.data)
        data = serializers.data
        activity_id = data['id']
        new_grade = data['grade']

        change_grade = Activity.objects.get(id=activity_id)

        change_grade.grade = new_grade
        change_grade.save()
        serializers = ActivitySerializer(change_grade)
        return Response(serializers.data,status=status.HTTP_201_CREATED)


class SelectedUserActivitiesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, FilterStudentActivity]

    def get(self, request, user_id):
        try:
            user = get_object_or_404(User, id=user_id)
            course = Activity.objects.filter(user_id=user_id)
            serializers = ActivitySerializer(course, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception:
            return Response({"detail": "Invalid user_id." }, status=status.HTTP_404_NOT_FOUND)
