from django.urls import path, include

from . import views

urlpatterns =[
    path('', views.getRoutes),
    path('visitors/', views.VisitorView.getVisitors, name='visitors-retrieve'),
    path('visitors/create/', views.VisitorView.createVisitor, name='visitor-create'),
    path('visitors/<int:pk>/update/', views.VisitorView.updateVisitor, name='visitor-update'),
    path('visitors/<int:pk>/', views.VisitorView.getVisitor, name='visitor-retrieve'),
    path('visitors/<int:pk>/delete/', views.VisitorView.deleteVisitor, name='visitor-delete'),


    path('visits/', views.VisitView.getVisits, name='visits-retrieve'),
    path('visits/create/', views.VisitView.createVisit, name='visit-create'),
    path('visits/<int:pk>/update/', views.VisitView.updateVisit, name='visit-update'),
    path('visits/<int:pk>/', views.VisitView.getVisit, name='visit-retrieve'),
    path('visits/<int:pk>/delete/', views.VisitView.deleteVisit, name='visit-delete')



]