from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import HttpResponse
import pandas as pd
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def home(request):
    if request.method == "POST":
        uploaded_file = request.FILES["file"]
        UploaderFile.objects.create(file=uploaded_file)
        return redirect("home")
    return render(request, "home.html")


@staff_member_required(login_url="admin:login")
def admin(request):
    uploaded_file = UploaderFile.objects.all()
    return render(request, "admin.html", {"uploaded_file": uploaded_file})


@staff_member_required(login_url="admin:login")
def downloade_file(request, file_id):
    uploaded_file = get_object_or_404(UploaderFile, id=file_id)
    response = HttpResponse(uploaded_file.file, content_type="application/octet-stream")
    response["Content-Disposition"] = f'attachment;filename="{uploaded_file.file.name}"'
    return response


@staff_member_required(login_url="admin:login")
def view_file(request, file_id):
    uploaded_file = get_object_or_404(UploaderFile, id=file_id)
    file_path = uploaded_file.file.path
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith(".xlsm"):
        df = pd.read_excel(file_path)
    else:
        return HttpResponse("Invalid file format")
    return render(
        request,
        "view_file.html",
        {"file_name": uploaded_file.file.name, "table_data": df.to_html()},
    )
