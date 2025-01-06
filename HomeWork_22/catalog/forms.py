from django import forms
from .models import Product
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'category']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        forbidden_words = {'казино', 'биржа', 'криптавалюта', 'крипта', 'дешево', 'бесплатно', 'обман',
                           'полиция', 'радар'}
        for word in forbidden_words:
            if word in name.lower():
                raise ValidationError(f'Поле не должно содержать слово "{word}"')
            return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        forbidden_words = {'казино', 'биржа', 'криптавалюта', 'крипта', 'дешево', 'бесплатно', 'обман',
                           'полиция', 'радар'}

        for word in forbidden_words:
            if word in description.lower():
                raise ValidationError(f'Поле не должно содержать слово "{word}"')
            return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError(f'Поле price не должно быть отрицателньым')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите название'  # Текст подсказки внутри поля
        })

        self.fields['description'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите описание'  # Текст подсказки внутри поля
        })

        self.fields['category'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите категорию товара'  # Текст подсказки внутри поля
        })

        self.fields['price'].widget.attrs.update({
            'class': 'form-control',  # Добавление CSS-класса для стилизации поля
            'placeholder': 'Введите цену товара'  # Текст подсказки внутри поля
        })

