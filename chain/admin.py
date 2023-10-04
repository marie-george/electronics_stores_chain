from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from chain.models import ChainUnit


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(ChainUnit)
class ChainUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'name', 'country', 'city', 'link_to_chain', 'debt', 'hierarchy_level', 'creation_date')
    list_filter = ('country', 'city')
    actions = [clear_debt]

    def link_to_chain(self, obj):
        if obj.supplier:
            link = reverse("admin:chain_chainunit_change", args=[obj.supplier.id])
            return format_html('<a href="{}">{}</a>', link, obj.supplier.name)
        return '-'
    link_to_chain.short_description = 'Edit chain'

