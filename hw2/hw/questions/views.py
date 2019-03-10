from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Question
from .form import QuestionForm


class IndexView(ListView):

    model = Question
    template_name = 'index.html'

    def get_queryset(self):
        return Question.objects.order_by('-id')
    
class QuestionView(DetailView):

    model = Question
    template_name = 'question.html'

    def get_form(self):
        return AnswerForm(initial={'question': self.kwargs['pk']})
    
class AskView(CreateView):

    model = Question
    form_class = QuestionForm
    template_name = 'ask.html'
