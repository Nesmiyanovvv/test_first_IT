from django import forms
from .models import CashflowRecord, Status, Type, Category, Subcategory
from django.forms.widgets import DateInput
from datetime import date

class CustomDateInput(DateInput):
    input_type = 'date'  # Это даст выбор даты в формате yyyy-mm-dd (браузер сам форматирует)

class CashflowRecordForm(forms.ModelForm):
    class Meta:
        model = CashflowRecord
        fields = '__all__'
        widgets = {
            'custom_date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={
                'step': 1,       # шаг — 1
                'min': 0         # можно ограничить от нуля, если нужно
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # ← вот здесь вставляем сегодняшнюю дату
        if not self.instance.pk and not self.data:
            self.fields['custom_date'].initial = date.today()

        # Актуальные querysets для выпадающих списков
        self.fields['category'].queryset = Category.objects.none()
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = Category.objects.filter(type_id=type_id)
            except (ValueError, TypeError):
                pass

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass