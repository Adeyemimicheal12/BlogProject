from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

User = get_user_model() #to allow you to refernce the user model dynamically without hardcoding it.

class EmailModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs): # It overrides the authenticate method provided by the ModelBackend.
        try: # to handle expections
            user = User.objects.get(email=username) #This attempts to retrieve a user from the database based on the provided email address (username). It queries the user model (User) using the get method.
            if user.check_password(password):
                return user # to return authenticated user object if password and email matches
        except User.DoesNotExist: #used if user with the provided email does not exist
            pass
        return None

class TokenAuthentication(BaseTokenAuth):
    keyword = "Bearer"

    # custom authentication Backend

    #In summary, this code provides custom authentication backends for a Django project: EmailModelBackend for authenticating users based on email addresses and TokenAuthentication for token-based authentication.






