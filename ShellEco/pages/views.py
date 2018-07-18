from django.shortcuts import render, render_to_response
from .models import Detail
from .forms import DetailForm
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf


def index(request):
    if request.POST:
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = DetailForm()
   
    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('pages/teamEcoTitans.html', args)


def about(request):
    return render(request, 'pages/teamEcoTitansAbout.html')


def team(request):
    return render(request, 'pages/teamEcoTitansTeam.html')


def efficiency(request):
    return render(request, 'pages/teamEcoTitansEfficiency.html')


def sponsors(request):
    return render(request, 'pages/teamEcoTitansSponsors.html')










