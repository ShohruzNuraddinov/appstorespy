from django.db import models
from django.contrib.auth.models import User

from utils.models import BaseModel

# Create your models here.
PENDING = "Pending"
CANCELLED = "Cancelled"
COMPLETED = "Completed"
IN_PROGRESS = "In Progress"
FAILED = "Failed"

FILE_STATUS = (
    ("pending", PENDING),
    ("cancelled", CANCELLED),
    ("completed", COMPLETED),
    ("in_progress", IN_PROGRESS),
    ("failed", FAILED),
)


# Files Model
class File(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to="files/")
    out_file = models.FileField(
        upload_to="files/results/", blank=True, null=True
    )
    status = models.CharField(
        max_length=20, choices=FILE_STATUS, default=PENDING)
