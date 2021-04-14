from django.db import models
from django.conf import settings
# Create your models here.


class Writer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

CATEGORY_CHOICES = (
    ('PR', 'Programming'),
    ('WR','Writing'),
    ('WB','Website Development')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S','secondary'),
    ('D','danger')
)
class Item(models.Model):
    title = models.CharField(max_length=100)
    pages = models.FloatField()
    price = models.FloatField()
    description = models.TextField()
    image=models.ImageField(blank=True)
    files= models.FileField(blank=True)
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2, default="WR")
    label = models.CharField(choices=LABEL_CHOICES, max_length=1, default="P")
    #def add-to-inprogress_url(self):

    def __str__(self):
        return self.title

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title
class Order(models.Model):
    STATUS = (
        ('Unassigned', 'Unassigned'),
        ('Pending', 'Pending'),
        ('In Revision', 'In Revision'),
        ('Delivered', 'Delivered'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date=models.DateField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    #inprogress = models.BooleanField(default=False)
    writer = models.ForeignKey(Writer, null=True, on_delete=models.SET_NULL)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.title




