from datetime import date
from typing import Any, Dict
from django.db.models.query import QuerySet

from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView

from .models import Post
from .forms import CommentForm
# Create your views here.

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data 

# convert function view to class view then do changes in blog/urls

# def starting_page(request):
#     #fetching post for starting page
#     latest_posts= Post.objects.all().order_by("-date")[:3]
#     return render(request,"blog/index.html", {
#         "posts":latest_posts
#     })

class AllPostView(ListView):
    template_name = "blog/all-posts.html"
    model= Post
    ordering= ["-date"]
    context_object_name = "all_posts"

    # def get_queryset(self):
    #      queryset = super().get_queryset()
    #      super().get_queryset()

# def posts(request):
#     all_posts= Post.objects.all().order_by("date")
#     return render(request,"blog/all-posts.html",{
#         "all_posts": all_posts
#     })

class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model= Post 
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context["post_tag"] = self.object.tag.all()
        context["comment_form"]= CommentForm()
        return context


# def post_details(request, slug):
#     # identified_post = Post.objects.get(slug=slug)
#     identified_post = get_object_or_404(Post,slug=slug)
#     return render(request,"blog/post-detail.html",{
#       "post" :identified_post,
#       "post_tag": identified_post.tag.all()
#     })






# {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpg",
#         "author": "Archana Bharadwaj",
#         "date": date(2023, 1, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Ishika Kumari",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "author": "Hari Rocks✌️",
#         "date": date(2023, 4, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }