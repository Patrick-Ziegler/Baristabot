from django.db import models
import uuid



# User -
# Liked -
# Created - 
# Drink -
# Contains -
# Side -
# Pairs With -



class Ingredient(models.Model):
    name = models.CharField(primary_key=True)
    caffination = models.IntegerField()
    
    def __str__(self):
        return f"<ingrediant_name = {self.name} contains = {self.caffination}mg of caffeine>"

class Drink(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField()
    officiality = models.BooleanField()
    description = models.TextField()
    instructions = models.TextField()
    temperature= models.IntegerField()
    contains = models.ManyToManyField(Ingredient)
    def __str__(self):
        return f"<drink_id = {self.id} drink_name = {self.name} drink_officiality = {self.officiality}>"

class User(models.Model):
    username = models.CharField(primary_key=True)
    password = models.CharField() # Unsure how to do safety stuff with passwords
    email = models.EmailField()
    liked = models.ManyToManyField(Drink, related_name='liked_drinks')
    created = models.ManyToManyField(Drink, related_name='created_drinks')
    
    def __str__(self):
        return f"<User {self.username} with email: {self.email}>"

class Side(models.Model):
    name = models.CharField(primary_key=True)
    description = models.TextField()
    pair_with = models.ForeignKey(Drink, null=False, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"side_name = {self.name}"