from django.db import models
from django.core.exceptions import ValidationError

class ConsultationRequest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    telegram_contact = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
        
    def save(self, *args, **kwargs):
        # Вызываем метод clean, чтобы убедиться, что данные валидны
        # После, мы можем отправить уведомление на почту, например
        super().save(*args, **kwargs)
        pass

    def __str__(self):
        return f"{self.first_name} {self.created_at}"
