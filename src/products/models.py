from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,unique=True)
    
    class Meta:
        ordering=('name',)
        verbose_name = 'category'
        verbose_name_plural = 'category'
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:category',args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    gender = models.CharField(max_length=20 , blank=True, null=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('created',)
        index_together = (('id', 'slug'),)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('products:product_detail',args=[self.slug])
    
    
# def get_image_filename(instance, filename):
#     title = instance.product.name
#     slug = slugify(title)
#     return "post_images/%s-%s" % (slug, filename)  


# class Images(models.Model):
#     product = models.ForeignKey(Product, default=None,related_name='images' , on_delete=models.CASCADE)
#     image = models.ImageField(upload_to=get_image_filename,verbose_name='Image')
    
    