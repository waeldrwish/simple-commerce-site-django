from django.shortcuts import render
from .models import Product
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
def index (request):
    return render(request,'shop/index.html',{'products': Product.objects.all()})