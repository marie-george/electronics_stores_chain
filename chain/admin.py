from django.contrib import admin

from chain.models import ChainUnit


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(ChainUnit)
class ChainUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'country', 'city', 'supplier', 'debt', 'hierarchy_level', 'creation_date')
    list_filter = ('country', 'city')
    actions = [clear_debt]
