from django import forms
from django_gentoo_pkg.simple_qa.models import QAReport
#from django_gentoo_pkg.simple_qa.models import Package

CHOICES = (
    ('category', 'Software category'),
    ('package', 'Package name'),
    ('version', 'Package version'),
    ('keywords', 'Keyword architecture'),
    ('qa_class', 'QA classification'),
    ('short_desc', 'Description'),
    ('arch', 'Stabled architecture'),
    ('threshold', 'Threshold'),
)

class AdvancedSearch(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    query = forms.CharField(max_length=255, label="Advanced search", 
                            initial="keywords", required=False)
    fields = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(
                                        attrs={'class': 'checkboxes'}), 
                                        choices=CHOICES, required=False)


class SimpleSearch(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    query = forms.CharField(max_length=255, label="Search", initial="keywords")


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
