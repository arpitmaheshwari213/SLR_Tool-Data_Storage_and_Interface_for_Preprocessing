from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from slrtool.models import Document,Paper,QualityAssessment
from slrtool.forms import DocumentForm,FilterForm,QAForm
from slrtool.storedata import storePapersInDatabase
from slrtool.query import getFilterData,isDocumentExist

def filter(request):
    form = FilterForm(request.GET['document_id'],request.GET or request.GET['document_id'])
    if form.is_valid():
        if(isDocumentExist(form.cleaned_data['document_id'])):
            papers=getFilterData(form)
            #request.session['paper'] = papers
            #qaforms= []
            #for i in papers:
            #    qaforms.append(QAForm(i.id))
            context = {'papers':papers} #,'qaforms':qaforms}
            return render(request, 'slrtool/qualitycheck.html', context)
        else:
            return render(request, 'slrtool/filter.html', {
            'form': form,
            'status':0
            })
    else:
        return render(request, 'slrtool/filter.html', {
        'form': form,
        'status':1
        })

def file_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        name = request.FILES['document'].name
        if form.is_valid():
            form.save()
            uploaded_form=form.instance
            storePapersInDatabase(uploaded_form)
            initial_dict = {
            "document_id":uploaded_form.id
            }
            filterform=FilterForm(uploaded_form.id,initial = initial_dict)
            context = {'form':filterform,'status':1} #'uploaded_form':uploaded_form,'name':name,
            return render(request, 'slrtool/filter.html', context)
    else:
        form = DocumentForm()
    return render(request, 'slrtool/index.html', {
        'form': form
    })

def quality_assessment(request):
    if request.method == 'GET':
        paper_id = request.GET["paper_id"]
        papers = Paper.objects.filter(id=paper_id)#Paper(id=paper_id)
        qaform = QAForm(paper_id)
        return render(request,'slrtool/qualityform.html',{
        'papers':papers,
        'qaform':qaform
        })

def add_quality_assessment(request):
    if request.method=='GET':
        paper_id = request.GET["paper_id"]
        form = QAForm(request.GET or paper_id)
        papers = Paper.objects.filter(id=paper_id)
        if form.is_valid():
            # process form data
            obj = QualityAssessment();
            obj.q1 = form.cleaned_data['q1']
            obj.q2 = form.cleaned_data['q2']
            obj.q3 = form.cleaned_data['q3']
            obj.q4 = form.cleaned_data['q4']
            obj.q5 = form.cleaned_data['q5']
            obj.q6 = form.cleaned_data['q6']
            obj.q7 = form.cleaned_data['q7']
            obj.q8 = form.cleaned_data['q8']
            obj.q9 = form.cleaned_data['q9']
            obj.q10 = form.cleaned_data['q10']
            obj.q11 = form.cleaned_data['q11']
            obj.q12 = form.cleaned_data['q12']
            obj.q13 = form.cleaned_data['q13']
            obj.q14 = form.cleaned_data['q14']
            obj.q15 = form.cleaned_data['q15']
            obj.paper_id = Paper(id=form.cleaned_data['paper_id'])
            obj.qa_passed = form.cleaned_data['qa_passed']
            obj.remarks = form.cleaned_data['remarks']
            obj.save()
        else:
            return render(request, 'slrtool/qualityform.html', {
            'qaform': form,
            'papers':papers
            })
