from django.shortcuts import render

def home(request):
    template_name = "home.html"
    context = {
        'title' : 'my home',
        'welcome' :'welcome my home',
    }
    return render(request, template_name, context)


def about(request):
    template_name = "about.html"
    context = {
        'title' : 'about me',
        'welcome' :'ini page about me',
    }
    return render(request, template_name, context)