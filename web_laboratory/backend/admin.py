from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Staff, Project

# Register your models here.


@admin.register(Staff)
class StaffAdmin(TranslationAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'employee', 'position', )
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('employee',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'author', 'pub_date')
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


# При регистрации модели Staff источником конфигурации для неё назначаем
# класс StaffAdmin
# admin.site.register(Staff, StaffAdmin)
# admin.site.register(Project, ProjectAdmin)
