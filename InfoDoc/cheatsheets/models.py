from django.db import models

# Create your models here.
class PdfFile(models.Model):
    username = models.CharField(max_length=200)
    cheatsheat_name = models.CharField(max_length=300)
    pdf_file = models.FileField()

    def __str__(self):
        return self.cheatsheat_name