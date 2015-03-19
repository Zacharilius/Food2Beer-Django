from django.shortcuts import HttpResponse

def index(request):
	return HttpResponse("Food2Beer_app says hello")


