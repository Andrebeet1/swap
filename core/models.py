from django.db import models

class SwapRequest(models.Model):
    full_name = models.CharField(max_length=100)
    old_number = models.CharField(max_length=20)
    new_sim_number = models.CharField(max_length=30)
    id_document = models.FileField(upload_to='ids/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.old_number}"