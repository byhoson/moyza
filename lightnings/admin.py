from django.contrib import admin
from .models import Lightning, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Lightning)
class LightningAdmin(admin.ModelAdmin):
    pass
