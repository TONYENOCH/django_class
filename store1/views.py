from django.shortcuts import render
from store1.forms import CreatPostFrom, DummyForm


def hello(request):
    return render(request, 'html/hello.html', {'name':'james', 'message': 'i am happy'})
    return render(request, 'html/goodbye.html')


# def welcome(request):
    # return HttpResponse('<h1>welcome</h2>')

# def home(request):
    # return render(request,'html/home.html')


def createpost(request):

   if request.method=='POST':
        form = DummyForm(request.POST)
        # if form.is_valid():
        #     form.save(commit=False)
   else:
        form = DummyForm()
   return render(request,'html/createpost.html',{'form':form,'tittle':'Create a post'})


# Create your views here.


