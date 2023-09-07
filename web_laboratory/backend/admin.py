from django.contrib import admin
from .models import Staff
# Register your models here.


class StaffAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'employee',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


# При регистрации модели Staff источником конфигурации для неё назначаем
# класс StaffAdmin
admin.site.register(Staff, StaffAdmin)
