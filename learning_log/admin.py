from django.contrib import admin

# Register your models here.
from learning_log.models import Topic, Entry

admin.site.register(Entry)
admin.site.register(Topic)
