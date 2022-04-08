from django.urls import path
from . import views

urlpatterns = [
    path('', views.WidgetList.as_view(), name='list'),
    path('<int:pk>/delete/', views.WidgetDelete.as_view(), name='delete'),
    path('add_widget/', views.add_widget, name ='add_widget')
]
