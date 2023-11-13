from modeltranslation.translator import register, TranslationOptions
from .models import Staff, Project


@register(Staff)
class StaffTranslationOptions(TranslationOptions):
    fields = ('text', 'employee', 'position')


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'author')
