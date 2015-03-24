from django import forms


class ValidationForm(forms.Form):
    def __init__(self, *args, **kwargs):
        extra = kwargs.pop('extra')
        super(ValidationForm, self).__init__(*args, **kwargs)
        for field_name in extra.keys():
            if extra[field_name]['type'] == 'text':
                self.fields[field_name] = forms.CharField(max_length=extra[field_name]['max_length'])
            else:
                self.fields[field_name] = forms.EmailField(required=False)
