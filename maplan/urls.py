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
]
