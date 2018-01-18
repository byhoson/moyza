from django.contrib import admin
from .models import Lightning, Comment, Catcher


@admin.register(Lightning)
class LightningAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Catcher)
class CatcherAdmin(admin.ModelAdmin):
    pass
