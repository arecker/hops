from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView,
                                  View)
from django.shortcuts import (render,
                              render_to_response,
                              RequestContext)
from django.http import JsonResponse

from content.models import (HoppyUpdate,
                            Announcement,
                            Gallery,
                            NewspaperArchive,
                            Event,
                            Partner,
                            search)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        try:
            context['latest_hoppy'] = HoppyUpdate.objects.latest()
        except HoppyUpdate.DoesNotExist:
            context['latest_hoppy'] = None

        try:
            context['latest_announcement'] = Announcement.objects.latest()
        except Announcement.DoesNotExist:
            context['latest_announcement'] = None

        try:
            context['latest_gallery'] = Gallery.objects.latest()
        except Gallery.DoesNotExist:
            context['latest_gallery'] = None


        context['latest_events'] = Event.objects.upcoming()

        return context


class HoppyUpdateListView(ListView):
    model = HoppyUpdate
    template_name = 'hoppyupdate_list.html'
    paginate_by = 5


class HoppyUpdateDetailView(DetailView):
    model = HoppyUpdate
    template_name = 'hoppyupdate_detail.html'


class AnnouncementListView(ListView):
    model = Announcement
    template_name = 'announcement_list.html'
    paginate_by = 5


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcement_detail.html'


class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery_list.html'
    paginate_by = 5


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'gallery_detail.html'


class NewspaperArchiveListView(ListView):
    model = NewspaperArchive
    template_name = 'newspaper_list.html'
    paginate_by = 5


class SearchView(View):
    template_name = 'search.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        term = request.POST.get('term', None)

        if not term:
            return self.get(request)

        context = search(term)

        return render_to_response(self.template_name, RequestContext(request, context))


class GiveView(TemplateView):
    template_name = 'give.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super(GiveView, self).get_context_data(*args, **kwargs)
        ctx['partners'] = Partner.objects.credits()
        return ctx


class CalendarView(TemplateView):
    template_name = 'calendar.html'


class EventDetailView(DetailView):
    template_name = 'event_detail.html'
    model = Event


def events(request):
    qs = Event.objects.all()

    events = [{'id': e.id,
               'title': e.title,
               'url': e.get_absolute_url(),
               'start': e.start,
               'end': e.end} for e in qs]

    return JsonResponse(events, safe=False)
