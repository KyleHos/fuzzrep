from django.shortcuts import render, redirect
from .models import Submit
from .forms import MyForm

def home(request):
    return render(request, 'fuzzball/Homepage.html')

def Formpage(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        # form.save()

        if form.is_valid():    #might work idk
            submit_instance = Submit()
            submit_instance.pet_name = form.cleaned_data['pet_name']
            submit_instance.species = form.cleaned_data['species']
            submit_instance.age = form.cleaned_data['age']
            submit_instance.color = form.cleaned_data['color']
            submit_instance.food_preference = form.cleaned_data['food_preference']

            submit_instance.save()  #till here

            return redirect('submitpage')
    else:
        form = MyForm()
    return render(request, 'fuzzball/Formpage.html', {'form': form})

def submitpage(request):
    submitpage = Submit.objects.all()
    return render(request, 'fuzzball/Submitpage.html', {'submitpage': submitpage})

def clear_submissions(request):    
    Submit.objects.all().delete()
    return redirect('submitpage')