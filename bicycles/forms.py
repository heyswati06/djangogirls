from django import forms

from .models import SalePost

class PostForm(forms.ModelForm):

    class Meta:
        model = SalePost
        fields = ('title', 'make','model', 'type', 'size', 'age', 'original_price', 'quoted_price', 'city', 'state', 'shipping', 'bill', 'negotiable', 'other_details')