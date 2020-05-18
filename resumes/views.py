from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect
from . import models


class HomeView(ListView):

    model = models.Resume
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "resumes"
