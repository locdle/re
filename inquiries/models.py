from django.db import models

# Create your models here.

class Starq(models.Model):
    starq_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    rating = models.IntegerField(default=0)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.starq_text
    def is_rating_zero(self):
        return self.rating == 0
    is_rating_zero.admin_order_field = 'rating'
#    is_rating_zero.boolean = True
    is_rating_zero.short_description = 'Not Rated'
    
        

class Textq(models.Model):
    textq_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    answer = models.TextField()
    def __unicode__(self):              # __unicode__ on Python 2
        return self.textq_text
