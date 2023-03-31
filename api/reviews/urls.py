from django.urls import path
from .import views


urlpatterns = [
    path("create/", views.CreateReviewView.as_view(), name="create_review"),
    path("list/", views.ReviewListView.as_view(), name="review_list"),
]
