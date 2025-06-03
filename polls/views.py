from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Feedback
from .forms import FeedbackForm
from django.contrib.auth.mixins import LoginRequiredMixin


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "polls/feedback.html"
    success_url = reverse_lazy("feedback_list")

class FeedbackListView(ListView):
    model = Feedback
    template_name = "polls/feedback_list.html"
    context_object_name = "feedbacks"
