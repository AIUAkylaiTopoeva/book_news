from django.urls import path 

from .views import NewList, NewDetail, NewCreate

urlpatterns = [
    path("<int:pk>/", NewDetail.as_view(), name="new_detail"), 
    path("", NewList.as_view(), name="new_list"),
    path('create/', NewCreate.as_view(), name= 'new_create')
]