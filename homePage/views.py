from django.shortcuts import render


def home(request):
    
    context = {
        'title': 'HomePage'
    }

    return render(
        request,
        template_name='homepage.html',
        context=context,
        )