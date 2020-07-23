from . import views as inn_views
from django.urls import path

app_name="inner"

urlpatterns=[
	path('',inn_views.home,name='home'),
	path('new/',inn_views.create_survey,name='new_survey'),
	path('profile/',inn_views.profile,name='profile'),
	path('details/<int:pk>/',inn_views.survey_detail,name='detail_survey'),
	path('delete-survey/<int:pk>/',inn_views.delete_survey,name='delete_survey'),
	path('fill/<int:pk>/',inn_views.fill_survey,name='fill_survey'),
]
