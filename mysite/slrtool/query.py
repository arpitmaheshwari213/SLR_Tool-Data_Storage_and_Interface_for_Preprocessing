from slrtool.models import Paper,Document
from django.db.models import Q
def getFilterData(form):
    year_from=form.cleaned_data['year_from']
    year_to=form.cleaned_data['year_to']
    paper_type=form.cleaned_data['paper_type']
    keywords= form.cleaned_data['keywords']
    title= form.cleaned_data['title']
    publisher=form.cleaned_data['publisher']
    language=form.cleaned_data['language']
    document_id= form.cleaned_data['document_id']
    document=Document(id=document_id)
    queryFilters = Q(document_id__exact=document)
    if((year_from!="" and year_from is not None ) and (year_to!="" and year_to is not None)):
        queryFilters &= Q(year__range=[year_from, year_to])|Q(year__isnull=True)

    if(paper_type!='All'):
        queryFilters &= Q(paper_type__exact=paper_type)

    if (publisher != 'All'):
        queryFilters &= Q(publisher__exact=publisher)

    if (language != 'All'):
        queryFilters &= Q(language__exact=language)

    if(keywords!="" and keywords is not None):
            #queryFilter = reduce(operator.and_, [Q(abstract__icontains=word) for word in keywords])
            for word in keywords.split(" "):
                queryFilters &=Q(abstract__contains=word)|Q(keywords__contains=word)
    if(title!="" and title is not None):
        for word in title.split(" "):
            queryFilters &=Q(booktitle__contains=word)|Q(title__contains=word)|Q(volume__contains=word)
    papers=Paper.objects.filter(queryFilters).distinct()
    return papers

def isDocumentExist(document_id):
    document=Document(id=document_id)
    if(document is None):
        return False
    return True
