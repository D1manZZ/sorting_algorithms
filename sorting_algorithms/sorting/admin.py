from django.contrib import admin
from .models import SortingAlgorithms, AddSorting, SortingForm


class AddSortingAdmin(admin.ModelAdmin):
    list_display = ['algorithm', 'start_time', 'sorting_duration']
    list_filter = ['algorithm']
    search_fields = ['algorithm', 'start_time', 'sorting_duration']


admin.site.register(SortingAlgorithms)
admin.site.register(AddSorting, AddSortingAdmin)
