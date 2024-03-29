from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegistrationSerializer, LoginSerializer, UserProfileSerializer
from rest_framework import generics
from .models import UserProfile
User = get_user_model()


class RegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegistrationSerializer


class LoginAPIView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class GETALLUser(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile_detail(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'GET':
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
