from django.contrib import admin
from .models import Category, Channel, Program


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'category_uz',
        'category_ru'
    ]

    class Meta:
        model = Category


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'Channel_name',
        'Channel_image'
    ]

    class Meta:
        model = Channel


@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'Program_name',
        'Program_time',
        'Channel'
    ]

    class Meta:
        model = Program
