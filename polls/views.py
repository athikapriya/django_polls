from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list" : latest_question_list}
    return render(request, "polls/index.html", context )

def details(request, question_id):
    try :
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist :
        raise Http404("Does not exist.")
    return render(request, "polls/details.html", {"question" : question})


def results(request, question_id):
    response = "You are looking at the result of question %s."
    return HttpResponse(response % question_id)

def votes(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)