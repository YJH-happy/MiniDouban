from django.urls import path
from . import views

urlpatterns = [
 path('bookhome', views.bookhome, name='bookhome'),
 path('<int:book_id>',views.bookdetail,name='bookdetail'),
 path('<int:book_id>/createbookreview', views.createbookreview, name='createbookreview'),
 path('reviewbook/<int:review_id>', views.updatebookreview, name='updatebookreview'),
path('review/<int:review_id>/delete', views.deletebookreview, name='deletebookreview'),
]