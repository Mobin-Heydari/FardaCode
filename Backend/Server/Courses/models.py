from django.db import models





class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to="Courses/Category/images", blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):

    class CourseStatus(models.TextChoices):
        IN_PROGRESS = 'INP', 'In Progress'
        COMPLETED = 'COM', 'Completed'

    class CoursePricingStatus(models.TextChoices):
        FREE = 'FR', 'Free'
        PURCHASABLE = 'PR', 'Purchasable'
    
    teacher = models.ForeignKey(
        'User.User',
        on_delete=models.CASCADE,
        related_name='teacher_courses'
    )

    students = models.ManyToManyField(
        'User.User', 
        related_name='enrolled_courses', 
        blank=True
    )

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='courses'
    )

    poster = models.ImageField(upload_to="Courses/posters/", blank=True, null=True)

    banner = models.ImageField(upload_to="Courses/banners/", blank=True, null=True)

    introduction = models.FileField(upload_to="Courses/introductions/", blank=True, null=True)

    description = models.TextField()
    status = models.CharField(
        max_length=3,
        choices=CourseStatus.choices,
        default=CourseStatus.IN_PROGRESS
    )

    pricing_status = models.CharField(
        max_length=2, 
        choices=CoursePricingStatus.choices, 
        default=CoursePricingStatus.PURCHASABLE
    )

    price = models.BigIntegerField(default=0)

    duration = models.DurationField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        indexes = [
            models.Index(fields=['slug']),
        ]

    def __str__(self):
        return self.title


class FaqCourse(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="Faq_Course"
    )

    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = "FAQ Course"
        verbose_name_plural = "FAQs Courses"

    def __str__(self):
        return self.question



class CourseContent(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to="Courses/content/images/", null=True, blank=True)
    video = models.FileField(upload_to="Courses/Content/videos/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Course Content"
        verbose_name_plural = "Course Contents"


    def __str__(self):
        return self.title
    

class CourseSeason(models.Model):

    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE, 
        related_name='seasons'
    )

    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True, null=True)  # Brief overview of the season
    duration = models.DurationField(blank=True, null=True)
    order = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Course Season"
        verbose_name_plural = "Course Seasons"
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Session(models.Model):

    season = models.ForeignKey(
        CourseSeason, 
        on_delete=models.CASCADE, 
        related_name='sessions'
    )

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Brief description of the session

    video = models.FileField(upload_to="Courses/sessions/videos/")

    duration = models.DurationField(blank=True, null=True)
    materials = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField()


    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"
        ordering = ['order']

    def __str__(self):
        return f"{self.season.title} - {self.title}"