from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('delete/<int:id>', views.delete_own_comment, name='delete_comment'),
    #path('edit/<comment_id>', edit_own_comment, name='edit_comment')
    path("edit/<comment_id>", views.edit_own_comment, name='edit_comment'),
]
