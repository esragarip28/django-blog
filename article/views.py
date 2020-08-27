from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.contrib.auth import authenticate
from  .models import ArticleModel ,Article,Comment
from django.contrib import messages
import article.views

# Create your views here.


def comment(request,id):
    article=get_object_or_404(Article,id=id)
    if request.method == 'POST' and  request.user.is_authenticated:
        comment_content=request.POST.get("comment_content")
        newComment=Comment(comment_author=request.user,comment_content=comment_content)
        newComment.article=article
        newComment.save()
        return redirect("/article/"+str(id))
       
    elif request.user.is_authenticated==False:
        messages.warning(request,"Yorum yapabilmeniz için lütfen giriş yapınız....")
        return redirect("login")
    #value=str(article.id)

    return redirect(reverse("comment",kwargs={"id":id}))  

def index(request):
    article=ArticleModel.objects.filter(id=1).first()
    return render(request,'index.html',{"article":article})

def about(request):
    article=ArticleModel.objects.filter(title="ESRA GARİP").first()
    return render(request,"about.html",{"article":article})


def articles(request):
    if 'keyword' in request.GET:
        search_term=request.GET['keyword']
        articles = Article.objects.all().filter(title__contains=search_term)
        if articles:
            return render(request,"articles.html",{"articles":articles})
        messages.warning(request,"Böyle bir makale bulunmamaktadır...")    
        return redirect("articles")   
    else :
        articles=Article.objects.all()
        if articles:
            context={"articles":articles}
            return render(request,'articles.html',context)
    messages.warning(request,"Henüz Makale Bulunmamaktadır...")
    return render(request,'articles.html')


def article(request,id) :
    
    article=Article.objects.filter(id=id).first()  
    comments=article.comments.all() #sagdaki comments related_name 
    if article:
        context={"article":article,"comments":comments}
        return render(request,"article.html",context)

    messages.warning(request,"Böyle bir makale bulunmamaktadır...")    
    return redirect("index")   
  
   
def allArticles(request):
    articles=Article.objects.all()
    if articles:
        context={"articles":articles}    
        
        return render(request,"allArticles.html",context)
    messages.info(request,"Bu blog için henüz makale bulunmamaktdır...")
    return render(request,"allArticles.html")



