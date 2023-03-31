from . import views
from django.urls import path


urlpatterns = [
    path("create/", views.CreateCategoryView.as_view(), name="create_category"),
    path("all/", views.CategoryListView.as_view(), name="category_list"),
    path(
        "category-detail/<uuid:category_id>",
        views.CategoryDetailView.as_view(),
        name="category_detail",
    ),
    path(
        "update-category/<uuid:category_id>",
        views.UpdateCategoryView.as_view(),
        name="update_category",
    ),
    path(
        "delete-category/<uuid:category_id>",
        views.DeleteCategoryView.as_view(),
        name="delete_category",
    ),
]
