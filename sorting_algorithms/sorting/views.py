from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import AddSort
from .models import AddSorting
from .algorithms import *


class SortNums(CreateView):
    form_class = AddSort
    template_name = 'sorting/sort_nums.html'
    success_url = reverse_lazy('sort_data')

    def form_valid(self, form):
        form.save()
        s = AddSorting()
        s.algorithm = form.instance.algorithm
        if str(form.instance.algorithm) == 'Пузырьковый':
            sort_class = BubbleSort()
        elif str(form.instance.algorithm) == 'Выборкой':
            sort_class = SelectionSort()
        elif str(form.instance.algorithm) == 'Вставками':
            sort_class = InsertionSort()
        elif str(form.instance.algorithm) == 'Слиянием':
            sort_class = MergeSort()
        file = open(form.instance.input_file.path, 'r')
        nums = ",".join(file.readlines())
        nums = list(map(lambda x: int(x), filter(lambda x: x != '\n', nums.split(','))))
        result = sort_class._SortNums__make_sort(self, nums)
        s.sorting_duration = result[0]
        s.sort_result = result[1]
        s.save()
        return super().form_valid(form)


class SortData(ListView):
    model = AddSorting
    template_name = 'sorting/sort_data.html'
    context_object_name = 'sort'

