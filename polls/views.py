from django.shortcuts import render

def index(request):
    context = {
        "user_name": "Tushar",
        "topics": ["HTML", "CSS", "Python", "Django"]
    }
    return render(request, "polls/index.html", context)
