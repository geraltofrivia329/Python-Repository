from django.urls import path
from projects import views

urlpatterns = [
    path('', views.project_list),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
    
