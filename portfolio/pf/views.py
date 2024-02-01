from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save form data to the database
            return render('index.html')  # Redirect to success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def index(request):
    return render(request, 'index.html')