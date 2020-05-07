import datetime
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

    """Instrument Choice Model"""

    class Meta:
        verbose_name = "Instrument Choice"


class Resume(core_models.TimeStampedModel):

    DEGREE_ASSOCIATE = "Associate degree"
    DEGREE_BACHELOR = "Bachelor's degree"
    DEGREE_MASTER = "Master's degree"
    DEGREE_BACHELOR = "Doctorl degree"

    DEGREE_CHOICES = (
        (DEGREE_ASSOCIATE, "전문학사"),
        (DEGREE_BACHELOR, "학사"),
        (DEGREE_MASTER, "석사"),
        (DEGREE_BACHELOR, "박사"),
    )

    YEAR_CHOICES = []
    for r in range(1970, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    resume_title = models.CharField(max_length=100, default="렛슨 제안서 제목을 입력해주세요")
    instructor = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    instrument = models.ForeignKey(instrumentChoice, on_delete=models.CASCADE)
    final_degree = models.CharField(
        max_length=80, choices=DEGREE_CHOICES, null=True, blank=True
    )
    college = models.CharField(max_length=80, null=True, blank=True)
    is_graduated = models.BooleanField(default=False)
    graduate_year = models.IntegerField(
        ("year"),
        max_length=4,
        choices=YEAR_CHOICES,
        default=datetime.datetime.now().year,
        null=True,
        blank=True,
    )
    awards = models.TextField(null=True, blank=True)
    career = models.TextField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    fee = models.IntegerField()
    is_test_class_possible = models.BooleanField(default=False)
    is_super_instructor = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.instrument}렛슨 - {self.instructor},{self.city}"


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=100)
    file = models.ImageField()
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)

    def __str__(self):
        return self.caption
