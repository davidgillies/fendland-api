from django.db import models


class Surgery(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    full_name = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    addr1 = models.CharField(max_length=50, blank=True)
    addr2 = models.CharField(max_length=50, blank=True)
    town = models.CharField(max_length=50, blank=True)
    county = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=50, blank=True)
    telephone = models.CharField(max_length=12, blank=True)
    admin_contact_name = models.CharField(max_length=50, blank=True)
    admin_contact_number = models.CharField(max_length=50, blank=True)
    hscic_code = models.CharField(max_length=45, blank=True)
    area = models.CharField(max_length=50, blank=True)
    modified_by = models.CharField(db_column='modified by', max_length=50, blank=True)  # Field renamed to remove unsuitable characters.
    modified = models.DateTimeField(blank=True, null=True)
    surgeriescol = models.CharField(max_length=45, blank=True)

    class Meta:
        db_table = 'surgeries'


class Volunteer(models.Model):
    volunteer_id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=50, blank=True)
    forenames = models.CharField(max_length=50, blank=True)
    initials = models.CharField(max_length=10, blank=True)
    dob = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=10, blank=True)
    sex = models.CharField(max_length=1, blank=True)
    addr1 = models.CharField(max_length=50, blank=True)
    addr2 = models.CharField(max_length=50, blank=True)
    town = models.CharField(max_length=50, blank=True)
    county = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=50, blank=True)
    home_tel = models.CharField(max_length=50, blank=True)
    work_tel = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    nhs_no = models.CharField(max_length=10, blank=True)
    surgery_id = models.IntegerField(blank=True, null=True)
    gp_id = models.IntegerField(blank=True, null=True)
    moved_away = models.IntegerField(blank=True, null=True)
    diabetes_diagnosed = models.IntegerField(blank=True, null=True)
    modified_by = models.CharField(max_length=50, blank=True)
    curr_status = models.IntegerField(blank=True, null=True)
    reason = models.IntegerField(blank=True, null=True)
    phase1_comment = models.TextField(blank=True)
    phase2_comment = models.TextField(blank=True)
    volunteerscol = models.CharField(max_length=45, blank=True)
    modified = models.DateTimeField(blank=True, null=True)
    surgeries = models.ForeignKey(Surgery)

    class Meta:
        db_table = 'volunteers'


class Appointment(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    repeat = models.IntegerField(blank=True, null=True)
    studyphase = models.IntegerField(blank=True, null=True)
    appt_date = models.DateField(blank=True, null=True)
    appt_time = models.TimeField(blank=True, null=True)
    test_site = models.CharField(max_length=10, blank=True)
    modified_by = models.CharField(max_length=45, blank=True)
    modified = models.DateTimeField(blank=True, null=True)
    volunteer = models.ForeignKey(Volunteer)

    class Meta:
        db_table = 'appointments'


class AuditLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    reason = models.TextField(blank=True)
    edit_date = models.DateField(blank=True, null=True)
    editor = models.CharField(max_length=50, blank=True)

    class Meta:
        db_table = 'audit_log'


class Status(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    curr_status = models.CharField(max_length=45, blank=True)

    class Meta:
        db_table = 'status'
