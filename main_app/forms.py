from django import forms
from .models import item, category


class itemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['item_name','is_used', 'price_in_JOD', 'categories', 'item_description', 'item_image']
        error_messages = {
            "item_name": {
                # "max_length": "Keep it short, please."
            }
        }

class categoryForm(forms.ModelForm):
    class Meta:
        model = category
        fields = ['category_name']

