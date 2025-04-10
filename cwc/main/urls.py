from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', views.home_page, name='admin'),

    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('lodge_complaint/', views.lodge_complaint, name='lodge_complaint'),
    path('view_complaints/', views.view_complaints, name='view_complaints'),

    # Police Station Module
    path('police_dashboard/', views.police_station_dashboard, name='police_station_dashboard'),
    path('update_complaint/<int:complaint_id>/', views.update_complaint_status, name='update_complaint_status'),

    # Administrator Module
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_station/', views.add_police_station, name='add_police_station'),
    path('delete_station/<int:station_id>/', views.delete_police_station, name='delete_police_station'),

    # Criminal Records Module
    path('add_criminal/', views.add_criminal, name='add_criminal'),
    path('criminal/<int:criminal_id>/', views.criminal_detail, name='criminal_detail'),
    path('edit_criminal/<int:criminal_id>/', views.edit_criminal, name='edit_criminal'),
    path('delete_criminal/<int:criminal_id>/', views.delete_criminal, name='delete_criminal'),

    # Emergency News Module
    path('add_emergency/', views.add_emergency_news, name='add_emergency'),
    path('view_emergency_news/', views.view_emergency_news, name='view_emergency_news'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
