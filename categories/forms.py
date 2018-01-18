from django import forms
from .models import Category


class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter category name',
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5, 
                'placeholder': 'Enter the description',
                'class': 'form-control'
            }
        )
    )
    parent = forms.ChoiceField(
        choices=[('', '--Select Parent Category--')] + list(Category.objects.values_list('id', 'name')), 
        required=False, 
        label='Parent Category',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Category
        fields = ['name', 'description', 'parent']

    def clean(self, *args, **kwargs):
        parent = self.cleaned_data.get('parent')

        if not parent:
            self.cleaned_data['parent'] = None
        return super(CategoryForm, self).clean(*args, **kwargs)
