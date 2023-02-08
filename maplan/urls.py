from django.urls import path

from.import views

app_name = 'maplan'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('inquiry/', views.InquiryView.as_view(),name="inquiry"),
    path('sitemap/', views.SitemapView.as_view(),name="sitemap"),
    path('policy/', views.PolicyView.as_view(),name="policy"),
    path('change_password/', views.Change_passwordView.as_view(),name="change_password"),
    path('mypage/', views.MypageView.as_view(), name="mypage"),
    path('personal/', views.PersonalView.as_view(), name="personal"),
    path('change_passwordkannryou/', views.Change_passwordkannryouView.as_view(),name="change_passwordkannryou"),
    path('withdrawal/', views.WithdrawalView.as_view(), name="withdrawal"),
    path('withdrawalk/', views.WithdrawalkView.as_view(), name="withdrawalk"),
    path('change_personal/', views.Change_personalView.as_view(), name="change_personal"),
    path('change_personalk/', views.Change_personalkView.as_view(), name="change_personalk"),
    path('searchbox/', views.SearchboxView.as_view(), name="searchbox"),
    path('mypage/history/', views.HistoryView.as_view(), name="history"),
    path('mypage/favorite/', views.FavoriteView.as_view(), name="favorite"),
    path('created1/', views.CreatedOneView.as_view(), name="created_one"),
    path('created2/', views.CreatedTwoView.as_view(), name="created_two"),
    path('error/', views.ErrorView.as_view(), name="error"),
    path('plan/', views.PlanView.as_view(), name="plan"),
    path('plan_detail/<int:pk>/', views.PlandetailView.as_view(), name="plan_detail"),
    path('plan_create_complete/', views.plan_create_completeView.as_view(), name="plan_create_complete"),
    path('mypage_favorite/', views.mypage_favoriteView.as_view(), name="mypage_favorite"),
    path('mypage_history/', views.mypage_historyView.as_view(), name="mypage_history"),
    path('mypage_eturan/', views.mypage_eturanView.as_view(), name="mypage_eturan"),
    path('mypage_sakusei/', views.mypage_sakuseiView.as_view(), name="mypage_sakusei"),
    path('mypage_komennto/', views.mypage_komenntoView.as_view(), name="mypage_komennto"),
    path('detail_test/', views.DetailTestView.as_view(), name="detail_test"),
    path('detail_result/<int:pk>/', views.DetailResultView.as_view(), name="detail_result"),
    path('plan_test/', views.plan_testView.as_view(), name="plan_test"),

]
