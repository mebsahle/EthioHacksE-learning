from django.contrib import admin

# Register your models here.
from .models import Category, Course, VideoTutorial

class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'course_code', 'video_file')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'category_name', 'course_description')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description', 'category_short_name')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(VideoTutorial, VideoAdmin)
