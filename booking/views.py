from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import FitnessClass, Booking
from .serializers import FitnessClassSerializer, BookingSerializer
from django.db import transaction

@api_view(['GET'])
def get_classes(request):
    classes = FitnessClass.objects.all().order_by('date_time')
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def book_class(request):
    class_id = request.data.get('class_id')
    name = request.data.get('client_name')
    email = request.data.get('client_email')

    if not all([class_id, name, email]):
        return Response({'error': 'class_id, client_name, and client_email are required'},
                        status=status.HTTP_400_BAD_REQUEST)

    try:
        with transaction.atomic():
            fitness_class = FitnessClass.objects.select_for_update().get(id=class_id)

            if fitness_class.available_slots <= 0:
                return Response({'error': 'No available slots'}, status=status.HTTP_400_BAD_REQUEST)

            # Create booking and decrement slot
            Booking.objects.create(
                fitness_class=fitness_class,
                client_name=name,
                client_email=email
            )

            fitness_class.available_slots -= 1
            fitness_class.save()

    except FitnessClass.DoesNotExist:
        return Response({'error': 'Class not found'}, status=status.HTTP_404_NOT_FOUND)

    return Response({'message': 'Booking successful'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_bookings(request):
    email = request.query_params.get('email')
    if not email:
        return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

    bookings = Booking.objects.filter(client_email=email)
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)
