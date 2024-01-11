from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.
def rental_review(request):
    
    # POST REQUEST  --> FORM CONTENT --> THANK YOU
    #check if someone post something
    if request.method == 'POST':
        #if so pass that information into the review form
        form = ReviewForm(request.POST)
        
        # this is essentially django checking automatically things like, there are check  fields at forms.py
        # and if it's valid, then i can do whatever i want for the information by accessing it through what assentially a python dictionary
        if form.is_valid():
            
            # {' first_name': 'sairi',}
            print(form.cleaned_data)
            #here i redirect them
            return redirect(reverse('cars:thank_you'))
        
    #ELSE --> RENDER THE FORM 
    #otherwise, it's the first time visited page to have a hit, submit then go ahead and just create the form and pass it in here as context of the page
    else:
        form = ReviewForm()
    return render(request, 'cars/rental_review.html', context={form:form} )
    

def thank_you(request):
    return render(request, 'cars/thank_you.html') 

