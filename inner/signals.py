from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User_survey,Fillers


@receiver(post_save, sender=User_survey)
def create_country_state(sender, instance, created, **kwargs):
    if created:
        Fillers.objects.create(survey=instance)


@receiver(post_save, sender=User_survey)
def save_country_state(sender, instance, **kwargs):
    instance.fillers.save()
