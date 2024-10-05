from django.urls import path
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

from kittens_app import views
from kittens_app.views import RegisterUserAPIView

router = routers.DefaultRouter()
router.register(r'kitten', views.KittenViewSet)
# router.register(r'kitten-detail', views.KittenDetailViewSet, basename='KittenViewSet')
router.register(r'kitten-by-breed', views.KittenByBreedViewSet, basename='KittenViewSet')
router.register(r'breed', views.BreedViewSet)
router.register(r'grade', views.GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterUserAPIView.as_view(), name="register"),
    path('login/', ObtainAuthToken.as_view(), name='token_obtain_pair'),
    # path('refresh/', TokenRefreshView.as_view(), name='token_refresh')
]