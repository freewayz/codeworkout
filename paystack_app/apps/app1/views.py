from django.shortcuts import render

# Create your views here.


def index_page(request):
    return render(request, template_name='app1/_base.html', context={})