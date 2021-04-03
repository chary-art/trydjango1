from django.db import models
from django.urls import reverse


# Create your models here.


class Product(models.Model):
    objects = None
    DoesNotExist = None
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000,)
    summary     = models.TextField(blank=False, null=False)
    featured        = models.BooleanField(default=True)
    ady         = models.CharField(max_length=120)
    welayaty    = models.CharField(max_length=120)
    etraby      = models.CharField(max_length=120)
    salgysy     = models.CharField(max_length=120)
    bazar_ishguni = models.CharField(max_length=120)
    maglumat    = models.TextField(blank=True, null=True)
    # field_name = forms.ChoiceField(**options)
    telefony    = models.CharField(max_length=120)
    ish_wagty   = models.CharField(max_length=120)
    # field = models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
    # model_pic = models.ImageField(upload_to = 'pic_folder/', default = 'pic_folder/None/no-img.jpg')
    surat     = models.ImageField(upload_to = 'img/%y')
    City_CHOICES = (
        ('city', 'Ashgabat'),
        ('city', 'Mary'),
        ('city', 'Balkan'),
        ('city', 'Turkmenabat'),
        ('city', 'Balkanabat'),
    )
    city = models.CharField(max_length=6, choices=City_CHOICES, default='green')

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"id": self.id})                     #f"/products/{self.id}/"






