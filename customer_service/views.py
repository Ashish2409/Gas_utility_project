
# Create your views here.
from datetime import timezone
from django.shortcuts import render, redirect,get_object_or_404, redirect
from .models import ServiceRequest
from .forms import ServiceRequestForm

def service_request_list(request):
    service_requests = ServiceRequest.objects.all()
    print(service_requests)
    return render(request, 'customer_service/request_list.html', {'service_requests': service_requests})

def service_request_detail(request, id):
    service_request = ServiceRequest.objects.get(id=id)
    return render(request, 'customer_service/request_detail.html', {'request': service_request})

def create_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer_service/service_request_form.html', {'form': form})

def change_status(request, id):
    request = get_object_or_404(ServiceRequest, id=id)
    if request.status != 'Completed':
        request.status = 'Completed'
    request.save()
    return redirect('service_request_list')



    







