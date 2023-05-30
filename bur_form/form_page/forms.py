from django import forms


class ContactForm(forms.Form):
    """Форма для заявки на почту"""

    from_email = forms.EmailField(label="Email", required=True)
    subject = forms.CharField(label="Тема", required=True)
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea(attrs={"placeholder": "Напишите тут свое сообщение"}),
        required=True,
    )

    class Media:
        '''Медиа класс Django, определяющий файл стиля для данной формы'''
        css = {"all": ("css/style.css",)}
