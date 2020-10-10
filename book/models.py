from django.db import models
from django.utils import timezone
from django.utils.timezone import now

# your book models here

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.CharField(max_length=300)
    category_created_at = models.DateTimeField(auto_now=True)
    category_short_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    category_name = models.ForeignKey(Category, default="Categori", on_delete=models.CASCADE)
    course_description = models.CharField(max_length=300)
    course_created_at = models.DateTimeField(auto_now=True)
    course_code = models.CharField(max_length=200, help_text='eg. PHYS0000')

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.course_code

class Book(models.Model):
    book_name = models.CharField(max_length=200)
    course_code = models.ForeignKey(Course, default="Cours", on_delete=models.CASCADE)
    book_file = models.FileField(upload_to='books/uploads/',default='null')

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.book_name
    