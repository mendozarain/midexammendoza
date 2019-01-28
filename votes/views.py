from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate,Position,Vote
from .forms import CandidateModelForm,AskForm, AskForm2


# Create your views here.
def index(request):
    context = {}
    candidates= Candidate.objects.all()
    context['candidates'] = candidates
    return render(request, 'index.html', context)


def detail(request, candidate_id):
    context = {}
    context['candidate'] =  Candidate.objects.get(id=candidate_id)
    return render(request, 'detail.html',context)


def create(request):
    context = {}
    form = AskForm()

    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')

    return render(request, 'candidate_create.html',{'form' :form})


def create_pos(request):
    context = {}
    form = AskForm2()

    if request.method == 'POST':
        form = AskForm2(request.POST)
        if form.is_valid():
            form.save()
            return redirect('votes:index')

    return render(request, 'position_create.html',{'form' :form})
