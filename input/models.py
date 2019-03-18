from django.db import models

class Input(models.Model):
    input = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='datum')

    def __str__(self):
        if len(self.input) > 50:
            string = self.input[:50] + "..."
        else:
            string = self.input
        return string
    