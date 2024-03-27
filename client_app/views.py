from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from .models import Client

# Create your views here.
def create_user_or_return_exception(request):
    data = request.data.copy()
    data['username'] = request.data.get("email")
    new_client = Client(**data)
    try:
        new_client.full_clean()
        new_client = Client.objects.create_user(**data)
        token = Token.objects.create(user= new_client)
        login(request, new_client)
        return [new_client, token]
    except ValidationError as e:
        return e

class Register_admin(APIView):
    def post(self, request):
        creds_or_err = create_user_or_return_exception(request)
        if type(creds_or_err) == list:
            client, token = creds_or_err
            client.is_staff = True
            client.is_superuser = True
            client.save()
            return Response({"client":client.email, "token":token.key}, status=HTTP_201_CREATED)
        return Response(creds_or_err.message_dict, status=HTTP_400_BAD_REQUEST)

class Register(APIView):
    def post(self, request):
        creds_or_err = create_user_or_return_exception(request)
        if type(creds_or_err) == list:
            client, token = creds_or_err
            client.is_staff = False
            client.is_superuser = False
            client.save()
            return Response({"client":client.email, "token":token.key}, status=HTTP_201_CREATED)
        return Response(creds_or_err.message_dict, status=HTTP_400_BAD_REQUEST) 

class Log_in(APIView):
    def post(self, request):
        data = request.data.copy()
        data['username'] = request.data.get("email")
        client = authenticate(username=data.get("username"), password=data.get("password"))
        if client:
            token, created = Token.objects.get_or_create(user = client)
            login(request, client)
            return Response({"client":client.email, "token":token.key})
        return Response("No user matching these credentials", status=HTTP_404_NOT_FOUND)
    
class TokenReq(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
class Info(TokenReq):

    def get(self, request):
        print(request.user)
        return Response(request.user.email)
    
class Log_out(TokenReq):

    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=HTTP_204_NO_CONTENT)