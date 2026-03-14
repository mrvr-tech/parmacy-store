from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('', views.login_view, name='login'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # API endpoints (keep for mobile/external use)
    path('api/login/', views.login),
    path('api/items/', views.get_items),
    path('api/add-item/', views.add_item),
    path('api/lab-request/', views.create_request),
    path('api/approve-request/<int:request_id>/', views.approve_request),
    
    # Store Keeper Routes
    path('store/dashboard/', views.store_dashboard, name='store_dashboard'),
    path('store/reports/', views.store_reports, name='store_reports'),
    path('store/expiry-alerts/', views.expiry_alerts, name='expiry_alerts'),
    path('store/manage-inventory/', views.manage_inventory, name='manage_inventory'),
    path('store/add-item/', views.add_item_form, name='add_item_form'),
    path('store/approve-requests/', views.approve_lab_requests, name='approve_lab_requests'),
    path('store/approve-request/<int:request_id>/', views.approve_single_request, name='approve_single_request'),
    path('store/reject-request/<int:request_id>/', views.reject_single_request, name='reject_single_request'),
    
    # Lab User Routes
    path('lab/dashboard/', views.lab_dashboard, name='lab_dashboard'),
    path('lab/request-item/', views.lab_request_item, name='lab_request_item'),
    path('lab/request-history/', views.lab_request_history, name='lab_request_history'),
    
    # Report Exports - Store Keeper Only
    path('store/export/purchase-pdf/', views.export_purchase_report, name='export_purchase_pdf'),
    path('store/export/lab-usage-pdf/', views.export_lab_usage_report, name='export_lab_usage_pdf'),
    path('store/export/stock-pdf/', views.export_stock_report, name='export_stock_pdf'),
    path('store/export/purchase-excel/', views.export_purchase_report_excel, name='export_purchase_excel'),
    path('store/export/lab-usage-excel/', views.export_lab_usage_report_excel, name='export_lab_usage_excel'),
    path('store/export/stock-excel/', views.export_stock_report_excel, name='export_stock_excel'),
    
    # Legacy routes (for backward compatibility)
    path('dashboard/', views.dashboard, name='dashboard_legacy'),
    path('reports/', views.reports, name='reports_legacy'),
]
