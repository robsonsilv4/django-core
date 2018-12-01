from django.urls import path

from .views import (
    post_model_create_view,
    post_model_list_view,
    post_model_detail_view,
)

app_name = 'blog'

urlpatterns = [
    path('', post_model_list_view, name='list'),
    path('create/', post_model_create_view, name='create'),
    path('<int:id>/', post_model_detail_view, name='detail'),
]
