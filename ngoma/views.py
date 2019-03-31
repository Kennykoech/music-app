from django.shortcuts import render
from ngoma.models import Song
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy, reverse
# from .filters import SongFilter
# user views
def contact(request):
    return render(request, "ngoma/contact.html")

class IndexView(generic.ListView):
    template_name = 'ngoma/index.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.all()
   

# kenny_admin views
class KennyIndexView(generic.ListView):
    template_name = 'ngoma/control_panel.html'
    context_object_name = 'all_songs'

    def get_queryset(self):
        return Song.objects.all()
   
    

class DetailView(generic.DetailView):
    model = Song
    template_name = 'ngoma/detail.html'


#song creation
class Songcreate(CreateView):
    model = Song
    fields = ['artist', 'genre', 'song_logo', 'song_title', 'song']

class Songupdate(UpdateView):
    model = Song
    fields = ['artist', 'genre', 'song_logo', 'song_title', 'song']

class Songdelete(DeleteView):
    model = Song
    success_url = reverse_lazy('ngoma:kenny_index') 


# class SongListView(DetailView):
#     model = Song
#     template_name = 'ngoma/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(self, **kwargs)
#         context['filter'] = SongFilter(self.request.GET, queryset=self.get_queryset())
#         return context

