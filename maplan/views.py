import logging

from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import InquiryForm

from .models import Plan, Route, Comment
from .models import Prefecture, Tourism, Category
from accounts.models import CustomUser


logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = "index.html"
    models = Plan
    context_object_data = "plan_list"

    def get_queryset(self):
        plans = Plan.objects.filter().order_by('?')
        return plans

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('maplan:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class MypageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "mypage.html"

class SitemapView(generic.TemplateView):
    template_name = "sitemap.html"

class PolicyView(generic.TemplateView):
    template_name = "policy.html"

class Change_passwordView(LoginRequiredMixin,generic.TemplateView):
    template_name = "change_password.html"

class PersonalView(LoginRequiredMixin,generic.ListView):
    template_name = "personal.html"
    model = CustomUser
    def get_queryset(self):
        user = CustomUser.objects.filter().order_by('id')
        return user

class Change_personalView(LoginRequiredMixin,generic.ListView):
    template_name = "change_personal.html"
    model = CustomUser
    def get_queryset(self):
        user = CustomUser.objects.filter().order_by('id')
        return user

class Change_passwordkannryouView(LoginRequiredMixin, generic.TemplateView):
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

class SearchboxView(generic.ListView):
    template_name = "searchbox.html"
    model = Plan
    context_object_data = 'category_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SearchboxView, self).get_context_data(**kwargs)
        context.update({
            'category_list': Category.objects.filter().order_by('category_code'),
        })
        return context

    def get_queryset(self):
        plans = Plan.objects.filter().order_by('?')
        return plans

class HistoryView(LoginRequiredMixin, generic.ListView):
    model = Plan
    template_name ='mypage_history.html'

    def get_queryset(self):
        plans = Plan.objects.filter(user=self.request.user).order_by('-created_at')
        return plans

class FavoriteView(LoginRequiredMixin, generic.ListView):
    model = Plan
    template_name ='mypage_favorite.html'

    def get_queryset(self):
        plans = Plan.objects.filter(user=self.request.user).order_by('-created_at')
        return plans

class CreatedOneView(generic.ListView):
    model = Prefecture
    template_name = 'plan_create1.html'
    context_object_data = 'prefecture_list'

    def get_context_data(self, **kwargs):
        context = super(CreatedOneView, self).get_context_data(**kwargs)
        context.update({
            'tourism_list': Tourism.objects.filter().order_by('tourism_code'),
            'category_list': Category.objects.filter().order_by('category_code'),
        })
        return context

    def get_queryset(self):
        prefectures = Prefecture.objects.filter().order_by('prefecture_code')
        return prefectures

class CreatedTwoView(generic.ListView):
    model = Category
    template_name = 'plan_create2.html'

    def get_queryset(self):
        categories = Category.objects.filter().order_by('category_code')
        return categories

class ErrorView(generic.TemplateView):
    template_name = "error.html"

class PlanView(generic.TemplateView):
    template_name = "plan.html"
    models = Tourism

    def get_queryset(self):
        plans = Tourism.objects.filter().order_by('?')
        return plans

class PlandetailView(generic.DetailView):
    template_name = "plan_detail.html"
    models = Plan
    context_object_data = "plan_list"

    def get_context_data(self, **kwargs):
        context = super(PlandetailView, self).get_context_data(**kwargs)
        context.update({
            'route_list' : Route.objects.filter().order_by('id'),
            'comment_list' : Comment.objects.filter().order_by('id')
        })
        return context

    def get_queryset(self):
        plans = Plan.objects.filter().order_by('id')
        return plans

class Plan_create2View(generic.ListView):
     template_name = "plan_create2.html"

class plan_create_completeView(generic.TemplateView):
    template_name = "plan_create_complete.html"

class mypage_favoriteView(generic.TemplateView):
    template_name = "mypage_favorite.html"

class mypage_historyView(generic.TemplateView):
    template_name = "mypage_history.html"

class mypage_eturanView(generic.TemplateView):
    template_name = "mypage_eturan.html"

class mypage_sakuseiView(generic.TemplateView):
    template_name = "mypage_sakusei.html"

class mypage_komenntoView(generic.TemplateView):
    template_name = "mypage_komennto.html"

class DetailTestView(generic.ListView):
    template_name = "detail_test.html"
    models = Plan

    def get_queryset(self):
        Plans = Plan.objects.filter().order_by('?')
        return Plans

class DetailResultView(generic.DetailView):
    template_name = "detail_result.html"
    models = Plan

    def get_queryset(self):
        Plans = Plan.objects.filter().order_by('?')
        return Plans

class planView(generic.TemplateView):
    template_name = "plan.html"

class plan_testView(generic.TemplateView):
    template_name = "plan_test.html"

