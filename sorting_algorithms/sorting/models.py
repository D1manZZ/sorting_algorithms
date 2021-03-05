from django.db import models


class SortingAlgorithms(models.Model):

    algorithm = models.CharField('алгоритм сортировки', max_length=30)

    def __str__(self):
        return self.algorithm

    class Meta:
        verbose_name = 'Алгоритм'
        verbose_name_plural = 'Алгоритмы'


class SortingData(models.Model):

    algorithm = models.ForeignKey(SortingAlgorithms, verbose_name='алгоритм сортировки', on_delete=models.CASCADE)
    start_time = models.DateTimeField('время сортировки', auto_now_add=True)
    sorting_duration = models.CharField('длительность сортировки', max_length=30)
    input_file = models.FileField('исходный файл', upload_to='files_inputs')
    output_file = models.FileField('результат сортировки', upload_to='files_outputs')

    def __str__(self):
        return f'Алгоритм сортировки {self.algorithm} успешно выполнен за {self.sorting_duration} секунд'

    class Meta:
        verbose_name = 'Успешная сортировка'
        verbose_name_plural = 'Успешные сортировки'
