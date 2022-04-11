from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=45)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'


class Drink(models.Model):
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=45)
    description = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    allergies = models.ManyToManyField('Allergy', through = 'DrinkAllergy')
    
    class Meta:
        db_table = 'drinks'


class DrinkAllergy(models.Model):
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'drinks_allergies'


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    sudium_mg = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    saturated_fat_g= models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    sugar_g = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    protein_g = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    caffein_mg = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)
    size = models.ForeignKey('Size', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'nutritions'
    
class DrinkImage(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.CASCADE)

    class Meta:
        db_table = 'drink_images'
    

class Allergy(models.Model):
    name = models.CharField(max_length=45)


    class Meta:
        db_table = 'allergies'


class Size(models.Model):
    name = models.CharField(max_length=45)
    size_ml = models.CharField(max_length=45, null=True)
    size_fluid_ounce = models.CharField(max_length=45, null=True)
    
    class Meta:
        db_table = 'sizes'
