from django.db import models
from helpers.models import TrackingModel
from authenticate.models import User

class Todo(TrackingModel):
    title = models.CharField(max_length=100,blank=False)
    description = models.TextField()
    status = models.BooleanField(default=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title