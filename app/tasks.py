from celery import shared_task

from app import models
from app.utils import File


@shared_task
def image_resize(obj, filename, pixel):
    # Task logic here
    # result = arg1 + arg2
    obj.status = models.IN_PROGRESS
    obj.save()
    file = File().image_resize(obj.id, filename, pixel)
    obj.file = file
    obj.status = models.COMPLETED
    obj.save()
    return obj
