from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from blog import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('accounts/login', views.LoginView.as_view(), name='login'),
    path('accounts/signup/', core_views.signup, name='signup'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]
