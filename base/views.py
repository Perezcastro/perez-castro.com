from django.shortcuts import render



# Create your views here.
def index(request):
	title= 'PEREZ-CASTRO.COM'
	context ={
		'title': title,}
	return render(request,'base/index.html',context)

def aboutMe(request):
	title= 'Sobre Mi'
	context ={
		'title': title,}
	return render(request,'base/aboutMe.html',context)

def cv(request):
	title = 'Curriculum Vitae'
	context ={
		'title': title,}
	return render(request,'base/cv.html',context)
