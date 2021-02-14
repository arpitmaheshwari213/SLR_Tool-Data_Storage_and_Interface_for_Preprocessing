from django import forms

from slrtool.models import Document,Paper,QualityAssessment
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _
import django.utils.timezone as timezone


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'document', )

def get_list(val,document_id):
    document=Document(id=document_id)
    choices_list=Paper.objects.filter(document_id=document).values_list(val,flat=True).distinct()
    #if val == 'language':
    choices_list = [x for x in choices_list if x]
        #choices_list.remove('None')
    choices=[]
    choices=[tuple([x,x]) for x in choices_list]
    choices.append(tuple(['All','All']))
    return choices

class FilterForm(forms.Form):
    def __init__(self,document_id, *args, **kwargs):
        super(FilterForm, self).__init__(*args, **kwargs)
        self.fields['paper_type'] = forms.ChoiceField(choices=get_list('paper_type',document_id),initial='All')
        self.fields['publisher'] = forms.ChoiceField(choices=get_list('publisher',document_id),initial='All')
        self.fields['language'] = forms.ChoiceField(choices=get_list('language',document_id),initial='All')
        self.fields['year_from']= forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(timezone.now().year)],required=False)
        self.fields['year_to']= forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(timezone.now().year)],required=False)
        self.fields['keywords']=forms.CharField(label='Search with Keywords',required=False)
        self.fields['title']=forms.CharField(label='Search with Book/Conference Title',required=False)
        self.fields['document_id']=forms.IntegerField(widget=forms.HiddenInput(),required=True)

    def clean(self):
        cleaned_data = self.cleaned_data
        year_to_data = cleaned_data.get('year_to')
        year_from_data = cleaned_data.get('year_from')
        if(year_from_data=="" or year_from_data is None):
            if(year_to_data!="" and year_to_data is not None):
                self.add_error('year_to', 'Please fill year from and to both.')
        elif(year_to_data=="" or year_to_data is None):
            self.add_error('year_to', 'Please fill year from and to both.')
        elif(year_to_data<year_from_data):
                self.add_error('year_to','Invalid Years, Ensure from is less than to')
        else:
            return cleaned_data

class QAForm(forms.Form):
    q1=forms.BooleanField(initial=False,required=False,label='1. Are the goals of the experiment clear?')
    q2=forms.BooleanField(initial=False,required=False,label='2. Were the research questions and hypothesis defined?')
    q3=forms.BooleanField(initial=False,required=False,label='3. Was there any replication? for example multiple test objects, multiple test sets? ')
    q4=forms.BooleanField(initial=False,required=False,label='4. Are the study measures valid? ')
    q5=forms.BooleanField(initial=False,required=False,label='5. If the test cases were required by the Test Treatment, how were the test cases generated?')
    q6=forms.BooleanField(initial=False,required=False,label='6. How were the test objects generated?')
    q7=forms.BooleanField(initial=False,required=False,label='7. How were the faults/modifications found?')
    q8=forms.BooleanField(initial=False,required=False,label='8. Did the Statistical analysis match the study design?')
    q9=forms.BooleanField(initial=False,required=False,label='9. Was any sensitivity analysis done to assess whether results were due to a specific test object or a specific type of fault/modification?')
    q10=forms.BooleanField(initial=False,required=False,label='10. Were limitations of the study reported either during  the explanation of the study design or during the discussion of the study results?')
    q11=forms.BooleanField(initial=False,required=False,label='11. Were the findings clearly reported?')
    q12=forms.BooleanField(initial=False,required=False,label='12. Are the findings of value to industry or researchers?')
    q13=forms.BooleanField(initial=False,required=False,label='13. Authors?')
    q14=forms.BooleanField(initial=False,required=False,label='14. University?')
    q15=forms.BooleanField(initial=False,required=False,label='15. Publication source?')
    qa_passed = forms.BooleanField(initial=False,required=False,label='Quality Assessment Passed (Yes/No)')
    remarks=forms.CharField(max_length=1000,required=False,label='Additional Remarks',widget=forms.Textarea)
    def __init__(self,paper_id):
        super(QAForm, self).__init__()
        self.fields['paper_id'] = forms.IntegerField(initial=paper_id,widget=forms.HiddenInput(),required=True)
