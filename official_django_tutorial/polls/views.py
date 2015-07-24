from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
# from django.template import RequestContext, loader
# from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Question

"""
Each view is responsible for doing one of two things:
	1- returning an HttpResponse object containing the content for the requested page,
	2- or raising an exception such as Http404.

The rest is up to you.

Your view can read records from a database, or not.
It can use a template system such as Django’s
– or a third-party Python template system – or not.
It can generate a PDF file, output XML, create a ZIP file on the fly,
anything you want, using whatever Python libraries you want.

All Django wants is that HttpResponse. Or an exception.
"""

# to avoid design logic in this methods it's better to create
# a "templates" folder and django will auto lookup for equal names
#
# Your project’s TEMPLATES setting describes how Django will load and
# render templates. The default settings file configures a DjangoTemplates backend
# whose APP_DIRS option is set to True. By convention DjangoTemplates looks for a
# “templates” subdirectory in each of the INSTALLED_APPS. This is how Django knows to
# find the polls templates even though we didn’t modify the DIRS option, as we did in
# Tutorial 2.
#
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)
	# latest_question_list = Question.objects.order_by('-pub_date')[:5]
	# template = loader.get_template('polls/index.html')
	# context = RequestContext(request, {
	#     'latest_question_list': latest_question_list,
	# })
	# return HttpResponse(template.render(context))

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/detail.html', {'question': question})
	"""
	There’s also a get_list_or_404() function, which works just as get_object_or_404()
	– except using filter() instead of get(). It raises Http404 if the list is empty.
	"""
	# 2
	# try:
	#     question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	#     raise Http404("Question does not exist")
	# return render(request, 'polls/detail.html', {'question': question})

	# 1
    # return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
