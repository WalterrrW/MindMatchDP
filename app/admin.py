from django.contrib import admin
from .models import UserProfileDB
from .models import UserPersonalityDB
from .models import QuestionsDB

# Register your models here.
admin.site.register(UserProfileDB)
admin.site.register(UserPersonalityDB)
admin.site.register(QuestionsDB)
