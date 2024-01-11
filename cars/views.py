from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.
def rental_review(request):
    
    # POST REQUEST  --> FORM CONTENT --> THANK YOU
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # this is essentially django checking automatically things like, there are check  fields at forms.py
        if form.is_valid():
            
            # {' first_name': 'sairi',}
            print(form.cleaned_data)
            #
            return redirect(reverse('cars:thank_you'))
        
    #ELSE --> RENDER THE FORM 
    else:
        form = ReviewForm()
    return render(request, 'cars/rental_review.html', context={form:form} )
    

def thank_you(request):
    return render(request, 'cars/thank_you.html') 

