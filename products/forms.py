from django import forms

from .models import Product


class ProductForm(
    forms.ModelForm):  # ashakdaky charfildyng ichinde yazylyan zatlar dine owadanlyk frontend edyar...yorite modele girmek gerek dal
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "hello place"}))  # required talap edilyar #label=("")- islendik haty yazyp bolyar # django widgets
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "new-class-name two", "placeholder": "hello place", "rows": 20, "cols": 50,
               "id": "new id"}))  # talap edilenok
    salgysy = forms.CharField(label='salgymyz', widget=forms.Textarea(attrs={"placeholder": "shu salgy"}))
    email = forms.EmailField()

    class Meta:  # fieldakylar browserda chykaryar...
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'salgysy'
        ]
        # -----Validation---------
    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "CFE" in title:
    #         raise forms.ValidationError("this is not a valid title")
    #     if not "news" in title:
    #         raise forms.ValidationError("this is not a valid title")
    #     return title
    #
    #                                 #------Validation dushunmedim----------
    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):               #endswith tazelenen gornushi update of django
    #         raise forms.ValidationError("This is not a valid email")
    #     return email


class ProductFormSecond(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'salgysy',
            'ady',
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={
        "placeholder": "hello place"}))  # required talap edilyar #label=("")- islendik haty yazyp bolyar # django widgets
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "new-class-name two", "placeholder": "hello place", "rows": 20, "cols": 50,
               "id": "new id"}))  # talap edilenok
    # description = forms.CharField(required=False, widget=forms.Textarea(attrs={"class": "new-class-name two", "rows": 1}))   # talap edilenok
    price = forms.DecimalField(initial=16515.99)
