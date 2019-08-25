# https://github.com/BaseMax/SimpleDjangoSignals
from django.db import models
from django.db.models import signals

class book(models.Model):
	name = models.CharField(max_length=50)
	author = models.CharField(max_length=25)
	code = models.CharField(max_length=9)

def bookCreated(sender, instance, created, **kwargs):
	print "Saved!"

signals.post_save.connect(receiver=bookCreated, sender=book)

# obj = book(name='book1', author='user1', code='123456')
# ...
# obj.save()
