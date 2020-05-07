from django.db import models
from core import models as core_models
from users import models as user_models


class AbstractItem(core_models.TimeStampedModel):

    title = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class instrumentChoice(AbstractItem):
    class Meta:
        verbose_name = "Instrument Choice"


class LessonType(AbstractItem):
    class Meta:
        verbose_name = "Lesson Type"


class PreferStyle(AbstractItem):
    class Meta:
        verbose_name = "Prefered Style"


class LessonDay(AbstractItem):
    class Meta:
        verbose_name = "Lesson Day"


class Advertisement(core_models.TimeStampedModel):

    LESSON_HOBBY = "hobby"
    LESSON_EXAM = "entrance exam"

    LESSON_CATEGORY = ((LESSON_EXAM, "입시"), (LESSON_HOBBY, "취미"))

    COUNT_ONE = "1"
    COUNT_TWO = "2"
    COUNT_THREE = "3"
    COUNT_TBD = "tbd"

    COUNT_CHOICE = (
        (COUNT_ONE, "1주일 1회"),
        (COUNT_TWO, "1주일 2회"),
        (COUNT_THREE, "1주일 3회"),
        (COUNT_TBD, "추후 협의"),
    )

    LESSON_TIME_MORNING = "am.9 - pm.12"
    LESSON_TIME_EARLY_AFTERNOON = "pm.12 - pm.3"
    LESSON_TIME_LATE_AFTERNOON = "pm.3 - pm.6"
    LESSON_TIME_EVENING = "pm.6 - pm.9"

    LESSON_TIME_CHOICE = (
        (LESSON_TIME_MORNING, "am.9 - pm.12"),
        (LESSON_TIME_EARLY_AFTERNOON, "pm.12 - pm.3"),
        (LESSON_TIME_LATE_AFTERNOON, "pm.3 - pm.6"),
        (LESSON_TIME_EVENING, "pm.6 - pm.9"),
    )

    student = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    instrument = models.ForeignKey(instrumentChoice, on_delete=models.CASCADE)
    category = models.CharField(max_length=10, choices=LESSON_CATEGORY)
    current_skill = models.TextField()
    skill_reference = models.FileField(null=True, blank=True)
    goal = models.CharField(max_length=100)
    lesson_count_per_week = models.CharField(
        max_length=10, choices=COUNT_CHOICE, blank=True, null=True
    )
    desired_lesson_days = models.ManyToManyField(LessonDay)
    desired_lesson_time = models.CharField(
        max_length=20, choices=LESSON_TIME_CHOICE, blank=True, null=True
    )
    desired_starting_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    wanna_test_class = models.BooleanField(default=False)
    lesson_type = models.ManyToManyField(LessonType)
    prefer_style = models.ManyToManyField(PreferStyle)

    def __str__(self):
        return f"{self.instrument}렛슨, 목표는 {self.goal}"
