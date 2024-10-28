from django import forms
from .models import Categories

class CategoryFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        selected_categories = kwargs.pop('selected_categories', None)
        super(CategoryFilterForm, self).__init__(*args, **kwargs)

        categories = Categories.objects.all()

        for category in categories:
            # Check if the category is in selected_categories to set the checkbox state
            initial_value = selected_categories and category.id in selected_categories
            self.fields[f'category_{category.id}'] = forms.BooleanField(
                required=False,
                label=category.name,
                initial=initial_value)
