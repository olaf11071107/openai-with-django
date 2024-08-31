from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

class ChatGptBot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    messageInput = models.TextField()
    bot_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Messages History'
        verbose_name_plural = 'Messages History'
        ordering = ['created_at']
