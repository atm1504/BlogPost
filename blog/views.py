from django.shortcuts import render

posts=[
	{
		'author':"atm1504",
		'title':'LOVESTORY',
		'Content':'I love u atreyee',
		'date_posted':'August 15,2018'
	},
	{
		'author':"atreyee",
		'title':'LOVESTORY2',
		'Content':'I love u amartya',
		'date_posted':'January 4 ,2019'
	}
]

# Create your views here.
def home(request):
	context={
	'posts':posts
	}
	return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})
