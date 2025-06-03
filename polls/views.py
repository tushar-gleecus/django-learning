from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "polls/result.html", {"name": form.cleaned_data["name"]})
    else:
        form = FeedbackForm()
    return render(request, "polls/feedback.html", {"form": form})
