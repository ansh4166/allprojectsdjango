"""
URL configuration for ansh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from .views import homepage, student_list, update_student, delete_student,signup ,user_login

urlpatterns = [
    path('', homepage, name='homepage'),
    path('students/', student_list, name='student_list'),
    path('students/<int:student_id>/update/', update_student, name='update_student'),
    path('students/<int:student_id>/delete/', delete_student, name='delete_student'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
]

