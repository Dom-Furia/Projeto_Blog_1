from django.contrib import admin
from django.urls import path, include
from APP_1 import views
from APP_1 import urls
from django.conf import settings
from django.conf.urls.static import static
from APP_1.views import register, user_login, user_logout, create_post, edit_post, delete_post 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('',include('APP_1.urls')),
    path('<slug:slug>', views.post_detail, name='post_detail'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)