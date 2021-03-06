from django import forms

from categories.models import Category
from tags.models import Tag
from .models import Product


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.label_suffix = ''

        # instance_data = kwargs.get('instance')
        
        # if instance_data:
        #     self.fields['sub_category'].initial = instance_data.sub_category.id
            # self.fields['tags'].initial = [tag.pk for tag in instance_data.tags.all()]
        # self.fields.keyOrder = ['name', 'category', 'description', 'price']

    category = forms.ChoiceField(
        choices=[('', '--Select Category--')] +
        list(Category.objects.filter(parent=None).values_list('id', 'name')),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'id_category'
            }
        )
    )

    sub_category = forms.ChoiceField(
        choices=[('', '--Select Sub Category--')] +
        list(Category.objects.values_list('id', 'name')),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'id_sub_category'
            }
        ),
        required=False
    )
    
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter product name',
                'class': 'form-control'
            }
        )
    )
    slug = forms.SlugField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the slug'
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
    price = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': 'number',
                'value': 0.0,
                'step': 0.5
            }
        )
    )
    image = forms.ImageField(required=False)
    tags = forms.MultipleChoiceField(
        choices=Tag.objects.values_list('id', 'name'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-control',
                'id': 'id_tags'
            }
        ),
        required=False
    )
    featured = forms.BooleanField(
        required=False, 
        widget=forms.CheckboxInput()
    )

    class Meta:
        model = Product 
        fields = ['name', 'slug', 'description',
                  'price', 'image', 'tags', 'featured', 'category']


    def clean(self, *args, **kwargs):
        sub_category = self.cleaned_data.get('sub_category')
        tags = self.cleaned_data.get('tags')
        
        if sub_category:
            self.cleaned_data['category'] = Category.objects.get(pk=sub_category)
        else:
            raise forms.ValidationError('Sub Category can not be empty.')

        return super(ProductForm, self).clean(*args, **kwargs)
