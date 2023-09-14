from django.shortcuts import render
from . import models
from django.http import Http404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import NotesForm
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

# Create your views here.
class NotesDeleteView(DeleteView):
    model = models.Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = models.Notes
    # fields = ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = models.Notes
    # fields = ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm
    login_url = '/admin'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesView(LoginRequiredMixin, ListView):
    template_name = 'notes/notes.html'
    model = models.Notes
    context_object_name = 'notes'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

class DetailNoteView(DetailView):
    context_object_name = 'note'
    model = models.Notes


# def list(request):
#     all_notes = models.Notes.objects.all()
#     return render(request, 'notes/notes.html', {'notes': all_notes})

# def detail(request, pk):
#     try:
#         detail_note = models.Notes.objects.get(pk=pk)
#     except models.Notes.DoesNotExist:
#         raise Http404("Note doesn't exist.")
#     return render(request, 'notes/detail_note.html', {'detail_note': detail_note})