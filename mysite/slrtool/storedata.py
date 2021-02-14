from pybtex.database import parse_string,parse_file,BibliographyData, Entry
from mysite.settings import BASE_DIR
from slrtool.models import Paper
# from bs4 import BeautifulSoup
# def get_video_links(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content)
#     links = soup.findAll('a')
#     video_links =
#     return video_links
def storePapersInDatabase(uploaded_form):
    file_url=uploaded_form.document.url
    document_id=uploaded_form
    #Paper.objects.all().delete()
    bib=parse_file(BASE_DIR+file_url,'bibtex')
    for key,entry in bib.lower().entries.items():
        d={}
        d=dict(entry.fields)
        d['id_on_web'] = key
        if((entry.type.lower())!="inbook"):
            d['paper_type'] = entry.type
        else:
            continue;
        author=""
        for i in entry.persons.values():
            first=True
            for j in i:
                if first:
                    first = False
                else:
                    author=author+', '
                author=author+''.join(j.first())
                author=author+' '+''.join(j.middle())
                author=author+' '+''.join(j.last())
        author = author.replace('{', '').replace('}', '')

        d['author']= author
        d['document_id']=document_id
        # create instance of model Paper by unpacking dictionary
        for k in dict(entry.fields):
            if not hasattr(Paper(), k):
                d.pop(k)
        if('doi' in d):
            d['pdf_url']='https://doi.org/'+d['doi']

        m = Paper(**d)
        # save to database!
        m.save()
