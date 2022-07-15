from django.contrib import admin

from .models import Question, Choice                                # <--- 2.7.1 - Choice added at 7.2

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):                              # 7.1.1
    # fields = ['pub_date', 'question_text']                        # 7.1.1 - updated to 7.1.2
    fieldsets = [
        (None,               {'fields': ['question_text']}),                                # 7.1.2
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),            # 7.1.2   
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']
                                        
admin.site.register(Question, QuestionAdmin)                        # <--- 2.7.1     - QuestionAdmin added at 7.1

