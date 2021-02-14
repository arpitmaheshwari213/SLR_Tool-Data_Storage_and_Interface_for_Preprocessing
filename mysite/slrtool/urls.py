from django.urls import path

from . import views

urlpatterns = [
    path('', views.file_upload, name='index'),
    path('filter/', views.filter, name='filter'),
    path('filter/quality_assessment/', views.quality_assessment, name='quality_assessment'),
    path('filter/add_quality_assessment', views.add_quality_assessment, name='add_quality_assessment')
]
