from django.contrib import admin
from timeline.models import ContinentModel, CountryModel, PersonModel, HistoryTimeline

# Register your models here.

admin.site.register([ContinentModel, CountryModel, PersonModel, HistoryTimeline])
