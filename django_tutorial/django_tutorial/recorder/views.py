from django.http import HttpResponse
from django.template import loader
from .forms import RecordForm
from django.shortcuts import render
from .models import Record


def home(request):
    return HttpResponse("Hello World!")


def update_record(request):
    record = Record.objects.get(name="wilson")
    if request.method == "POST" :
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return HttpResponse(f"Record updated {request.POST}")
        else:
            return HttpResponse("Failed to update record")
    else:
        form = RecordForm(instance=record)
    return render(request, "index.html", {"forms": form})


def create_record(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Record created successfully!")
        else:
            return HttpResponse("Invalid form data!")
    else:
        form = RecordForm()
    return render(request, "index.html", {"forms": form})


def view_records(request):
    data = Record.objects.all()

    # return HttpResponse(data)
    return render(request, "views.html", {"records": data})
