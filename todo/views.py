from django.shortcuts import render

# Create your views here.
def Homeview(request):
    return render(request, 'todo/index.html')

def Todoview(request):
    return render(request, 'todo/todo_list.html')