from rest_framework import serializers
from .models import Type, Category, Subcategory, Status, CashflowRecord

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class CashflowRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashflowRecord
        fields = '__all__'

    def validate(self, data):
        category = data.get('category')
        subcategory = data.get('subcategory')
        type_ = data.get('type')

        if category and type_ and category.type != type_:
            raise serializers.ValidationError("Категория не принадлежит типу")

        if subcategory and category and subcategory.category != category:
            raise serializers.ValidationError("Подкатегория не принадлежит категории")

        return data
