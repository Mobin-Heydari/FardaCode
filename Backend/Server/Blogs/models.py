from django.db import models




class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    image = models.ImageField(upload_to="Blogs/Category/images/")

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"
    
    def __str__(self):
        return self.name



class Blog(models.Model):

    class BlogStatus(models.TextChoices):
        DRAFT = "DRF", "Draft"
        PUBLISHED = "PUB", "Published"
    

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name="blog_category")

    content = models.TextField()

    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    status = models.CharField(max_length=3, choices=BlogStatus.choices, default=BlogStatus.DRAFT)

    image = models.ImageField(upload_to="Blogs/Blog/images/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title
    


class BlogContent(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='Content')

    title = models.CharField(max_length=255, blank=True, null=True)

    content = models.TextField(null=True, blank=True)

    image = models.ImageField(upload_to="Blogs/Blog/content/images/", null=True, blank=True)
    video = models.FileField(upload_to="Blogs/Blog/Content/videos/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog Content'
        verbose_name_plural = 'Blog Contents'

    def __str__(self):
        return f'{self.blog.title}'
    


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='Comments')

    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Blog Comment'
        verbose_name_plural = 'Blog Comments'

    def __str__(self):
        return f'{self.blog.title}'