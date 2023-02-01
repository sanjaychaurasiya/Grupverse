from django.urls import path
from .views import UserList, UserDetails, SendTemplateMailView, render_image


urlpatterns = [
    path('userlist/', UserList.as_view(), name='user-list'),
    path('userlist/<int:pk>/', UserDetails.as_view(), name='user-details'),
    path('send/render_image/', render_image, name='render_image'),
    path('send/', SendTemplateMailView.as_view(), name='send_template'),
]