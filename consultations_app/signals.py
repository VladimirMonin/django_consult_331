from consultations.settings import TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ConsultationRequest
from .telegram_bot import send_telegram_message
import asyncio

@receiver(post_save, sender=ConsultationRequest)
def send_telegram_notification(sender, instance, created, **kwargs):
    if created:
        message = f"""
*Новая заявка на консультацию*
*Имя:* {instance.first_name}
*Фамилия:* {instance.last_name or 'не указана'}
*Email:* {instance.email or 'не указан'}
*Телефон:* {instance.phone or 'не указан'}
*Контакт в Telegram:* {instance.telegram_contact or 'не указан'}
*Комментарий:* {instance.comment or 'не указан'}
*Дата создания:* {instance.created_at.strftime('%Y-%m-%d %H:%M:%S')}
        """
        asyncio.run(send_telegram_message(TELEGRAM_BOT_TOKEN, YOUR_PERSONAL_CHAT_ID, message))