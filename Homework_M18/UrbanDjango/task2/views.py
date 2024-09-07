from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def f_task2(request):
    return render(request, 'func_template.html')


class C_task2(TemplateView):
    template_name = 'class_template.html'
