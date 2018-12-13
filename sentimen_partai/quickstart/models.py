from django.db import models

# Create your models here.
class Book(models.Model):
    query = models.CharField()
    tweets = models.ListField(
        child=models.CharField(),
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})