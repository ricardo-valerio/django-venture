from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from .models import Question, Choice


def index(request):
    return render(request, "polls/index.html", {
        "latest_question_list": Question.objects.order_by('-pub_date')[:5]
    })


def detail(request, question_id):
    # There’s also a get_list_or_404() function
    return render(request, 'polls/detail.html', {
        'question': get_object_or_404(Question, pk=question_id)
    })


def results(request, question_id):
    return render(request, 'polls/results.html', {
        'question': get_object_or_404(Question, pk=question_id)
    })


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    try:
        #  request.POST values are always strings.
        #  Django also provides request.GET
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        # request.POST['choice'] will raise KeyError if choice wasn’t
        # provided in POST data.
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(
            reverse('polls:results', args=(question.id,)))
