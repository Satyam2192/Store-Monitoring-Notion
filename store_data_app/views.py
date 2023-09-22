from rest_framework import viewsets
from .models import StoreStatus, BusinessHours, Timezones
from .serializers import StoreStatusSerializer, BusinessHoursSerializer, TimezonesSerializer
from datetime import timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from random import choices
import string
from django.http import HttpResponse

class StoreStatusViewSet(viewsets.ModelViewSet):
    queryset = StoreStatus.objects.all()
    serializer_class = StoreStatusSerializer

class BusinessHoursViewSet(viewsets.ModelViewSet):
    queryset = BusinessHours.objects.all()
    serializer_class = BusinessHoursSerializer

class TimezonesViewSet(viewsets.ModelViewSet):
    queryset = Timezones.objects.all()
    serializer_class = TimezonesSerializer

# 
def calculate_uptime_downtime(store_status):
    # Calculate uptime and downtime based on business hours
    business_hours = BusinessHours.objects.filter(store_id=store_status.first().store_id)
    start_time = min(business_hours, key=lambda x: x.start_time_local).start_time_local
    end_time = max(business_hours, key=lambda x: x.end_time_local).end_time_local


    uptime_last_hour = 0
    downtime_last_hour = 0
    uptime_last_day = 0
    downtime_last_day = 0
    uptime_last_week = 0
    downtime_last_week = 0

    # Iterate over the store status records
    for status in store_status:
        timestamp = status.timestamp_utc
        status_duration = timedelta(minutes=1)  # each status record is for 1 minute

        # Check if the timestamp is within business hours
        if start_time <= timestamp.time() <= end_time:
            # Check if the status is "online"
            if status.status == "online":
                uptime_last_hour += status_duration.total_seconds() / 60
                uptime_last_day += status_duration.total_seconds() / 3600
                uptime_last_week += status_duration.total_seconds() / 3600
            else:
                downtime_last_hour += status_duration.total_seconds() / 60
                downtime_last_day += status_duration.total_seconds() / 3600
                downtime_last_week += status_duration.total_seconds() / 3600

    # Update the store status record with the calculated uptime and downtime
    store_status.uptime_last_hour = int(uptime_last_hour)
    store_status.downtime_last_hour = int(downtime_last_hour)
    store_status.uptime_last_day = int(uptime_last_day)
    store_status.downtime_last_day = int(downtime_last_day)
    store_status.uptime_last_week = int(uptime_last_week)
    store_status.downtime_last_week = int(downtime_last_week)
    store_status.save()


@api_view(['POST'])
def trigger_report(request):
    # Get the latest timestamp among all store status records
    latest_timestamp = StoreStatus.objects.latest('timestamp_utc').timestamp_utc

    # Update the uptime and downtime fields for all store status records
    store_ids = StoreStatus.objects.values_list('store_id', flat=True).distinct()
    for store_id in store_ids:
        store_status = StoreStatus.objects.filter(store_id=store_id)
        calculate_uptime_downtime(store_status)

    # Generate a random report ID
    report_id = ''.join(choices(string.ascii_uppercase + string.digits, k=10))

    # Return the report ID
    return Response({'report_id': report_id})

@api_view(['GET'])
def get_report(request, report_id):
               
        try:
            # checking if the report generation is complete or not
            report = StoreStatus.objects.get(report_id=report_id)
            if report.uptime_last_hour is None or report.downtime_last_hour is None:
                return Response({'status': 'Running'})

            # generate the CSV file
            csv_data = 'store_id,uptime_last_hour,uptime_last_day,uptime_last_week,downtime_last_hour,downtime_last_day,downtime_last_week\n'
            store_status = StoreStatus.objects.all()
            for status in store_status:
                csv_data += f'{status.store_id},{status.uptime_last_hour},{status.uptime_last_day},{status.uptime_last_week},{status.downtime_last_hour},{status.downtime_last_day},{status.downtime_last_week}\n'

            # return the CSV file
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="report.csv"'
            response.write(csv_data)
            return response
        except StoreStatus.DoesNotExist:
            return Response({'status': 'Invalid report ID'})

@api_view(['GET'])
def get_reports(request):
    try:
        # Check if the report generation is complete
        store_status = StoreStatus.objects.all()
        # if any(status.uptime_last_hour is None or status.downtime_last_hour is None for status in store_status):
        #     return Response({'status': 'Running'})

        # Generate the CSV file
        csv_data = 'store_id,uptime_last_hour,uptime_last_day,uptime_last_week,downtime_last_hour,downtime_last_day,downtime_last_week\n'
        for status in store_status:
            csv_data += f'{status.store_id},{status.uptime_last_hour},{status.uptime_last_day},{status.uptime_last_week},{status.downtime_last_hour},{status.downtime_last_day},{status.downtime_last_week}\n'

        # Return the CSV file
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="report.csv"'
        response.write(csv_data)
        return response
    except Exception as e:
        return Response({'status': 'Error', 'message': str(e)})
