from django.shortcuts import render
from django.shortcuts import get_list_or_404
from .models import *

class InfoMixin():
    Model = None
    Template = None

    def get(self, request):
        title = self.Model.__name__.lower()+"s"
        object = get_list_or_404(self.Model)
        return render(request, self.Template, context={title: object})