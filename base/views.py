from django.shortcuts import render
from base.tasks import visit

def index(request):
    visit.delay()
    return render(request, 'base/index.html', {})
