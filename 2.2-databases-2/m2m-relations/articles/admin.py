from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Scope

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        check = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            if form.cleaned_data:
                if form.cleaned_data['is_main']:
                    check += 1
        if check == 0:
            raise ValidationError('Не выбран основной раздел')
        elif check > 1:
            raise ValidationError('Основной раздел может быть только один')
        else: return super().clean()  # вызываем базовый код переопределяемого метода

class RelationshipInline(admin.TabularInline):
    model = Scope
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [RelationshipInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']










