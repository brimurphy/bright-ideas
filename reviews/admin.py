from django.contrib import admin

from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    name = 'reviews'

    list_display = (
        'trades_person',
        'user',
        'rating',
        'comment',
        'date',
    )

    ordering = ('-date',)


admin.site.register(Reviews, ReviewsAdmin)
