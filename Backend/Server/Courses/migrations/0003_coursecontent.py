# Generated by Django 5.1.6 on 2025-02-16 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_faqcourse'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Courses/content/images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='Courses/Content/videos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Course Content',
                'verbose_name_plural': 'Course Contents',
            },
        ),
    ]
