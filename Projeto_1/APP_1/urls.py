from APP_1 import views
from django.urls import path
from APP_1.views import register, user_login, user_logout, create_post, edit_post, delete_post

urlpatterns = [
    path('register/',register, name='register'),
    path('login/',user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('create_post/',create_post, name='create_post'),
    path('edit_post/<int:post_id>/',edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/',delete_post,  name='delete_post'),  
]