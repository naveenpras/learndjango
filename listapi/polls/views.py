from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Poll

def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context = RequestContext(request, {'latest_poll_list' : latest_poll_list,})
#    output = ', '.join([p.question for p in latest_poll_list])
    return HttpResponse(template.render(context))
#    return HttpResponse(output)

def detail(request, poll_id):
    selected_poll = Poll.objects.get(id=poll_id)
    template = loader.get_template("polls/detail.html")
    context = RequestContext(request, {'selected_poll' : selected_poll,})
    return HttpResponse(template.render(context))
    
#    return HttpResponse("Ha HA You're looking at poll %s." % selected_poll.question)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
