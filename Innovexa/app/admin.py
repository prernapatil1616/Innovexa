from django.contrib import admin
from .models import *


class what_you_learn_TabularInline(admin.TabularInline):
    model = what_you_learn


class Requiremnets_TabularInline(admin.TabularInline):
    model = Requirement


class challenge_admin(admin.ModelAdmin):
    inlines = (what_you_learn_TabularInline, Requiremnets_TabularInline)


admin.site.register(Categories)
admin.site.register(Level)
admin.site.register(Challenge, challenge_admin)
admin.site.register(what_you_learn)
admin.site.register(Requirement)
admin.site.register(SubmitForm)
