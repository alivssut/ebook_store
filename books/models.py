from django.db import models
from accounts.models import User
from .managers import EbookManager, CommentManager
# Create your models here.

# author model
class Author(models.Model):
    """Model representing an author."""
    full_name = models.CharField(max_length=100, verbose_name='FullName')
    slug = models.SlugField(default="", null=False, db_index=True, blank=False, max_length=200, unique=True, verbose_name='Slug')
    bio = models.TextField(verbose_name='Bio')
    image = models.FileField(upload_to = "authors/images/", null=True, blank=True, verbose_name='image')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='DateOfBirth')
    date_of_death = models.DateField(null=True, blank=True, verbose_name='DateOfDeath')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    def __str__(self):
        """String for representing the Model object."""
        return '{0}'.format(self.full_name)
    
    
# Category model
class Category(models.Model):
    name = models.CharField(max_length=200, null=True, verbose_name='Name')
    icon = models.FileField(upload_to = "category/icons/", null=True, blank=True, verbose_name='Icon')
    slug = models.SlugField(default="", null=False, db_index=True, blank=False, max_length=200, unique=True, verbose_name='Slug')
    description = models.CharField(max_length=500, null=True,blank=True, verbose_name='Description')
    is_active = models.BooleanField(default=False, verbose_name='IsActive')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Catagories'

    def __str__(self):
        return str(self.name) 

# ebook model
class Ebook(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    authors = models.ManyToManyField(Author, related_name='books', verbose_name='Authors')
    pages = models.IntegerField(null=True, blank=True, verbose_name='NumberOfPages')
    price = models.FloatField(verbose_name='Price')
    cover = models.ImageField(upload_to='ebooks/covers/', verbose_name='Cover')
    slug = models.SlugField(default="", null=False, db_index=True, blank=False, max_length=200, unique=True, verbose_name='Slug')
    description = models.TextField(verbose_name='Description')
    # this will be the download link of the ebook
    ebook = models.FileField(upload_to='ebooks/files/', verbose_name='EBook')
    is_active = models.BooleanField(default=False, verbose_name='IsActive')
    # has one to many relationship with Category
    category = models.ManyToManyField(Category, related_name='books', verbose_name='Categories')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = EbookManager()

    class Meta:
        verbose_name = 'EBook'
        verbose_name_plural = 'EBooks'
        
    def __str__(self):
        return self.title
    
# comment model
class Comment(models.Model):
    body = models.TextField(verbose_name='Body')
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, related_name='comments')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False, verbose_name='IsActive')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CommentManager()
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return 'created by {} at {}'.format(self.owner, self.created)