from django.urls import path
from . import views
urlpatterns = [
    path("profile/",views.UserProfileView.as_view(),name="profile"),    # the url to get the user profile
    path("signup/",views.UserSignUpApiView.as_view(),name="sign_up"),  # the url to sign up users
    path("login/",views.UserLoginView.as_view(),name="login"), # the url to login users
]