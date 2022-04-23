from django.contrib import admin
from . import models

admin.site.register(models.Cover)
admin.site.register(models.Attachment)
admin.site.register(models.Label)
admin.site.register(models.Checklist)
