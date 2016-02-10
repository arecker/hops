from django.views.generic import TemplateView

from planning.models import HoppyUpdate, Announcement


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView,self).get_context_data(**kwargs)

        context['latest_hoppy'] = HoppyUpdate.objects.latest()
        context['latest_announcement'] = Announcement.objects.latest()

        return context
