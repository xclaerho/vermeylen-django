from django.db import models

class Sponsor(models.Model):
    name = models.CharField(max_length=30,verbose_name='naam')
    logo = models.ImageField(upload_to='sponsors',help_text='Kies een vierkantje foto opdat het er goed uitziet')
    link = models.URLField(help_text='Link naar website of social media',default='#')

    def __str__(self):
        return self.name

class PraesidiumMember(models.Model):
    name = models.CharField(max_length=50,verbose_name='naam')
    function = models.CharField(max_length=20,verbose_name='functie')
    room = models.IntegerField(verbose_name='Kamernummer',help_text='niet verplicht',blank=True,null=True)
    city = models.CharField(max_length=50,verbose_name='afkomstig van')
    study = models.CharField(max_length=50,verbose_name='studie')
    email = models.EmailField()
    image = models.ImageField(verbose_name='foto',upload_to="praesidiumleden",null=True,blank=True,help_text='Kies een vierkante foto opdat het er goed uitziet')
    rank = models.IntegerField()
    
    def __str__(self):
        return self.name + ', ' + self.function

    class Meta:
        verbose_name = "praesidiumlid"
        verbose_name_plural = "praesidiumleden"
        ordering = ['rank']
