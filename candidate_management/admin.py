from django.contrib import admin

from .models import Candidate


class CandidateAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "gender", "email", ]
    list_filter = ["gender",]
    search_fields = ["email", "name", "phone_number"]


admin.site.register(Candidate, CandidateAdmin)
