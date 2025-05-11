from django.shortcuts import render, redirect
from .models import SwapRequest
from django.core.files.storage import FileSystemStorage

def home(request):
    return render(request, 'core/home.html')

def swap_request(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        old_number = request.POST['old_number']
        new_sim_number = request.POST['new_sim_number']
        id_document = request.FILES['id_document']
        SwapRequest.objects.create(
            full_name=full_name,
            old_number=old_number,
            new_sim_number=new_sim_number,
            id_document=id_document
        )
        return render(request, 'core/home.html', {'success': True})
    return render(request, 'core/swap_form.html')