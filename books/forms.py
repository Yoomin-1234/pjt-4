from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "description",
            "customer_review_rank",
            "author",
        ]
        labels = {
            "title": "도서 제목",
            "description": "도서 설명",
            "customer_review_rank": "회원 리뷰 평점",
            "author": "저자",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "도서 제목을 입력하세요.",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "도서 설명을 입력하세요.",
                }
            ),
            "customer_review_rank": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 0,
                    "max": 10,
                }
            ),
            "author": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "저자 이름을 입력하세요.",
                }
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if len(title) < 1:
            raise forms.ValidationError("도서 제목을 입력해 주세요.")

        return title

    def clean_author(self):
        author = self.cleaned_data["author"].strip()

        if len(author) < 1:
            raise forms.ValidationError("저자 이름을 입력해 주세요.")

        return author
