from django.contrib import admin
from base.models import Room, Topic, Message, User



admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)