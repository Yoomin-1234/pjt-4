from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import (
    require_GET,
    require_http_methods,
    require_POST,
)
from .services import create_author_metadata
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
            # 1. 도서 정보를 가져오되 아직 DB에 저장하지 않음
            book = form.save(commit=False)

            try:
                # 2. 저자 이름으로 위키백과 검색 및 AI 정보 생성
                author_data = create_author_metadata(book.author)

                # 3. 생성된 작가 정보를 Book 객체에 저장
                book.author_info = author_data["author_info"]
                book.author_works = author_data["author_works"]
                book.author_image_url = author_data["author_image_url"]

            except Exception as error:
                # 4. 작가 정보 생성에 실패해도 도서는 저장
                print(f"작가 정보 생성 실패: {error}")

                book.author_info = "현재 작가 정보를 생성할 수 없습니다."
                book.author_works = []
                book.author_image_url = ""

            # 5. 도서와 작가 정보를 DB에 저장
            book.save()

            # 6. 저장한 도서의 상세 페이지로 이동
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
        # 수정 전 저자 이름 저장
        original_author = book.author

        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            # 아직 DB에 저장하지 않고 수정 내용만 반영
            book = form.save(commit=False)

            # 저자 이름이 변경된 경우에만 AI 정보 갱신
            if original_author != book.author:
                try:
                    author_data = create_author_metadata(book.author)

                    book.author_info = author_data["author_info"]
                    book.author_works = author_data["author_works"]
                    book.author_image_url = author_data["author_image_url"]

                except Exception as error:
                    print(f"작가 정보 갱신 실패: {error}")

                    # 새 저자의 정보를 가져오지 못한 경우
                    book.author_info = "현재 작가 정보를 생성할 수 없습니다."
                    book.author_works = []
                    book.author_image_url = ""

            # 수정한 도서 정보 저장
            book.save()

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

