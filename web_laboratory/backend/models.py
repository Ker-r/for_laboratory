from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Staff(models.Model):
    text = models.TextField(
        'Текст о сотруднике'
    )
    employee = models.CharField(max_length=200)
    image = models.ImageField(
        'Картинка',
        upload_to='staff/',
        blank=True
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=200)
    image = models.ImageField(
        'Картинка',
        upload_to='project/',
        blank=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'post_pk': self.pk})

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
