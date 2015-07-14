from django.db import models


class FamHistQuestionnaire(models.Model):
    sibling_choices = (
        (-1, 'None'),
        (1, 'Sister'),
        (2, 'Brother'),
        (3, 'Half sister'),
        (4, 'Half Brother'),
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
    boolean_choices = (
        (-1, 'Please select...'),   
        (2, 'Yes'),
        (3, 'No'),
        (4, 'Not known'),  
    )
    
    FH03_BrotherTotal = models.IntegerField(blank=True, null=True)
    FH02_SisterTotal = models.IntegerField(blank=True, null=True)
    FH04_MotherDiabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH05_MotherAge = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH06_FatherDiabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH07_FatherAge = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH08_Sibling01Type = models.IntegerField(blank=True, null=True, choices=sibling_choices)
    FH09_Sibling01Diabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH10_Sibling01Age = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH11_Sibling02Type = models.IntegerField(blank=True, null=True, choices=sibling_choices)
    FH12_Sibling02Diabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH13_Sibling02Age = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH14_Sibling03Type = models.IntegerField(blank=True, null=True, choices=sibling_choices)
    FH15_Sibling03Diabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH16_Sibling03Age = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH17_Sibling04Type = models.IntegerField(blank=True, null=True, choices=sibling_choices)
    FH18_Sibling04Diabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH19_Sibling04Age = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH20_Sibling05Type = models.IntegerField(blank=True, null=True, choices=sibling_choices)
    FH21_Sibling05Diabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH22_Sibling05Age = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH23_Sibling06Type = models.IntegerField(blank=True, null=True, choices=sibling_choices)
    FH24_Sibling06Diabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH25_Sibling06Age = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH26_Sibling07Type = models.IntegerField(blank=True, null=True, choices=sibling_choices)
    FH27_Sibling07Diabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH28_Sibling07Age = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH29_Sibling08Type = models.IntegerField(blank=True, null=True, choices=sibling_choices)
    FH30_Sibling08Diabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH31_Sibling08Age = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH32_Sibling09Type = models.IntegerField(blank=True, null=True, choices=sibling_choices)
    FH33_Sibling09Diabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH34_Sibling09Age = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH35_Sibling10Type = models.IntegerField(blank=True, null=True, choices=sibling_choices)
    FH36_Sibling10Diabetic = models.IntegerField(blank=True, null=True, choices=boolean_choices)
    FH37_Sibling10Age = models.IntegerField(blank=True, null=True, choices=age_choices)
    FH38_FamilyHistoryEntryComments = models.TextField(blank=True, null=True)
