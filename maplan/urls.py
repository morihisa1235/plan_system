from django.urls import path

from.import views

app_name = 'maplan'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('inquiry/', views.InquiryView.as_view(),name="inquiry"),
    path('sitemap/', views.SitemapView.as_view(),name="sitemap"),
    path('policy/', views.PolicyView.as_view(),name="policy"),
    path('mypage/', views.MypageView.as_view(), name="mypage"),
    path('personal/', views.PersonalView.as_view(), name="personal"),
]
