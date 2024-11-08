from django.shortcuts import render,redirect
from .models import Book,Reviewbook
from .forms import ReviewForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.

def bookhome(request):
    searchTerm = request.GET.get('searchBook')
    if searchTerm:
        book_list = Book.objects.filter(title__contains=searchTerm)
    else:
        book_list = Book.objects.all().order_by('id')
    paginator = Paginator(book_list, 3)
    page_number = request.GET.get('page', 1)
    books = paginator.page(page_number)
    return render(request,"bookhome.html",
                  {'searchTerm':searchTerm,
                  'books':books})
def bookdetail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Reviewbook.objects.filter(book=book)
    return render(request, 'bookdetail.html',
                  {'book': book,"reviews":reviews})

def createbookreview(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'GET' :
        return render(request, 'createbookreview.html' ,
        {'form':ReviewForm , 'book':book})
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.book = book
            newReview.save()
            return redirect('bookdetail',newReview.book.id)
        except ValueError:
            return render(request,'createbookreview.html',
                          {'form':ReviewForm, 'error':'非法数据'})

def updatebookreview(request, review_id) :
    review = get_object_or_404(Reviewbook, pk=review_id, user=request.user)
    if request.method == 'GET':
        form = ReviewForm(instance=review)
        return render(request, 'updatebookreview.html', {'review':review, 'form':form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect('bookdetail', review.book.id)
        except ValueError:
            return render(request, 'updatebookreview.html',
                          {'review':review, 'form':form, 'error':'提交非法数据'})

def deletebookreview(request, review_id) :
    review = get_object_or_404(Reviewbook, pk=review_id, user=request.user)
    review.delete()
    return redirect('bookdetail', review.book.id)