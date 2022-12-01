import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

#from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import InquiryForm

#from .models import Plan
logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('maplan:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class MypageView(generic.TemplateView):
    template_name = "mypage.html"

class SitemapView(generic.TemplateView):
    template_name = "sitemap.html"

class PolicyView(generic.TemplateView):
    template_name = "policy.html"

class Change_passwordView(generic.TemplateView):
    template_name = "change_password.html"

class PersonalView(generic.TemplateView):
    template_name = "personal.html"

class Change_passwordkannryouView(generic.TemplateView):
    template_name = "change_passwordkannryou.html"

class WithdrawalView(generic.TemplateView):
    template_name = "withdrawal.html"

class PolicyView(generic.TemplateView):
    template_name = "policy.html"

class WithdrawalkView(generic.TemplateView):
    template_name = "withdrawalk.html"

class Change_personalView(generic.TemplateView):
    template_name = "change_personal.html"

class Change_personalkView(generic.TemplateView):
    template_name = "change_personalk.html"

class SearchboxView(generic.TemplateView):
    template_name = "searchbox.html"
