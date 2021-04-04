from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    qnt_per_people = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    cost_per_people = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    cost_per_distance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)
    principal_dish = models.BooleanField()
    entrance_dish = models.BooleanField()
    space_restriction = models.BooleanField()
    image = models.ImageField(upload_to='images/', max_length=500, default='https://cdn.dribbble.com/users/1012566/screenshots/4187820/topic-2.jpg')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Dish'
        verbose_name_plural = u'Dishes'






