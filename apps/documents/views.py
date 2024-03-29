from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy

from .forms import DocumentForm
from .models import Document

class HomePageView(ListView):
    model = Document
    template_name = "home.html"

class CreateDocumentView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = "document.html"
    success_url = reverse_lazy("result")

class ResultDocumentView(CreateView):
    model = Document
    template_name = "result.html"