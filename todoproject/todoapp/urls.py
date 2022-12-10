from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.inicio,name='inicio'),
    path('todoApi/',views.todoApi),
    path('contactApi/',views.contactApi),
     path('projectApi/',views.projectApi),
    path('todoAppCreate/', views.todoAppCreate,name='todoAppCreate'),
    path('CargaContact/', views.ContactCreate,name='ContactCreate'),
    path('ProjectCreate/',views.ProjectCreate,name='ProjectCreate')
]
