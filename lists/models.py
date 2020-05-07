from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    title = models.CharField(max_length=100)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    resumes = models.ManyToManyField("resumes.Resume")

    def __str__(self):
        return self.title
