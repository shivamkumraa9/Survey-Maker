from django.contrib import admin
from .models import User_survey,Question,Answer,Fillers

admin.site.register(User_survey)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Fillers)
