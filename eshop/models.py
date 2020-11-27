from django.db import models

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    cartgory=models.CharField(max_length=50,default='')
    subcartgory=models.CharField(max_length=30,default='')
    price= models.IntegerField(default=0)
    decs=models.CharField(max_length=300)
    date=models.DateField()
    image=models.ImageField(upload_to="shop/img",default="")
    timage=models.ImageField(upload_to="shop/img",default="")
    def __str__(self):
        return self.product_name


class relprod(models.Model):
    rel_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    rate=models.IntegerField(default=0)
    img=models.ImageField(upload_to="shop/related",default="")


    def __str__(self):
        return self.name
