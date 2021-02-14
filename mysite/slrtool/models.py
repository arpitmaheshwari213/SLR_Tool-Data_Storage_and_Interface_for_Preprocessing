from django.db import models
import os
from datetime import datetime
# Create your models here.
class Document(models.Model):
    document = models.FileField(upload_to='document/'+datetime.now().strftime('%Y-%m-%d_%H-%M-%S')+'/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Paper(models.Model):
    #'paper_type','id_on_web','author','booktitle', 'title', 'year', 'volume', 'number', 'pages',
    #'abstract', 'keywords', 'doi', 'issn', 'publisher', 'isbn', 'paper_url','pdf_url','language'
    paper_type = models.CharField(max_length=30)
    id_on_web = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=200)
    booktitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    year = models.IntegerField(null=True)
    volume = models.CharField(max_length=100,null=True)
    number = models.CharField(max_length=100,null=True)
    pages = models.CharField(max_length=100,null=True)
    abstract = models.CharField(max_length=2000,null=True)
    keywords = models.CharField(max_length=1000,null=True)
    doi = models.CharField(max_length=100,null=True)
    issn = models.CharField(max_length=100,null=True)
    publisher = models.CharField(max_length=100,null=True)
    isbn = models.CharField(max_length=100,null=True)
    language = models.CharField(max_length=100,null=True)
    url = models.CharField(max_length=1000,null=True)
    pdf_url =  models.CharField(max_length=1000,null=True)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)

class QualityAssessment(models.Model):
    paper_id =  models.ForeignKey(Paper, on_delete=models.CASCADE)
    q1 = models.BooleanField(default=False)
    q2 = models.BooleanField(default=False)
    q3 = models.BooleanField(default=False)
    q4 = models.BooleanField(default=False)
    q5 = models.BooleanField(default=False)
    q6 = models.BooleanField(default=False)
    q7 = models.BooleanField(default=False)
    q8 = models.BooleanField(default=False)
    q9 = models.BooleanField(default=False)
    q10 = models.BooleanField(default=False)
    q11 = models.BooleanField(default=False)
    q12 = models.BooleanField(default=False)
    q13 = models.BooleanField(default=False)
    q14 = models.BooleanField(default=False)
    q15 = models.BooleanField(default=False)
    qa_passed = models.BooleanField(default=False)
    remarks = models.CharField(max_length=1000,null=True)
