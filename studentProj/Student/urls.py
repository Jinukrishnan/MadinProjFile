
from django.urls import path

from Student import views

urlpatterns = [
    path('', views.Content, name='Content'),
    path('register/', views.register, name='register'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<int:pk>/',views.dpt,name='Department'),
    path('add/', views.student_create_view, name='student_add'),

    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'),  # AJAX

]
