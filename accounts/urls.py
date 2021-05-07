from django.urls import path
from .views import AccountView,LoginView,CourseView,ActivityView,SelectedUserActivitiesView

urlpatterns =  [
    path("accounts/",AccountView.as_view()),
    path("login/",LoginView.as_view()),
    path("courses/",CourseView.as_view()),
    path("courses/registrations/",CourseView.as_view()),
    path("activities/",ActivityView.as_view()),
    path("activities/<int:user_id>/",SelectedUserActivitiesView.as_view())
]