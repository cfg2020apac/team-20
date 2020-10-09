from django.utils import timezone
from django.conf import settings
from django.db import models


class handson_program(models.Model):
    occur_id = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    hours_program_total = models.DecimalField(max_digits=30, decimal_places=15)
    pop_served_list = models.CharField(max_length=100)
    impact_area = models.CharField(max_length=100)
    impact_outcome = models.DecimalField(max_digits=30, decimal_places=15)
    opportunity_name = models.CharField(max_length=100)
    schedule_type = models.CharField(max_length=100)
    reg_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date_time = models.CharField(max_length=100)
    end_date_time = models.CharField(max_length=100)
    opportunity_coordinator = models.CharField(max_length=100)
    opportunity_coordinator_email = models.CharField(max_length=100)
    vol_leader_need = models.IntegerField()
    max_attend = models.IntegerField()
    min_attend = models.IntegerField()
    vol_confirmed = models.IntegerField()
    vol_in_need = models.IntegerField()
    num_attend = models.IntegerField()
    num_not_attend = models.IntegerField()
    hours_occur_total = models.DecimalField(max_digits=30, decimal_places=15)
    opportunity_record_id = models.CharField(max_length=100)


class volunteer_profile(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Interests = models.CharField(max_length=300)
    Gender = models.CharField(max_length=10)
    Employment_Status = models.CharField(max_length=20)
    Mobile_phone = models.CharField(max_length=20)
    Connection_Id = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Attendance_Status = models.CharField(max_length=30)
    Hours_Served = models.DecimalField(max_digits=30, decimal_places=15)
    Hours_Served_since_account_was_created = models.DecimalField(max_digits=30, decimal_places=15)
    Volunteer_Opportunity_Name = models.CharField(max_length=100)
    Organization_Name = models.CharField(max_length=30)
    Type = models.CharField(max_length=30)
    Employer = models.CharField(max_length=30)
    Contact_ID = models.CharField(max_length=30)