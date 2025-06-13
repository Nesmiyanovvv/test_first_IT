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
]
