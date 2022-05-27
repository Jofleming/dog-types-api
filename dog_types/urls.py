from django.urls import path
from .views import Dog_type_list, DogDetail

urlpatterns = [
    path('', Dog_type_list.as_view(), name='dog_type_list'),
    path('<int:pk>/', DogDetail.as_view(), name='dog_detail'),
]