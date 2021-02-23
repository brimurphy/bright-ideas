from django.contrib import admin
from .models import TradesPeople


class TradespeopleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'location',
        'email',
        'rating',
    )

    ordering = ('name',)


admin.site.register(TradesPeople, TradespeopleAdmin)
