from django.shortcuts import render

from . import util
# data=[{
title="CSS"
# "description":"CSS is a language that can be used to add style to an [HTML](/wiki/HTML) page."
# }]

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def new(request):
    return render(request, "encyclopedia/new.html")

def random(request):
    return render(request, "encyclopedia/random.html")

def wikititle(request):
    return render(request, "encyclopedia/title.html",{
        "title":title,
        "description":markdown2.markdown(util.get_entry(title))
    })
