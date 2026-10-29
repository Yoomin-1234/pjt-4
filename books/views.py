from django.shortcuts import render
from .models import Book

from django.http import HttpResponse

# Create your views here.
def index(request):
    books = Book.objects.all().order_by("-pk")
    context = {
        "books": books,
    }
    return render(request, "books/index.html", context)


def create(request):
    return HttpResponse("도서 등록")


def detail(request, pk):
    return HttpResponse(f"{pk}번 도서 상세")


def update(request, pk):
    return HttpResponse(f"{pk}번 도서 수정")


def delete(request, pk):
    return HttpResponse(f"{pk}번 도서 삭제")