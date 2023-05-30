from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from bur_form.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from .forms import ContactForm


def home(request):
    ''' Метод определяющий домашную страницу, с текстом из файла и формой для отправки письма на почту'''
    f = open("form_page/templates/bur_page/text.txt", "r", encoding="utf-8")
    file_contents = f.read()
    f.close()

    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        # если метод POST, проверим форму и отправим письмо
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data["message"]
            try:
                send_mail(
                    f"{subject} от {from_email}",
                    message,
                    DEFAULT_FROM_EMAIL,
                    RECIPIENTS_EMAIL,
                )
            except BadHeaderError:
                return HttpResponse("Ошибка в теме письма.")
            return redirect("home")
        else:
            return HttpResponse("Неверный запрос.")
    data = {"text_file": file_contents, "form": form}
    return render(request, "bur_page/home.html", context=data)
