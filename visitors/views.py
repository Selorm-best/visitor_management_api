from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VisitorSerializer,VisitSerializer,DestinationSerializer
from .models import Visitor,Visit, Destination


@api_view(['GET'])
def getRoutes(request):
            routes =[
                {
            'Endpoint' :'/visitors/',
            'method' :'GET',
            'body' :'None',
            'description' : 'Returns list of all visitors'
            },

            {
            'Endpoint' :'/visitors/id',
            'method' :'GET',
            'body' :'None',
            'description' : 'Returns info of specific visitor'
             },

        {
            'Endpoint' :'/visitors/',
            'method' :'POST',
            'body' :'None',
            'description' : 'Adds a visitor''s details'
        },

        {
            'Endpoint' :'/visitors/id',
            'method' :'PATCH',
            'body' :'None',
            'description' : 'Modifies an detail of a specific visitor'
        },
    #Visits
        {
            'Endpoint' :'/visit/',
            'method' :'GET',
            'body' :'None',
            'description' : 'Returns info of all visits'
        },

        {
            'Endpoint' :'/visit/id',
            'method' :'GET',
            'body' :'None',
            'description' : 'Returns info of specific visit'
        },

            {
            'Endpoint' :'/visit/',
            'method' :'POST',
            'body' :'None',
            'description' : 'Adds visit details'
        },

        {
            'Endpoint' :'/visit/id',
            'method' :'PATCH',
            'body' :'None',
            'description' : 'Modifies a specific visit detail'
        },
        ]
            return Response(routes)

class VisitorView:

    #Lisiting all Visitors' Details
    @api_view(['GET'])
    def getVisitors(request):
        visitors = Visitor.objects.all()
        serializer = VisitorSerializer(visitors, many=True)
        return Response(serializer.data)
    
    #Lisiting Specific Visitor's Details
    @api_view(['GET'])
    def getVisitor(request, pk):
        visitor = Visitor.objects.get(id=pk)
        serializer = VisitorSerializer(visitor, many=False)
        return Response(serializer.data)

    @api_view(['POST'])
    def createVisitor(request):
          data = request.data
          visitor = Visitor.objects.create(name=data['name'],organization=data['organization'],contact_details=data['contact_details'], photo=data['photo'])

          serializer = VisitorSerializer(visitor, many=False)
          return Response(serializer.data)
 
    @api_view(['PATCH'])
    def updateVisitor(request, pk):
          data = request.data
          visitor = Visitor.objects.get(id=pk)

          serializer = VisitorSerializer(visitor, data=request.data, partial=True)
          if serializer.is_valid():
                serializer.save()
          return Response(serializer.data)

    @api_view(['DELETE'])

    def deleteVisitor(request,pk):
        visitor = Visitor.objects.get(id=pk)
        visitor.delete()

        return Response('Visitor was deleted!')

class VisitView:
    
    #Lisiting all Visits' Details
    @api_view(['GET'])
    def getVisits(request):
        visits = Visit.objects.all()
        serializer = VisitSerializer(visits, many=True)
        return Response(serializer.data)
    
    #Lisiting Specific Visit's Details
    @api_view(['GET'])
    def getVisit(request, pk):
        visit = Visit.objects.get(id=pk)
        serializer = VisitSerializer(visit, many=False)
        return Response(serializer.data)

    @api_view(['POST'])
    def createVisit(request):
          data = request.data
          visit = Visit.objects.create(purpose_of_visit=data['purpose_of_visit'],destination_id=data['destination'],visitor_id=data['visitor'])

          serializer = VisitSerializer(visit, many=False)
          return Response(serializer.data)
 
    @api_view(['PATCH'])
    def updateVisit(request, pk):
          data = request.data
          visit = Visit.objects.get(id=pk)

          serializer = VisitSerializer(visit, data=request.data, partial=True)
          if serializer.is_valid():
                serializer.save()
          return Response(serializer.data)

    @api_view(['DELETE'])

    def deleteVisit(request,pk):
        visit = Visit.objects.get(id=pk)
        visit.delete()

        return Response('Visit was deleted!')

class DestinationView:
    
    #Lisiting all Destinations
    @api_view(['GET'])
    def getDestinations(request):
        destination = Destination.objects.all()
        serializer = DestinationSerializer(destination, many=True)
        return Response(serializer.data)
    
    #Lisiting Specific Destination Details
    @api_view(['GET'])
    def getDestination(request, pk):
        destination = Destination.objects.get(id=pk)
        serializer = DestinationSerializer(destination, many=False)
        return Response(serializer.data)


    @api_view(['POST'])
    def createDestination(request):
          data = request.data
          destination = Destination.objects.create(name=data['name'], location=data['location'])
          serializer = DestinationSerializer(destination, many=False)
          return Response(serializer.data)
 
    @api_view(['PATCH'])
    def updateDestination(request, pk):
          data = request.data
          destination = Destination.objects.get(id=pk)

          serializer = DestinationSerializer(destination, data=request.data, partial=True)
          if serializer.is_valid():
                serializer.save()
          return Response(serializer.data)

    @api_view(['DELETE'])

    def deleteDestination(request,pk):
        destination = Destination.objects.get(id=pk)
        destination.delete()
        return Response('Destination was deleted!')


