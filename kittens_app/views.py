from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .permissions import IsOwnerOrAdmin
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Kitten, Breed, Grade
from .serializers import KittenSerializer, BreedSerializer, UserCreateSerializer, GradeSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserCreateSerializer


class KittenViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer

    def post(self, request):
        serializer = KittenSerializer(data=request.data)
        print(self.request.user)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            print(self.request.user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class KittenDetailViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer


class KittenByBreedViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    serializer_class = KittenSerializer

    def get_queryset(self):
        queryset = Kitten.objects.all()
        breed = self.request.query_params.get('breed')
        if breed is not None:
            queryset = queryset.filter(breed=breed)

        return queryset


class BreedViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class GradeViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
