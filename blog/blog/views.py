from django.http import HttpResponse

def index(request):
    return HttpResponse('윤태호')