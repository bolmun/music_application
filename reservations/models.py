import datetime
from django.db import models
from django.utils import timezone
from core import models as core_models


class Reservation(core_models.TimeStampedModel):

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICE = (
        (STATUS_PENDING, "예약 내역 확인 중"),
        (STATUS_CONFIRMED, "예약 확정"),
        (STATUS_CANCELED, "예약 취소"),
    )

    status = models.CharField(
        max_length=15, choices=STATUS_CHOICE, default=STATUS_PENDING
    )
    student = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    resume = models.ForeignKey(
        "resumes.Resume", related_name="reservations", on_delete=models.CASCADE
    )
    meeting_time = models.DateTimeField()
    meeting_address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.student}님 | {self.status} | 예약 시간: {self.meeting_time} | 장소 : {self.meeting_address}"

    def in_progress(self):
        now = timezone.now()
        meeting_end = self.meeting_time + datetime.timedelta(hours=1)
        return now > self.meeting_time and now < meeting_end

    in_progress.boolean = True

    def is_finished(self):
        now = timezone.now()
        meeting_end = self.meeting_time + datetime.timedelta(hours=1)
        return now > meeting_end

    is_finished.boolean = True
