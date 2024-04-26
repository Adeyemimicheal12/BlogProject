from django.urls import path
from . import views

urlpatterns = [
    # the url to create and list all post
    path("post/",views.BlogPostListCreateView.as_view(),name="post_list_create"),
    
    # the url to list all post made by a user with the id user_id
    path("post/user/<int:user_id>/",views.UserBlogPostListView.as_view(),name="user_posts_by_id"),
    
    # the url to retrieve,update and delete a post by the post id
    path("post/<int:pk>/",views.BlogPostUpdateDeleteView.as_view(),name="post_retrieve_update_delete"),
    
    # the url to list and create category 
    path("category/",views.CategoryListCreateView.as_view(),name="category_list_create"),
    
    # the url to list a blog post associated to a catergory by the category_id
    path("category/<int:category_id>/",views.CateroryBlogListView.as_view(),name="category_posts_list"),
    
]