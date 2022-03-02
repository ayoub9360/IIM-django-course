from django.contrib import admin
from .models import Question
from .models import Member


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
  fields = ['text']

admin.site.register(Question)
admin.site.register(Member)
