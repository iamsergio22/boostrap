from django.urls import path
from . import views

urlpatterns = [
   path('get/',views.getBooks),
   path('post/',views.postBook),
   path('put/<int:id>/',views.putBook),
   path('delete/<int:id>/',views.deleteBook),
]