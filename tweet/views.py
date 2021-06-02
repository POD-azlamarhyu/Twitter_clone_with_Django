from django.shortcuts import render,redirect,get_object_or_404
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
        "tweet" : tweet,
    }

    return render(request,'tweet/tweetdetail.html',context)

def tweetListView(request,*args,**kwargs):
    qs = Tweet.objects.all()
    #tweetList = [{"id" : x.id,"text":x.text} for x in qs]

    context = {
        "tweetlist" : qs
    }

    return render(request,"tweet/tweet.html",context)

def tweetCreateView(request,*args,**kwargs):

    user = request.user

    if not request.user.is_authenticated:
        if request.is_ajax():
            return JsonResponse({},status=401)

        return redirect(settings.LOGIN_URL)

    form = TweetForm()

    if request.method == "POST":
        form = TweetForm(request.POST)
        
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = user
            tweet.save()
        # messages.success(request,"投稿しました")
        
        return redirect('tweet:tweetlist')
    context = {
        "form" : form,
    }

    return render(request,"tweet/tweetform.html",context)

def tweetEditView(request,tweet_id,*args,**kwargs):

    tweet = Tweet.objects.get(id=tweet_id)
    form = TweetForm(instance=tweet)
    
    if request.method == "POST":
        form = TweetForm(request.POST,instance=tweet)
        if form.is_valid():
            form.save()
            # messages.success(request,"修正しました")
            # tweet.save()
            return redirect('tweet:tweetlist')
    
    context = {
        "form":form
    }

    return render(request,"tweet/tweetedit.html",context)

def tweetDeleteView(request,tweet_id,*args,**kwargs):
    tweet = Tweet.objects.get(id=tweet_id)

    if request.method == "POST":
        tweet.delete()

        return redirect('tweet:tweetlist')

    context = {
        "tweet":tweet,
        "tweet_id":tweet_id
    }

    return render(request,'tweet/tweetdelete.html',context)

    
