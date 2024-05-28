from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .forms import ConsultationRequestForm

class HomeView(View):
    def get(self, request):
        form = ConsultationRequestForm()
        return render(request, 'main.html', {'form': form})

    def post(self, request):
        form = ConsultationRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('thank_you'))
        return render(request, 'main.html', {'form': form})

class ThankYouView(View):
    def get(self, request):
        return render(request, 'thank_you.html')
