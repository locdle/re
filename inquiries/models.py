from django.db import models
from django.db.models import Count
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

#class Starq(models.Model):
#    starq_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#    def __unicode__(self):              # __unicode__ on Python 2
#        return self.starq_text
#    rating_amount = Count('rating_set')
#    def overall_rating(self):
#        for rating in starq.rating_set.iterator():
#            rating_amount += 1
#        return rating_amount
#            
#                
#class Rating(models.Model):
#    starq = models.ForeignKey(Starq)
#    value = models.IntegerField(default=0, validators=[MinValueValidator(0),  MaxValueValidator(5)])
#    pub_date = models.DateTimeField('date published')
#    def is_rating_zero(self):
#        return self.rating == 0
#    is_rating_zero.admin_order_field = 'rating'
##    is_rating_zero.boolean = True
#    is_rating_zero.short_description = 'Not Rated'
#    def __unicode__(self):
#        return self.value

#class Textq(models.Model):
#    textq_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#    answer = models.TextField()
#    def __unicode__(self):              # __unicode__ on Python 2
#        return self.textq_text

class Question(models.Model):
    pub_date = models.DateTimeField('date published')
    rating = models.BooleanField(default = False)
    question_response = models.CharField(max_length=1000)
    
    
