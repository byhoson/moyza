from django.contrib import admin
from .models import Lightning, Comment, Catch


@admin.register(Lightning)
class LightningAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Catch)
class CatchAdmin(admin.ModelAdmin):
    pass
