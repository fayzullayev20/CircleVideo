from django.db import models
from django.conf import settings

class Playlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='playlists')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    videos = models.JSONField(blank=True, null=True) # Yoki ManyToManyField('videos.Video', blank=True) ishlatish ham mumkin

    class Meta:
        db_table = 'playlist'

    def __str__(self):
        return self.title