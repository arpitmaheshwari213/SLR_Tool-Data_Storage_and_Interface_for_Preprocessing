from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Document
from .models import Paper,QualityAssessment


admin.site.register(Document)
admin.site.register(Paper)
admin.site.register(QualityAssessment)
