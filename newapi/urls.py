from django.urls import path 

from .views import NewList, NewDetail

urlpatterns = [
    path("<int:pk>/", NewDetail.as_view(), name="new_detail"), 
    path("", NewList.as_view(), name="new_list"),
]