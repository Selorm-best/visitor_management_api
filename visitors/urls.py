from django.urls import path

from . import views

#Endpoints to the Visit, Visitors and Destination REST API CRU operation are here
urlpatterns =[
path('vistors/',views.VistorListCreateView.as_view(), name ='visitor-list-create'),
path('visits',views.VisitListCreateView.as_view(), name='visit-list-create'),
path('destinations', views.DestinationListCreateView.as_view(), name ='destination-list-create')

]