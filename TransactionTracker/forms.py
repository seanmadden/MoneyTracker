from django import forms
from django.contrib.auth.models import User
from TransactionTracker.models import transaction_type


class EntryForm(forms.Form):
    user = forms.ModelChoiceField(label="User",
                                  queryset=User.objects.all(),
                                  initial=0,
                                  widget=forms.Select(
                                      attrs={'class': 'form-control'}))

    type = forms.ModelChoiceField(label="Type",
                                  queryset=transaction_type.objects.all(),
                                  initial=0,
                                  widget=forms.Select(
                                      attrs={'class': 'form-control'}
                                  ))

    amount = forms.DecimalField(decimal_places=2,
                                widget=forms.TextInput(
                                    attrs={"class": "form-control"}))

    description = forms.CharField(max_length=50,
                                  widget=forms.TextInput(
                                      attrs={"class": "form-control"}
                                  ))
