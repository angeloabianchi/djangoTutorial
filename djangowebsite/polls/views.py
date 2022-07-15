from django.http import Http404                                                 # 3.4
from django.shortcuts import render, get_object_or_404                          # 3.3 if use this, we can delete the import loader. get_object_or_404 implemented at 3.5
from django.urls import reverse                                                 # 4.1
from django.views import generic                                                # 4.3.1.
from django.utils import timezone                                               # 5.2.7

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect                      # 3.2.1 - added the HttpResponseRedirect in 4.1.1
# from django.template import loader                                            # 3.2.2

from .models import Question, Choice                                            # 3.2.2

# def index(request):                                                           # updated to 4.3.1
    # return HttpResponse("Hello, world. You're at the polls index.")           # Added sometime in Part 1 of the tutorial and has been updated at 3.2.1
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]         # 3.2.1 - updated to 4.3.1
    # output = ', '.join([q.question_text for q in latest_question_list])       # 3.2.1 - Updated at 3.2.2 as you can see below
    # template = loader.get_template('polls/index.html')                        # 3.2.2 - updated at 3.3
    # context = {                                                               # 3.2.2 - updated to 4.3.1
    #     'latest_question_list': latest_question_list,                         # updated to 4.3.1
    # }                                                                         # updated to 4.3.1
    # return HttpResponse(output)                                               # 3.2.1
    # return HttpResponse(template.render(context, request))                    # 3.2.2 - updated at 3.3
    # return render(request, 'polls/index.html', context)                       # updated to 4.3.1

class IndexView(generic.ListView):                                              # 4.3.1 inicio
    template_name = 'polls/index.html'                                          
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        # return Question.objects.order_by('-pub_date')[:5]                     # 4.3.1 fim. - updated to 5.2.7
        return Question.objects.filter(                                         # 5.2.7 inicio
            pub_date__lte=timezone.now()                        
        ).order_by('-pub_date')[:5]                                             # 5.2.7 fim
        # Question.objects.filter(pub_date__lte=timezone.now()) returns 
        # a queryset containing Questions whose pub_date is less than 
        # or equal to - that is, earlier than or equal to - timezone.now.



# def detail(request, question_id):                                             # 3.1 - updated to 4.3.1
    # try:                                                                      # 3.4 - updated at 3.5
    #    question = Question.objects.get(pk=question_id)                        # 3.4 - updated at 3.5
    # except Question.DoesNotExist:                                             # 3.4 - updated at 3.5
    #    raise Http404("Question does not exist")                               # 3.4 - updated at 3.5
    # return HttpResponse("You're looking at question %s." % question_id)       # 3.1 - updated at 3.4
    # return render(request, 'polls/detail.html', {'question': question})       # 3.4 - updated at 3.5

    # question = get_object_or_404(Question, pk=question_id)                    # 3.5 - updated to 4.3.1
    # return render(request, 'polls/detail.html', {'question': question})       # 3.5 - updated to 4.3.1

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):                                                     # 5.2.9 inicio
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())            # 5.2.9 fim

# def results(request, question_id):                                            # 3.1 - updated to 4.3.1
    # response = "You're looking at the results of question %s."                # 3.1 - updated to 4.1.2
    # return HttpResponse(response % question_id)                               # 3.1 - updated to 4.1.2
    # question = get_object_or_404(Question, pk=question_id)                    # 4.1.2 - updated to 4.3.1
    # return render(request, 'polls/results.html', {'question': question})      # 4.1.2 - updated to 4.3.1

class ResultsView(generic.DetailView):                                          # 4.3.1 inicio
    model = Question
    template_name = 'polls/results.html'                                        # 4.3.1 fim

def vote(request, question_id):                                                 # 3.1
    # return HttpResponse("You're voting on question %s." % question_id)        # 3.1 - Updated to 4.1
    question = get_object_or_404(Question, pk=question_id)                      # 4.1 starts here
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])    # request.POST is a dictionary-like object that lets you access submitted data by key name. In this case, request.POST['choice'] returns the ID of the selected choice, as a string. request.POST values are always strings.
    except (KeyError, Choice.DoesNotExist):                                     # request.POST['choice'] will raise KeyError if choice wasn’t provided in POST data.
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
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  # 4.1 finishes here. After incrementing the choice count, 
                                                                                    # the code returns an HttpResponseRedirect rather than a normal HttpResponse. 
                                                                                    # HttpResponseRedirect takes a single argument: the URL
        # We are using the reverse() function in the HttpResponseRedirect constructor 
        # in this example. This function helps avoid having to hardcode a URL in the 
        # view function.