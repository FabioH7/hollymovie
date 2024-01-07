from django.core.validators import MinLengthValidator, MaxLengthValidator, EmailValidator
from django.forms import ModelForm, CharField, DateInput

from viewer.models import Movie, Author, Genre


class MovieCreateForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            "released": DateInput(format='%d%m%Y', attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    title = CharField(validators=[MinLengthValidator(2), MaxLengthValidator(10)])


class AuthorCreateForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    email = CharField(validators=[EmailValidator()])
    password = CharField(validators=[MinLengthValidator(8)])

class GenreCreateForm(ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
