from django.urls import path
from . import views


urlpatterns = [
    path('', views.TableListView.as_view(), name='home'),
    path('table/<int:pk>/', views.TableDetailView.as_view(), name='table-detail'),
    path('table/<int:pk>/update/', views.TableUpdateView.as_view(), name='table-update'),
    path('table/<int:pk>/delete/', views.TableDeleteView.as_view(), name='table-delete'),
    path('table/new/', views.TableCreateView.as_view(), name='table-create'),
]
