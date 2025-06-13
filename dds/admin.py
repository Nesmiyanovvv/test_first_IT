from django.contrib import admin
from .models import Type, Category, Subcategory, Status, CashflowRecord

admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Status)
admin.site.register(CashflowRecord)