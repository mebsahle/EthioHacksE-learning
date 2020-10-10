from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    category_description = models.CharField(max_length=200)
    category_created_at = models.DateTimeField(auto_now=True)
    category_short_name = models.CharField(max_length=200, help_text='eg. PHY')

    class Meta:
        verbose_name_plural = "Category"

    def __str__(self):
        return self.category_name
    

class Course(models.Model):
    course_name = models.CharField(max_length=200)
    category_name = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    course_description = models.CharField(max_length=200)
    course_created_at = models.DateTimeField(auto_now=True)
    course_code = models.CharField(max_length=200, help_text='eg. PHY1001')
    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.course_name
    
class VideoTutorial(models.Model):
    video_title = models.CharField(max_length=200)
    publication_date = models.DateTimeField(auto_now=True)
    video_content_description = models.TextField()
    video_file = models.FileField(upload_to='videos/uploads/', default='null')
    course_code = models.ForeignKey(
        Course,
        default=1,
        on_delete=models.CASCADE
    )
    # likes = models.ManyToManyField(User, blank=True)

    class Meta:
        verbose_name_plural = "VideoTutorials"
    
    def __str__(self):
        return self.video_title
    