from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from rest_framework import status, generics
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth  import authenticate, login, logout
from rest_framework.response import Response
from .serializers import UserSerializer
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# class SignupView(generics.CreateAPIView):
#     serializer_class = UserSerializer


#@method_decorator(csrf_protect, name='dispatch')
class InternationalSignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = InternationalTraderSignupSerializer

#@method_decorator(csrf_protect, name='dispatch')
class LocalSignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = LocalTraderSignupSerializer

#@method_decorator(csrf_protect, name='dispatch')
class ProducerSignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ProducerSignupSerializer

#@method_decorator(csrf_protect, name='dispatch')
class CarrierSignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = CarrierSignupSerializer

class AdministratorSignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = AdministratorSignupSerializer
class ConsultantSignupView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = ConsultantSignupSerializer



@method_decorator(csrf_protect, name='dispatch')
class LoginView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        email = data['email']
        password = data['password']

        try:
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return Response({ 'success': 'User authenticated' })
            else:
                return Response({ 'error': 'Error Authenticating' })
        except:
            return Response({ 'error': 'Something went wrong when logging in' })






# @method_decorator(ensure_csrf_cookie, name='dispatch')
# class GetCSRFToken(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def get(self, request, format=None):
#         return Response({ 'success': 'CSRF cookie set' })
def csrf(request):
    return JsonResponse({'csrfToken': get_token(request)})

def ping(request):
    return JsonResponse({'result': 'OK'})

class LogoutView(APIView):
    def post(self, request, format=None):
        try:
            logout(request)
            return Response({ 'success': 'Logout Out' })
        except:
            return Response({ 'error': 'Something went wrong when logging out' })



class CheckAuthenticatedView(APIView):
    def get(self, request, format=None):
        user = self.request.user

        try:
            isAuthenticated = user.is_authenticated

            if isAuthenticated:
                return Response({ 'isAuthenticated': 'success' })
            else:
                return Response({ 'isAuthenticated': 'error' })
        except:
            return Response({ 'error': 'Something went wrong when checking authentication status' })


class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated, ]
    authentication_classes = [SessionAuthentication, ]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

# @method_decorator(ensure_csrf_cookie, name='dispatch')
# class GetCSRFToken(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def get(self, request, format=None):
#         return JsonResponse({ 'success': 'CSRF cookie set' })

class DeleteAccountView(APIView):
    def delete(self, request, format=None):
        user = self.request.user

        try:
            User.objects.filter(id=user.id).delete()

            return Response({ 'success': 'User deleted successfully' })
        except:
            return Response({ 'error': 'Something went wrong when trying to delete user' })


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (permissions.AllowAny,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)



class UpdateEmailView(generics.UpdateAPIView):

    queryset = UserAccount.objects.all()
    permission_classes = (IsAuthenticated,)
   
    def get_serializer_class(self):
        user = self.request.user
        if user.type == "PRODUCER":
            return UpdateEmailProducerSerializer
        if user.type == "INTERNATIONAL TRADER":
            return UpdateEmailExtranjeroSerializer
        if user.type == "LOCAL TRADER":
            return UpdateEmailLocalSerializer
        if user.type == "CARRIER":
            return UpdateEmailCarrierSerializer
        else:
            pass

    def get_object(self):
        user = self.request.user
        data = self.request.data
        if user.type == "PRODUCER":
            producer = Producer.objects.get(id= user.id)
            return producer
        if user.type == "INTERNATIONAL TRADER":
            international = InternationalTrader.objects.get(id= user.id)
            return international
        if user.type == "LOCAL TRADER":
            lTrader = LocalTrader.objects.get(id= user.id)
            return lTrader
        if user.type =="CARRIER":
            carrier = Carrier.objects.get(id= user.id)
            return carrier
        else:
            pass