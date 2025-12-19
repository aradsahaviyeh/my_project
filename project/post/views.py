from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from django.db.models import F
from .models import Post, Comment
from django.urls import reverse
# Create your views here.


def home(request):
    template = loader.get_template("post/home.html")
    return HttpResponse(template.render())


def post_list(request):
    posts = get_list_or_404(Post)
    template = loader.get_template("post/post_list.html")
    return HttpResponse(template.render(context={"posts": posts})) 
    # return render(request, "post/post_list.html", {"posts": posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        selected_post = request.POST["like"]
        if post.id == int(selected_post):
            post.votes = F("votes") + 1
            post.save()
            return redirect(reverse("post:post_detail", args=(post.id,)))
    return render(request, "post/post_detail.html", context={"post":post})

def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        caption = request.POST.\
        get("caption")
        post = Post(title=title, caption=caption)
        post.save()
        post_id = post.id
        return HttpResponse("your post it's created at :\
             <br>\
             <a href=\"/post/post_detail/%s\"> link </a>"%(post_id))
    else:
        return render(request, "post/form.html")    
    

def post_vote(request, id):
    post = get_object_or_404(Post, id=id)
    post.votes = F("votes") + 1
    post.save()
    return redirect("/post/post_list")



def comment_vote(request, id):
    post = get_object_or_404(Post, id=id)
    try:
        comment = post.comment_set.get(id = request.POST.get("comment"))
    except Exception:
        return render(
            request,
            "post/post_detail.html",
            {
                "post" : post,
                "error" : "you can't like this comment",
            }
        )
    else:
        comment.votes += 1
        comment.save()

        return redirect(reverse("post:post_detail", args=(post.id,)))