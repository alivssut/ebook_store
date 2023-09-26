from django.db import models

class EbookManager(models.Manager):
    def all_related_ebooks_to_category(self, category_slug):
        queryset = self.filter(category__slug=category_slug).prefetch_related('category').prefetch_related('authors')
        return queryset
    
    def all_ebooks(self, active=True):
        if active:
            queryset = self.filter(is_active=True).prefetch_related('authors').prefetch_related('category')
        else:
            queryset = self.filter().prefetch_related('authors').prefetch_related('category')
        
        return queryset
    
class CommentManager(models.Manager):
    def all_related_comments_to_ebook(self, ebook_slug):
        queryset = self.filter(post__slug=ebook_slug).prefetch_related('ebook')
        return queryset
    
    def all_comments(self, active=True):
        if active:
            queryset = self.filter(is_active=True).prefetch_related('post')
        else:
            queryset = self.filter().prefetch_related('post')
            
        return queryset