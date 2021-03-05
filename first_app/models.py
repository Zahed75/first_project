from django.db import models

# Create your models here.
class Musician(models.Model):
    #id=models.AutoFiled(Primary_Key=True)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=40)
    instrument=models.CharField(max_length=40)
    def __str__(self):
        return (self.first_name)


class Album(models.Model):
    artist=models.ForeignKey(Musician, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    release_date= models.DateField()

    rating=(
    (1,"Normal"),
    (2,"Bad"),
    (3,"Worse"),
    (4,"Good"),
    (5,"Excellent"),
    )
    num_stars=models.IntegerField(choices=rating)

class Text(models.Model):
    letter=models.CharField(max_length=20)

class Planguage(models.Model):
    name=models.CharField(max_length=30)
    writter=models.CharField(max_length=20)
    price=models.DecimalField(max_digits=30,decimal_places=2)
    # def __str__(self):
    #     return (self.name)
    def __str__(self):
        return str(self.name) + ": bdt" + str(self.price)


    rating=(
    (1,"*"),
    (2,"**"),
    (3,"***"),
    (4,"****"),
    (5,"*****"),
    )
    rating=models.IntegerField(choices=rating)

# class Media(models.Model):
#     m=models.
