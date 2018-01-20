# See cumbersome version - that why we have shortcuts!
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

from polls.models import Question, Choice

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

""" Cumbersome version

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
"""

def detail(request, question_id):
    # Why doesn't the get function just through a 404?
    # Becuase that means the model function messes with the view - not pretty
    # >> Coupling of model and view layer
    # What are the potential harms of this coupling? Like, would the get
    # function be called from outside views.py? It probably would be used a
    # lot within the model layer. I guess we'll see concrete examples later.
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

""" Cumbersome version
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
"""

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
