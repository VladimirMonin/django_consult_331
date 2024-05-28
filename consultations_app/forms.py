from django import forms
from .models import ConsultationRequest
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class ConsultationRequestForm(forms.ModelForm):
    class Meta:
        model = ConsultationRequest
        fields = ['first_name', 'last_name', 'email', 'telegram_contact', 'phone', 'comment']

    def __init__(self, *args, **kwargs):
        super(ConsultationRequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        telegram_contact = cleaned_data.get('telegram_contact')
        phone = cleaned_data.get('phone')
        if not email and not telegram_contact and not phone:
            raise forms.ValidationError('Необходимо ввести хотя бы один контакт: email, телефон или контакт в Telegram.')
        # Тут мы можем внедрить свою логику. Данные очищены, и напрмер мы хотим отправить уведомление на почту
        return cleaned_data
