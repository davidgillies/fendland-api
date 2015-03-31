from django import forms
from .models import Volunteer


def fields(field_type):
    return {'text': forms.CharField, 'integer': forms.IntegerField,
            'real': forms.FloatField, 'date': forms.DateField,
            'dateTime': forms.DateTimeField, 'time': forms.TimeField,
            }[field_type]


class ValidationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(ValidationForm, self).__init__(*args, **kwargs)
        for field_name in extra.keys():
            if extra[field_name]['type'] == 'text':
                self.fields[field_name] = forms.CharField(max_length=extra[field_name]['max_length'])
            else:
                self.fields[field_name] = forms.EmailField(required=False)


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = Volunteer
    