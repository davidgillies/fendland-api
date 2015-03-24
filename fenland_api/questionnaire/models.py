# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from django.db import models


class Users(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    password_hash = models.TextField(blank=True)
    salt = models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        return self.user_id

    class Meta:
        db_table = 'users'


class Groups(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    study_name = models.CharField(max_length=50)
    user_group = models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        return "%s, %s" % (self.user_group, self.user_id)

    class Meta:
        db_table = 'groups'


class Progress(models.Model):
    user = models.ForeignKey(Users)
    questionnaire_id = models.CharField(max_length=50, blank=True)
    started = models.IntegerField(blank=True, null=True)
    finished = models.IntegerField(blank=True, null=True)
    progress_id = models.AutoField(primary_key=True)
    
    def __unicode__(self):
        return self.user.user_id

    class Meta:
        db_table = 'progress'


class Questionnaires(models.Model):
    id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=50)
    study_name = models.CharField(max_length=50)
    user_group = models.CharField(max_length=50)
    questionnaire_id = models.CharField(max_length=50)
    questionnaire_name = models.CharField(max_length=50)
    save_as = models.CharField(max_length=45)
    
    def __unicode__(self):
        return "%s, %s" % (self.questionnaire_id, self.study_name)

    class Meta:
        db_table = 'questionnaires'


class Results(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    user = models.ForeignKey(Users)
    questionnaire_id = models.CharField(max_length=45)
    var_id = models.CharField(max_length=45, blank=True)
    var_name = models.CharField(max_length=100)
    var_value = models.CharField(max_length=500, blank=True)
    
    def __unicode__(self):
        return self.user.user_id

    class Meta:
        db_table = 'results'


class Roles(models.Model):
    user_id = models.CharField(primary_key=True, max_length=50)
    role = models.CharField(max_length=50)
    
    def __unicode__(self):
        return "%s, %s" % (self.user_id, self.role)

    class Meta:
        db_table = 'roles'
