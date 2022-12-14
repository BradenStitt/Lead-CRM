from django.shortcuts import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganizerAndLoginRequiredMixin


# Create your views here.
class AgentListView(OrganizerAndLoginRequiredMixin, generic.ListView):
    template_name = 'agent_list.html'

    def get_queryset(self):
        org = self.request.user.userprofile
        return Agent.objects.filter(organization=org)
    
    
class AgentCreateView(OrganizerAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agent_create.html'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organization = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)
    

class AgentDetailView(OrganizerAndLoginRequiredMixin, generic.DetailView):
    template_name = "agent_detail.html"
    context_object_name = "agent"
    
    def get_queryset(self):
        org = self.request.user.userprofile
        return Agent.objects.filter(organization=org)
    

class AgentUpdateView(OrganizerAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agent_update.html'
    form_class = AgentModelForm
    
    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def get_queryset(self):
        org = self.request.user.userprofile
        return Agent.objects.filter(organization=org)
    
    

class AgentDeleteView(OrganizerAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agent_delete.html"
    context_object_name = "agent"
    
    def get_success_url(self):
        return reverse("agents:agent-list")
    
    def get_queryset(self):
        org = self.request.user.userprofile
        return Agent.objects.filter(organization=org)
    