
#imports
from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator



def movie_list(request):

    movies_object=Movies.objects.all()

    movie_name=request.GET.get('movie_name') #to get the data the user wants to search for


    #filtering out the movie data base and displaying the filtered result according to the user request in the html file
    if movie_name != '' and movie_name is not None:
        movies_object=movies_object.filter(name__icontains=movie_name) 


    paginator=Paginator(movies_object , 4) #telling the paginator which items to paginate and the number of items per page ! 
    page=request.GET.get('page')
    movies_object=paginator.get_page(page) #the movie objects in the requested page !

    return render (request,
                    './movie_list.html/',
                   {'movie_objects' : movies_object})

