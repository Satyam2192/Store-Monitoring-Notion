from django.urls import include, path
from rest_framework import routers
from store_data_app import views
from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'store_status', views.StoreStatusViewSet)
router.register(r'business_hours', views.BusinessHoursViewSet)
router.register(r'timezones', views.TimezonesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('trigger_report/', views.trigger_report, name='trigger_report'),
    path('get-report/', views.get_reports, name='get-report'),
    path('get-report/<str:report_id>/', views.get_report, name='get-report-detail'),
]