from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        max_length=50,
        unique=True,
        help_text="Unique value for category page URL, created from name.",
    )
    meta_keywords = models.CharField(
        "Meta Keywords",
        max_length=255,
        help_text="Comma-delimited set of SEO keywords for meta tag",
    )
    meta_description = models.CharField(
        "Meta Description", max_length=255, help_text="Content for description meta tag"
    )

    def save(self, *args, **kwargs):
        # Tự động tạo slug từ trường name
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'categories'
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'

    @property
    def get_absolute_url(self):
        return reverse('catalog_category', kwargs={'category_slug': self.slug})