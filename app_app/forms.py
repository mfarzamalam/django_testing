from django import forms
import datetime


class RenewalBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")

    def clean_renewal_date(self):
        date = self.cleaned_data['renewal_date']

        if date < datetime.date.today():
            raise forms.ValidationError('Invalid date - renewal in past')

        if date > datetime.date.today() + datetime.timedelta(weeks=4):
            raise forms.ValidationError('Invalid date - renewal more than 4 weeks ahead')

        # Remember to always return the cleaned data.
        return date