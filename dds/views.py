from rest_framework import viewsets
from .models import Type, Category, Subcategory, Status, CashflowRecord
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import CashflowRecordForm
from .serializers import (
    TypeSerializer, CategorySerializer, SubcategorySerializer,
    StatusSerializer, CashflowRecordSerializer
)

def record_list(request):
    records = CashflowRecord.objects.select_related('status', 'type', 'category', 'subcategory')
    return render(request, 'dds/record_list.html', {'records': records})

def record_create(request):
    form = CashflowRecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('record_list')
    return render(request, 'dds/record_form.html', {'form': form})

def load_categories(request):
    type_id = request.GET.get('type_id')
    categories = Category.objects.filter(type_id=type_id).values('id', 'name')
    return JsonResponse(list(categories), safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category_id')
    subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
    return JsonResponse(list(subcategories), safe=False)

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(viewsets.ModelViewSet):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

class CashflowRecordViewSet(viewsets.ModelViewSet):
    queryset = CashflowRecord.objects.all()
    serializer_class = CashflowRecordSerializer
