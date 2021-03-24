from django.db import models

"""
Your Task
This assignment is to use Django REST framework and a fresh Django server
to create an API as a potential demo for a shoe store with the following
models, broken out for standardization:

Manufacturer
name: str
website: url

---

ShoeType
style: str

---

ShoeColor
color_name: str (ROYGBIV + white / black) --> 
hint: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices

---

Shoe
size: int
brand name: str
manufacturer: FK (Foreign Key)
color: FK
material: str
shoe_type: FK
fasten_type: str

"""


# Manufacturer
class NSManufacturer(models.Model):
    """
    name: str
    website: url
    """
    name = models.CharField(max_length=50, blank=True, default='')
    website = models.URLField()


# ShoeType
class NSShoeType(models.Model):
    """
    style: str
    """
    style = models.CharField(max_length=50, blank=True, default='')


# ShoeColor
class NSShoeColor(models.Model):
    """
    # color_name: str (ROYGBIV + white / black) -->
    # hint: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices
    """
    ROYGBIV = 'RYG'
    WHITE = 'WH'
    BLACK = 'BLK'
    COLOR_NAME_CHOICES = [
        (ROYGBIV, 'ROYGBIV'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
    ]
    color_name = models.CharField(
        max_length=3,
        choices=COLOR_NAME_CHOICES,
        default=WHITE,
    )


# Shoe
class NSShoe(models.Model):
    """
    size: int
    brand name: str
    manufacturer: FK (Foreign Key)
    color: FK
    material: str
    shoe_type: FK
    fasten_type: str
    """
    size = models.IntegerField(blank=True, default='')
    brand_name = models.CharField(max_length=50, blank=True, default='')
    manufacturer = models.ForeignKey('NSManufacturer', on_delete=models.CASCADE)
    color = models.ForeignKey('NSShoeColor', on_delete=models.CASCADE)
    material = models.CharField(max_length=25, blank=True, default='')
    shoe_type = models.ForeignKey('NSShoeType', on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=25, blank=True, default='')
