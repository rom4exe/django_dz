# from django.contrib import admin
from django.urls import path
from .views import SensorView, MeasurementView, SensorDetailView


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
