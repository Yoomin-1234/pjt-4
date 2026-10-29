from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

GENRE_CHOICES = [
    ('소설/시/희곡', '소설/시/희곡'),
    ('경제/경영', '경제/경영'),
    ('자기계발', '자기계발'),
    ('인문/교양', '인문/교양'),
    ('과학', '과학'),
    ('취미/실용', '취미/실용'),
    ('어린이/청소년', '어린이/청소년'),
]


class CustomUserCreationForm(UserCreationForm):
    interested_genres = forms.MultipleChoiceField(
        choices=GENRE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='관심 장르',
    )

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            'username',
            'email',
            'last_name',
            'first_name',
            'gender',
            'age',
            'weekly_reading_time',
            'annual_reading_count',
            'interested_genres',
        )
        labels = {
            'username': '아이디',
            'email': '이메일',
            'last_name': '성',
            'first_name': '이름',
            'gender': '성별',
            'age': '나이',
            'weekly_reading_time': '주간 평균 독서 시간(시간)',
            'annual_reading_count': '연간 독서량(권)',
            'interested_genres': '관심 장르',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = '비밀번호'
        self.fields['password2'].label = '비밀번호 확인'


class CustomUserChangeForm(UserChangeForm):
    interested_genres = forms.MultipleChoiceField(
        choices=GENRE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='관심 장르',
    )

    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = (
            'email',
            'last_name',
            'first_name',
            'gender',
            'age',
            'weekly_reading_time',
            'annual_reading_count',
            'interested_genres',
        )
        labels = {
            'email': '이메일',
            'last_name': '성',
            'first_name': '이름',
            'gender': '성별',
            'age': '나이',
            'weekly_reading_time': '주간 평균 독서 시간(시간)',
            'annual_reading_count': '연간 독서량(권)',
            'interested_genres': '관심 장르',
        }