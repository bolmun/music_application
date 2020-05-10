from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    professionailsm = models.IntegerField()
    kindness = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    resume = models.ForeignKey(
        "resumes.Resume", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} - {self.review}"

    def rating_avg(self):
        avg = (
            self.accuracy + self.communication + self.professionailsm + self.kindness
        ) / 4
        return round(avg, 1)

    rating_avg.short_description = "Review Average"
