"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from .views import (CourseView, CourseListView, CourseCreateView, CourseUpdateView,CourseDeleteView
                    # MyListView
    # my_fbv
)
app_name = 'courses'        #haysy papkada duranyny aytyar..
urlpatterns = [
    path('', CourseListView.as_view(), name='courses-list'),    #ozal CourseView , CourseListView, durdy     path('', CourseListView.as_view, name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='course-delete'),
]
