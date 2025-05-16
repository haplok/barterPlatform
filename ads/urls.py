from django.urls import path
from . import views

urlpatterns = [
    path('', views.ad_list, name='ad_list'),
    path('ads/create/', views.ad_create, name='ad_create'),
    path('ads/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('ads/<int:ad_id>/edit/', views.ad_update, name='ad_update'),
    path('ads/<int:ad_id>/delete/', views.ad_delete, name='ad_delete'),
    path('ad/<int:ad_id>/propose/', views.propose_exchange, name='propose_exchange'),
    path('exchange/proposals/', views.exchange_proposals, name='exchange_proposals'),
    path('exchange/proposal/<int:proposal_id>/', views.proposal_detail, name='proposal_detail'),
]
