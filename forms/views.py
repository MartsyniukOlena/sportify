from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ContactRequest
from .forms import ContactRequestForm

def contact_request(request):
    if request.method == 'POST':
        form = ContactRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for contacting us! Your message has been sent successfully. We will get back to you shortly.')
            return redirect(reverse('contact_request'))
    else:
        form = ContactRequestForm()
    return render(request, 'forms/contact_request.html', {'form': form})