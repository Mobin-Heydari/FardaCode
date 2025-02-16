from datetime import timedelta
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Session, CourseSeason

@receiver(post_save, sender=Session)
@receiver(post_delete, sender=Session)
def update_season_duration(sender, instance, **kwargs):
    season = instance.season
    total_duration = timedelta()  # Initialize as timedelta object

    # Sum up the durations of all sessions in the season
    for session in season.sessions.all():
        if session.duration:
            total_duration += session.duration
    season.duration = total_duration
    season.save()

    # Calculate the total duration for the course
    course = season.course
    total_course_duration = timedelta()  # Initialize as timedelta object
    for season in course.seasons.all():
        if season.duration:
            total_course_duration += season.duration
    course.duration = total_course_duration
    course.save()
