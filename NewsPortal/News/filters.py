from .models import *
from django.forms import DateTimeInput
from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter
from django import forms


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='post_category',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=True,
    )

    added_after = DateTimeFilter(
        field_name='creation_time',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }
