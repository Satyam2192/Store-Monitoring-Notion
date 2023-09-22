from django.db import models

# class StoreStatus(models.Model):
#     store_id = models.BigIntegerField()
#     timestamp_utc = models.DateTimeField()
#     status = models.CharField(max_length=10)
class StoreStatus(models.Model):
    store_id = models.BigIntegerField()
    timestamp_utc = models.DateTimeField()
    status = models.CharField(max_length=10)
    uptime_last_hour = models.IntegerField(null=True)
    uptime_last_day = models.IntegerField(null=True)
    uptime_last_week = models.IntegerField(null=True)
    downtime_last_hour = models.IntegerField(null=True)
    downtime_last_day = models.IntegerField(null=True)
    downtime_last_week = models.IntegerField(null=True)


class BusinessHours(models.Model):
    store_id = models.BigIntegerField()
    day = models.IntegerField()
    start_time_local = models.TimeField()
    end_time_local = models.TimeField()

class Timezones(models.Model):
    store_id = models.BigIntegerField()
    timezone_str = models.CharField(max_length=50)


