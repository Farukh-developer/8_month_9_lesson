from django.urls import path, include
# from .views import
from rest_framework import routers



# router=routers.SimpleRouter()
# router.register("food_detail", FoodDetailAPIView)
# router.register("food_type", FoodTypelAPIView)
# router.register("made_food", Made_of_FoodAPIView)
# router.register("comment_food", CommentDetailAPIView)

urlpatterns = [
    # path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
    #### Djoser
    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
]
