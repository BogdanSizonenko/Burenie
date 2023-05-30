from django.test import TestCase
from ..forms import ContactForm


class ContactFormTests(TestCase):
    # два разных метода тестов
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = ContactForm()
    # проверяем лейблы полей формы
    def test_form_label_field(self):
        email_label = ContactFormTests.form.fields['from_email'].label
        subject_label = ContactFormTests.form.fields['subject'].label
        message_label = ContactFormTests.form.fields['message'].label
        self.assertEqual(email_label, 'Email')
        self.assertEqual(subject_label, 'Тема')
        self.assertEqual(message_label, 'Сообщение')
    # проверяем required полей формы
    def test_form_required_field(self):
        form = ContactForm()
        self.assertTrue(form.fields['from_email'].required == True)
        self.assertTrue(form.fields['subject'].required == True)
        self.assertTrue(form.fields['message'].required == True)
    # проверяем атриббуты полей формы
    def test_from_attrs_field(self):
        form = ContactForm()
        self.assertTrue(form.fields['message'].widget.attrs['placeholder'] == 'Напишите тут свое сообщение')


if __name__ == '__main__':
    unittest.main()