from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Cook


@receiver(post_save, sender=Cook)
def send_email_on_new_cook(sender, instance, created, **kwargs):

    if created:
        message = f"Hello, {instance.username}! You are in the army now."
        print(message)
