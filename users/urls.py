# users/urls.py

from django.urls import path
from django.urls import path

from users.views import dashboard

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
]


from django.urls import path

from . import views


app_name = "users"
urlpatterns = [
    path("dashboard", views.dashboard.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]