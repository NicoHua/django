from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world!")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    now = datetime.datetime.now()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>It is now %s. In %s hour(s), it will be %s.</body></html>" % (now, offset, dt)
    return HttpResponse(html)

def weblink(request):
    #swd3home
    #now = datetime.datetime.now()
    fp = open('/home/swd3/workspace/django/mysite/download_zip/download_zip.html')
    html = fp.read()
    fp.close()
    return HttpResponse(html)