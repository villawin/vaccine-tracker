from django.db.models import fields
from django.forms import widgets
import django_filters
from django.forms.widgets import *
from django_filters import DateFilter
from django_filters.filters import CharFilter, DateFromToRangeFilter, NumberFilter
from .models import *


class PatientFilter(django_filters.FilterSet):
    id = NumberFilter(widget=NumberInput(attrs={'class': 'form-control', 'placeholder': 'Record Number'}), 
                        lookup_expr='icontains', label='Record Number'
    )
    first_name = CharFilter(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), 
                            lookup_expr='icontains', label='First Name'   
    )
    last_name = CharFilter(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), 
                            lookup_expr='icontains', label='Last Name'
    )
    birthdate = DateFilter(widget=NumberInput(attrs={'type': 'date','class': 'form-control', 'placeholder': 'Date of Birth'})
    ,input_formats=['%m-%d-%Y'])

    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'birthdate']

class PhysicianFilter(django_filters.FilterSet):
    first_name = CharFilter(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), 
                            lookup_expr='icontains', label='First Name'   
    )
    last_name = CharFilter(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), 
                            lookup_expr='icontains', label='Last Name'
    )
    title = CharFilter(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}), 
                            lookup_expr='icontains', label='Title'
    )
    user = CharFilter(widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}), 
                            lookup_expr='username', label='Username'
    )
    class Meta:
        model = Physician
        fields = ['first_name', 'last_name', 'title', 'user']