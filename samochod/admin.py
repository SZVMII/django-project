from django.contrib import admin
from . import models


class PartAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        'model',
        'mark',
        'startOfProduction',
        'endOfProduction',
        'engines',
        'bodyType',
        'partName',
        'partOpis',
        'user_added',
        'status',
    )


admin.site.register(models.Part, PartAdmin)
