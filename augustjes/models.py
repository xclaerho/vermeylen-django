from django.db import models

class Augustje(models.Model):
    edition = models.CharField(max_length=50,verbose_name="editie")
    date = models.DateField(verbose_name='datum')
    embed = models.TextField()
    description = models.TextField(blank=True,null=True,verbose_name='beschrijving')

    def __str__(self):
        return self.edition + ', ' + str(self.date)
    
    class Meta:
        ordering = ['-date']

class Subscriber(models.Model):
    name = models.CharField(max_length=50,verbose_name="naam")
    room = models.IntegerField(blank=True,null=True,verbose_name='kamer')
    email = models.EmailField(blank=True,null=True)
    consent = models.BooleanField(default=False,verbose_name="Akkoord met opslag gegevens")

    def __str__(self):
        return self.name
    