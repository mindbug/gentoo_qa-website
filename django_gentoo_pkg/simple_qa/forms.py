from django import forms
from django_gentoo_pkg.simple_qa.models import QAReport
#from django_gentoo_pkg.simple_qa.models import Package


class SearchForm(forms.Form):
    query = forms.CharField(max_length=255)


class QAReportForm(forms.ModelForm):
    class Meta:
        model = QAReport


TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)


class ContactForm(forms.Form):
    topic = forms.ChoiceField(choices=TOPIC_CHOICES)
    message = forms.CharField()
    sender = forms.EmailField(required=False)
