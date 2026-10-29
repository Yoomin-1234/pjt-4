from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (
    require_GET,
    require_http_methods,
    require_POST,
)

from .forms import BookForm
from .models import Book

# Create your views here.
@require_GET
def index(request):
    books = Book.objects.all().order_by("-pk")

    context = {
        "books": books,
    }
    return render(request, "books/index.html", context)

@require_GET
def detail(request, pk):
    book = get_object_or_404(Book, pk=pk)

    context = {
        "book": book,
    }
    return render(request, "books/detail.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            book = form.save()
            return redirect("books:detail", book.pk)
    else:
        form = BookForm()

    context = {
        "form": form,
        "page_title": "도서 등록",
    }
    return render(request, "books/form.html", context)

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            book = form.save()
            return redirect("books:detail", book.pk)
    else:
        form = BookForm(instance=book)

    context = {
        "form": form,
        "book": book,
        "page_title": "도서 수정",
    }
    return render(request, "books/form.html", context)

@login_required
@require_POST
def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()

    return redirect("books:index")

