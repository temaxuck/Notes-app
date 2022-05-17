from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Note(models.Model):
	title = models.CharField(max_length=100, default='Untitled')
	content = models.TextField(default='', blank=True)
	timestampCreated = models.DateTimeField(default=timezone.now)
	timestampLastModified = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.title}'

	def update(self, title, content):
		self.title = title
		self.content = content
		self.save()

	class Meta:
		ordering = ['-timestampLastModified']