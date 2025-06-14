from rest_framework import viewsets
from .models import Type, Category, Subcategory, Status, CashflowRecord
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import CashflowRecordForm
from django.db.models import Q
from django.apps import apps
from django.forms import modelform_factory
from django.shortcuts import get_object_or_404
from .serializers import (
    TypeSerializer, CategorySerializer, SubcategorySerializer,
    StatusSerializer, CashflowRecordSerializer
)

def record_list(request):
    records = CashflowRecord.objects.select_related('status', 'type', 'category', 'subcategory')

    # Получаем значения из GET-параметров
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    status = request.GET.get('status')
    type_id = request.GET.get('type')
    category_id = request.GET.get('category')
    subcategory_id = request.GET.get('subcategory')

    if start_date:
        records = records.filter(custom_date__gte=start_date)
    if end_date:
        records = records.filter(custom_date__lte=end_date)
    if status:
        records = records.filter(status_id=status)
    if type_id:
        records = records.filter(type_id=type_id)
    if category_id:
        records = records.filter(category_id=category_id)
    if subcategory_id:
        records = records.filter(subcategory_id=subcategory_id)

    # Вот здесь отфильтруем логически связанные значения
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    if type_id:
        categories = categories.filter(type_id=type_id)
    if category_id:
        subcategories = subcategories.filter(category_id=category_id)

    context = {
        'records': records,
        'statuses': Status.objects.all(),
        'types': Type.objects.all(),
        'categories': categories,
        'subcategories': subcategories,
        'filters': {
            'start_date': start_date,
            'end_date': end_date,
            'status': status,
            'type': type_id,
            'category': category_id,
            'subcategory': subcategory_id,
        }
    }
    return render(request, 'dds/record_list.html', context)

def record_create(request):
    form = CashflowRecordForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('record_list')
    return render(request, 'dds/record_form.html', {'form': form})

def load_categories(request):
    type_id = request.GET.get('type_id')
    if type_id:
        try:
            type_id = int(type_id)
            categories = Category.objects.filter(type_id=type_id).values('id', 'name')
        except ValueError:
            categories = []
    else:
        categories = []  # пустой список, если type не выбран
    return JsonResponse(list(categories), safe=False)

def load_subcategories(request):
    category_id = request.GET.get('category_id')
    if category_id:
        try:
            category_id = int(category_id)
            subcategories = Subcategory.objects.filter(category_id=category_id).values('id', 'name')
        except ValueError:
            subcategories = []
    else:
        subcategories = []
    return JsonResponse(list(subcategories), safe=False)

def record_edit(request, pk):
    record = get_object_or_404(CashflowRecord, pk=pk)
    form = CashflowRecordForm(request.POST or None, instance=record)
    if form.is_valid():
        form.save()
        return redirect('record_list')
    return render(request, 'dds/record_form.html', {'form': form})

def record_delete(request, pk):
    record = get_object_or_404(CashflowRecord, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('record_list')
    return render(request, 'dds/record_confirm_delete.html', {'record': record})

DIRECTORY_MODELS = {
    'type': Type,
    'status': Status,
    'category': Category,
    'subcategory': Subcategory,
}

def directory_home(request):
    context = {
        'types': Type.objects.all(),
        'statuses': Status.objects.all(),
        'categories': Category.objects.select_related('type'),
        'subcategories': Subcategory.objects.select_related('category'),
    }
    return render(request, 'dds/directory_home.html', context)

def directory_create(request, model_name):
    Model = DIRECTORY_MODELS.get(model_name)
    FormClass = modelform_factory(Model, fields='__all__')
    form = FormClass(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('directory_home')
    return render(request, 'dds/directory_form.html', {'form': form, 'action': 'Создание'})

def directory_edit(request, model_name, pk):
    Model = DIRECTORY_MODELS.get(model_name)
    instance = get_object_or_404(Model, pk=pk)
    FormClass = modelform_factory(Model, fields='__all__')
    form = FormClass(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('directory_home')
    return render(request, 'dds/directory_form.html', {'form': form, 'action': 'Редактирование'})

def directory_delete(request, model_name, pk):
    Model = DIRECTORY_MODELS.get(model_name)
    instance = get_object_or_404(Model, pk=pk)
    if request.method == 'POST':
        instance.delete()
        return redirect('directory_home')
    return render(request, 'dds/record_confirm_delete.html', {'record': instance})

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
