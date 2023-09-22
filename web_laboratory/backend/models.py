from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Staff(models.Model):
    text = models.TextField(
        'Текст о сотруднике'
    )
    employee = models.CharField(
        'Имя сотрудника',
        max_length=200,
    )
    position = models.TextField(
        'Звание/Должность'
    )
    image = models.ImageField(
        'Картинка',
        upload_to='staff/',
        blank=True
    )

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('staff_detail', kwargs={'post_pk': self.pk})

    class Meta:
        ordering = ['id']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Project(models.Model):
    title = models.CharField(
        'Название проекта',
        max_length=200
    )
    description = models.TextField(
        'Описание проекта'
    )
    author = models.CharField(
        'Автор проекта',
        max_length=200,
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
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
        ordering = ['-pub_date']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
