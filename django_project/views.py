from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render


def index(request):
    # template = loader.get_template('templates/chessboard.html')
    # return HttpResponse(template.render())
    # return HttpResponse("<h1>hello</h1>")
    return render(request, 'templates/chessboard.html', {'color': 'grey'})


def changeMoves(request, table):
    print("working change")
    data = {
        'body': table,
        'color': 'red',
    }
    return render(request, 'templates/chessboard.html', data)

def updateMoves(request):
    print("updating")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])