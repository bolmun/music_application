import datetime
from django.db import models
from core import models as core_models


class Report(core_models.TimeStampedModel):

    student = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="student"
    )
    instructor = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="instructor"
    )
    goal = models.CharField(max_length=200)
    due_date = models.DateField(blank=True, null=True)
    lesson_date = models.DateField(default=datetime.date.today)
    lesson_contents = models.TextField()
    good_point = models.CharField(max_length=200, null=True, blank=True)
    bad_point = models.CharField(max_length=200, null=True, blank=True)
    achievement_score = models.IntegerField()
    homework = models.TextField()

    def __str__(self):
        return f"{self.student}님 {self.lesson_date} 진도표"
