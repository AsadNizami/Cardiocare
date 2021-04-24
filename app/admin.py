from django.contrib import admin
from .models import Test


class TestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date')



admin.site.register(Test)
admin.site.site_header = 'Cardiocare Diagnostics'
admin.site.site_title = 'Cardiocare Dashboard'
admin.site.index_title = 'Cardiocare Admin'
