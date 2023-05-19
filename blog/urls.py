from django.urls import path
from . import views

urlpatterns = [
    # previously we r pointing starting page view after changing StartingPage fun to StartingPageView class 
    # now we have to pointing StartingPageView and call as_view
    # path("",views.starting_page, name="starting-page"),
    path("",views.StartingPageView.as_view(), name="starting-page"),
    path("posts",views.AllPostView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page") 
    # /posts/my-first-post
    
]
