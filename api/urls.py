from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/", views.BlogPostListCreate.as_view(), name="blogpost-list-create"),
    path("blogpost/<int:pk>/", views.BlogPostRetrieve.as_view(), name="blogpost-retrieve"),
    path("blogpost/<int:pk>/update/", views.BlogPostUpdate.as_view(), name="blogpost-update"),
    path("blogpost/<int:pk>/delete/", views.BlogPostDestroy.as_view(), name="blogpost-delete"),
]

