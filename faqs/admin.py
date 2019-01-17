from django.contrib import admin
from .models import FrequentQuestions, FrequentQuestionsAnswers
# Register your models here.


class FrequentQuestionsInline(admin.StackedInline):

    model = FrequentQuestionsAnswers
    max_num = 1


class FrequentQuestionsAdmin(admin.ModelAdmin):

    inlines = [FrequentQuestionsInline]


admin.site.register(FrequentQuestions, FrequentQuestionsAdmin)

