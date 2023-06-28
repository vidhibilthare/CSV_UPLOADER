from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('admin_all/',views.admin, name='admin_page'),
    path('downloafde/<int:file_id>/',views.downloade_file, name='downloade_file'),
    path('view/<int:file_id/',views.view_file, name='view_file')
    
]

