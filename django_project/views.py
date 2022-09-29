from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    # template = loader.get_template('templates/chessboard.html')
    # return HttpResponse(template.render())
    # return HttpResponse("<h1>hello</h1>")
    return render(request, 'templates/chessboard.html')
