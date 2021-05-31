from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,JsonResponse
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def tweetDetailView(request,tweet_id,*args,**kwargs):

    """
    Rest API View
    return json
    """

    # context = {
    #     "id" : tweet_id,
    # }

    # status = 200

    # try:
    #     tweet = Tweet.objects.get(id=tweet_id)
    #     context["text"] = tweet.text
    # except:
    #     context["message"] = "Not found"
    #     status = 404

    # return JsonResponse(context,status=status)


    """
    Dynamic Routing
    """
    try:
        tweet = Tweet.objects.get(id = tweet_id)
    except:
        raise Http404
    
    context = {
        "tweet" : tweet
    }

    return render(request,'tweet/tweet.html',context)

def tweetListView(request,*args,**kwargs):
    qs = Tweet.objects.all()
    tweetList = [{"id" : x.id,"text":x.text} for x in qs]

    context = {
        "tweetlist" : qs
    }

    return render(request,"tweet/tweet.html",context)

def tweetCreateView(request,*args,**kwargs):
    form = TweetForm(request.POST or None)

    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.save()
        messages.success(request,"投稿しました")
        form = TweetForm()
    
    context = {
        "form" : form
    }

    return render(request,"tweet/tweetform.html",context)


