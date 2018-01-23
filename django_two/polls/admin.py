from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
            ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')


# Without the QuestionAdmin argument, this just creates the default admin page
# with fields for all attributes of Questions with no fields for choices.
admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
