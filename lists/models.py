from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    title = models.CharField(max_length=100)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    resumes = models.ManyToManyField("resumes.Resume", related_name="lists")

    def __str__(self):
        return self.title

    def count_resumes(self):
        return self.resumes.count()

    count_resumes.short_description = "Number of Resumes"
