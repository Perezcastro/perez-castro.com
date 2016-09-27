from django.shortcuts import render



# Create your views here.
def index(request):
	title= 'PEREZ-CASTRO.COM'
	context ={
		'title': title,}
	return render(request,'base/index.html',context)