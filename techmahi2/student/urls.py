"""techmahi2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from . import views

urlpatterns = [
    # path('demo/', views.OrderWizard.as_view(views.FORMS), name='demo'),
    
    path('student_new/', views.Employe, name='student_new'),
    path('active/', views.Active, name='active'),
    path('demo/', views.demo, name='demo'),
    path('edit/student/<int:p_id>/', views.Employe_edit, name='edit_student'),
    path('delete/student/<int:p_id>/', views.delete_employ, name='delete_student'),
    # path('employee/', views.Employment_history, name='employee'),
    # path('background/', views.Background, name='background'),
    # path('declartion/', views.Declaration, name='declartion'),
    # path('acceptance/', views.Acceptance, name='acceptance'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('student/login/', views.login, name='student_login'),
    path('student/register/', views.register, name='student_register'),
    

    

]