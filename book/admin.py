from django.contrib import admin
from .models import Category, Course, Book
# your book models here

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'course_code', 'book_file')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_name', 'course_description', 'course_code')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description', 'category_short_name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Book, BookAdmin)
