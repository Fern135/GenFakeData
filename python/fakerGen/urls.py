from django.urls import path, include

from . import views

# api/

urlpatterns = [
    path('users/', views.genUsers, name="gen_users"),
    path('products/', views.genProducts, name="gen_products"),
    path('companies/', views.genCompanies, name="gen_companies"),
    path('credit-cards/', views.genCreditCards, name="gen_cc"),
    path('jobs/', views.genJobs, name="gen_jobs"),
    path('text-contents/', views.genText, name="gen_text"),

    path('users/<int:count>/', views.genUsers, name="gen_users_count"),
    path('products/<int:count>/', views.genProducts, name="gen_products_count"),
    path('companies/<int:count>/', views.genCompanies, name="gen_companies_count"),
    path('credit-cards/<int:count>/', views.genCreditCards, name="gen_cc_count"),
    path('jobs/<int:count>/', views.genJobs, name="gen_jobs_count"),
    path('text-contents/<int:count>/', views.genText, name="gen_text_count"),
]
