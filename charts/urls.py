from django.urls import path, reverse
from django.contrib.auth.decorators import login_required
from .views import ChartListView, ChartDetailView, ChartCreateView, ChartUpdateView, ChartDeleteView
from . import views

urlpatterns = [
    # path('', views.view_chart, name='view-charts'),
    path('', ChartListView.as_view(), name='view-charts'),
    path('user/<str:username>', login_required(ChartListView.as_view()), name='charts'), # show posts of one user only
    path('charts', login_required(ChartListView.as_view()), name='charts'),
    path('chart/<int:pk>/', ChartDetailView.as_view(), name='chart-detail'),
    path('chart/<int:pk>/update/', ChartUpdateView.as_view(), name='chart-update'),
    path('chart/<int:pk>/delete/', ChartDeleteView.as_view(), name='chart-delete'),
    path('chart/new/', ChartCreateView.as_view(), name='chart-create'),
    # path('chart/<int:pk>/add_temp/', AddTemperature.as_view(), name='add-temp'),
    path('add_chart', views.add_chart, name='add-chart'),
    ]