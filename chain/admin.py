from django.contrib import admin

from chain.models import ChainUnit


@admin.register(ChainUnit)
class ChainUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'country', 'supplier', 'debt', 'hierarchy_level', 'creation_date')
    list_filter = ('country',)
