from django import forms


class NewItemForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)
    #photo = forms.CharField(max_length=100)
    price = forms.FloatField()

class UpdateItemForm(forms.Form):
    id = forms.IntegerField()
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=300)
    # photo = forms.CharField(max_length=100)
    price = forms.FloatField()