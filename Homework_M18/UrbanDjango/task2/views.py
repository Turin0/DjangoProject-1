from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


def f_task2(request):
    return render(request, 'second_task/func_template.html')


class C_task2(TemplateView):
    template_name = 'second_task/class_template.html'
