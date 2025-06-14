from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import (
    TypeViewSet, CategoryViewSet, SubcategoryViewSet,
    StatusViewSet, CashflowRecordViewSet
)

router = DefaultRouter()
router.register(r'types', TypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'records', CashflowRecordViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.record_list, name='record_list'),
    path('create/', views.record_create, name='record_create'),
    path('ajax/load-categories/', views.load_categories, name='ajax_load_categories'),
    path('ajax/load-subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    path('edit/<int:pk>/', views.record_edit, name='record_edit'),
    path('delete/<int:pk>/', views.record_delete, name='record_delete'),
    path('directories/', views.directory_home, name='directory_home'),
    path('directory/<str:model_name>/create/', views.directory_create, name='directory_create'),
    path('directory/<str:model_name>/<int:pk>/edit/', views.directory_edit, name='directory_edit'),
    path('directory/<str:model_name>/<int:pk>/delete/', views.directory_delete, name='directory_delete'),

]
