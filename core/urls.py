from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('checkout/', views.checkout, name='checkout'),
    path('payment-successful/', views.payment_successful, name='payment_successful'),
    path('payment-cancelled/', views.payment_cancelled, name='payment_cancelled'),
    path('webhook/stripe/', views.webhook, name='stripe_webhook'),
    path('download/', views.download_page, name='download_page'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path("robots.txt", views.robots_txt),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml')
]