from django.shortcuts import render,redirect
from .models import Movie,Review
from .forms import ReviewForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def moviehome(request):
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movie_list = Movie.objects.filter(title__contains=searchTerm)
    else:
        movie_list = Movie.objects.all().order_by('id')
    paginator = Paginator(movie_list, 3)
    page_number = request.GET.get('page',1)
    movies = paginator.page(page_number)
    return render(request,"moviehome.html",
                  {'searchTerm':searchTerm,
                  'movies':movies})
    # return HttpResponse(
    #     # '<h1>欢迎来到movie应用首页</h1>'
    #     # '<h2>电影</h2>'
    #     # '<h3>正在热映</h3>'
    #     # '<h4>刺猬</h4>'
    #     # '<h5>电影评分</h5>'
    #     # '<h4>姥姥的外孙</h4>'
    #     # '<h4>野孩子</h4>'
    # )
def home(request):
    return render(request,"home.html",
                  {'name':'YJH'})
    # return HttpResponse(
    #     '<h1>欢迎来到项目首页</h1>'
    # )
def signup(request):
    email = request.GET.get('email')
    return render(request,'signup.html',
                  {'email':email})

def moviedetail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews=Review.objects.filter(movie=movie)
    return render(request, 'moviedetail.html',
                  {'movie': movie, 'reviews':reviews})

@login_required
def createmoviereview(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET' :
        return render(request, 'createmoviereview.html' ,
        {'form':ReviewForm , 'movie':movie})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect('moviedetail',newReview.movie.id)
        except ValueError:
            return render(request,'createmoviereview.html', {'form':ReviewForm, 'error':'非法数据'})

@login_required
def updatemoviereview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatemoviereview.html',
                      {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('moviedetail', review.movie.id)
        except ValueError:
            return render(request, 'updatemoviereview.html',
                          {'review':review, 'form':form, 'error':'提交非法数据'})

@login_required
def deletemoviereview(request, review_id) :
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect('moviedetail', review.movie.id)