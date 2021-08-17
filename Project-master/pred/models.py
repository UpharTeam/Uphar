from django.db import models
from med.models import Medicine
from guide.models import guides
# Create your models here.
class prediction(models.Model):
    medicine = models.ForeignKey(guides,on_delete=models.CASCADE, null=True,verbose_name='Medicine')
    pd_price = models.FloatField(verbose_name='Medicine Price',default=0.0)
    pd_qty = models.IntegerField(default=0,verbose_name='Medicine Quantity')
    pd_tot = models.FloatField(default=0.0,verbose_name='Total price')
    date_data = models.DateField(default='',max_length=100)
