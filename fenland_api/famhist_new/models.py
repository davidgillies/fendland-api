from django.db import models


class FamHistQuestionnaire(models.Model):
    sibling_choices = (
        (1, 'Sister'),
        (2, 'Brother'),
    )
    
    age_choices = (
        (1, '>10'),
        (2, '10-19'),
        (3, '20-29'),
        (4, '30-39'),
        (5, '40-49'),
        (6, '50-59'),
        (7, '60-69'),
        (8, '70+'),
        (9, 'Not known'),    
    )
    
    FH03_BrotherTotal = models.IntegerField(blank=True, null=True)
    FH02_SisterTotal = models.IntegerField(blank=True, null=True)
    FH04_MotherDiabetic = models.NullBooleanField(blank=True, null=True)
    FH05_MotherAge = models.IntegerField(blank=True, null=True)
    FH06_FatherDiabetic = models.NullBooleanField(blank=True, null=True)
    FH07_FatherAge = models.IntegerField(blank=True, null=True)
    FH08_Sibling01Type = models.IntegerField(blank=True, null=True)
    FH09_Sibling01Diabetic = models.NullBooleanField(blank=True, null=True)
    FH10_Sibling01Age = models.IntegerField(blank=True, null=True)
    FH11_Sibling02Type = models.IntegerField(blank=True, null=True)
    FH12_Sibling02Diabetic = models.NullBooleanField(blank=True, null=True)
    FH13_Sibling02Age = models.IntegerField(blank=True, null=True)
    FH14_Sibling03Type = models.IntegerField(blank=True, null=True)
    FH15_Sibling03Diabetic = models.NullBooleanField(blank=True, null=True)
    FH16_Sibling03Age = models.IntegerField(blank=True, null=True)
    FH17_Sibling04Type = models.IntegerField(blank=True, null=True)
    FH18_Sibling04Diabetic = models.NullBooleanField(blank=True, null=True)
    FH19_Sibling04Age = models.IntegerField(blank=True, null=True)
    FH20_Sibling05Type = models.IntegerField(blank=True, null=True)
    FH21_Sibling05Diabetic = models.NullBooleanField(blank=True, null=True)
    FH22_Sibling05Age = models.IntegerField(blank=True, null=True)
    FH23_Sibling06Type = models.IntegerField(blank=True, null=True)
    FH24_Sibling06Diabetic = models.NullBooleanField(blank=True, null=True)
    FH25_Sibling06Age = models.IntegerField(blank=True, null=True)
    FH26_Sibling07Type = models.IntegerField(blank=True, null=True)
    FH27_Sibling07Diabetic = models.NullBooleanField(blank=True, null=True)
    FH28_Sibling07Age = models.IntegerField(blank=True, null=True)
    FH29_Sibling08Type = models.IntegerField(blank=True, null=True)
    FH30_Sibling08Diabetic = models.NullBooleanField(blank=True, null=True)
    FH31_Sibling08Age = models.IntegerField(blank=True, null=True)
    FH32_Sibling09Type = models.IntegerField(blank=True, null=True)
    FH33_Sibling09Diabetic = models.NullBooleanField(blank=True, null=True)
    FH34_Sibling09Age = models.IntegerField(blank=True, null=True)
    FH35_Sibling10Type = models.IntegerField(blank=True, null=True)
    FH36_Sibling10Diabetic = models.NullBooleanField(blank=True, null=True)
    FH37_Sibling10Age = models.IntegerField(blank=True, null=True)
    FH38_FamilyHistoryEntryComments = models.TextField(blank=True, null=True)
