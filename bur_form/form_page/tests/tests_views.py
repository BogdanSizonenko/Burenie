from django.test import TestCase, Client
from ..forms import ContactForm
from django.urls import reverse
from django import forms


class HomeViewsTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.con = Client()
    # проверяем классы полей формы на домашней страницы
    def test_page_show_correct_context(self):
        response = HomeViewsTests.con.get(reverse('home'))
        form_fields = {
            'from_email' : forms.EmailField,
            'subject' : forms.CharField,
            'message' : forms.CharField,
        }
        context_fields = response.context['form'].fields
        for value in context_fields:
            field = context_fields[value]
            self.assertIsInstance(field, form_fields[value])
    
    def test_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'bur_page/home.html')


if __name__ == '__main__':
    unittest.main()
