"""
Used for import libaries
"""
from django.shortcuts import render


# Create your views here.
def get_todo_list(request):
    """
    Returns the html template todo_lists.html
    """
    return render(request, 'todo/todo_list.html')
