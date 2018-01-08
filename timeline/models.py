from django.db import models

# Create your models here.


class ContinentModel(models.Model):
    continent = models.CharField('大洲', max_length=10)

    def __str__(self):
        return self.continent


class CountryModel(models.Model):
    continent = models.ForeignKey(ContinentModel, on_delete=models.CASCADE)
    country = models.CharField('国家', max_length=100)
    # historytimeline = models.ForeignKey('HistoryTimeline', on_delete=models.CASCADE)

    def __str__(self):
        return self.country


class PersonModel(models.Model):
    name = models.CharField('姓名', max_length=100)
    birthday = models.CharField('出生日期', max_length=100, blank=True, null=True)
    death = models.CharField('去世日期', max_length=100, blank=True, null=True)
    country = models.ForeignKey(CountryModel, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.CharField('出生地', max_length=100, blank=True, null=True)
    abstract = models.CharField('人物简介', max_length=100)
    detailed = models.TextField('人物介绍')

    def __str__(self):
        return self.country


class HistoryTimeline(models.Model):

    # continent = models.CharField('大洲', max_length=100, blank=True, null=True)
    country = models.ForeignKey(CountryModel, related_name='timeline', on_delete=models.CASCADE)
    BC = models.BooleanField('公元前')
    time = models.CharField('发生时间', max_length=100)
    dynasty = models.CharField('朝代/时代', max_length=100, blank=True, null=True)
    person = models.CharField('人物', max_length=100, blank=True, null=True)
    address = models.CharField('地点', max_length=100, blank=True, null=True)
    abstract = models.CharField('事件简介', max_length=100)
    detailed = models.TextField('事件详细')

    def __str__(self):
        return self.abstract

    class Meta:
        ordering = ['time']
