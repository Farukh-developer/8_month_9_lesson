from django.urls import path, include
from .views import BlogAPIView, LikeAPIView, CommentAPIView
from rest_framework import routers



router=routers.SimpleRouter()
router.register("blog", BlogAPIView)
router.register("likes", LikeAPIView)
router.register("comment", CommentAPIView)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
    #### Djoser
    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
]
