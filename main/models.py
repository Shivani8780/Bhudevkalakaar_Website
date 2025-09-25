# Participant model for profile page
from django.db import models

class Participant(models.Model):
	name = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	bio = models.TextField(blank=True)
	skills = models.CharField(max_length=200, blank=True, help_text="Comma-separated skills")
	image = models.ImageField(upload_to='participants/', blank=True, null=True)
	# Removed social/contact fields as requested

	def skill_list(self):
		return [s.strip() for s in self.skills.split(',') if s.strip()]

	def __str__(self):
		return self.name
from django.db import models
from django.conf import settings

class OtherPlaceEvent(models.Model):
	title = models.CharField(max_length=200)
	event_datetime = models.DateTimeField()
	location = models.CharField(max_length=200)
	image = models.ImageField(upload_to='participants/', blank=True, null=True)
	ticket_available = models.BooleanField(default=False, help_text="Is ticket available for this event?")

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if self.image and self.image.name.split('.')[-1].lower() != 'webp':
			from PIL import Image
			import os
			img_path = self.image.path
			webp_path = os.path.splitext(img_path)[0] + '.webp'
			try:
				img = Image.open(img_path)
				img.save(webp_path, 'WEBP', quality=80)
				self.image.name = os.path.relpath(webp_path, settings.MEDIA_ROOT).replace('\\', '/')
				super().save(update_fields=['image'])
				os.remove(img_path)
			except Exception:
				pass
	description = models.TextField(blank=True)
	ticket_available = models.BooleanField(default=False, help_text="Set True if tickets are available for this event.")

	def __str__(self):
		return self.title

# Home page images managed by admin
class HomePageImage(models.Model):
	title = models.CharField(max_length=100, blank=True)
	image = models.ImageField(upload_to='homepage_images/')

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if self.image and self.image.name.split('.')[-1].lower() != 'webp':
			from PIL import Image
			import os
			img_path = self.image.path

# ...existing code...

class ContactMessage(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField()
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} ({self.email})"

# Past event images managed by admin
class PastEvent(models.Model):
	title = models.CharField(max_length=200)
	image = models.ImageField(upload_to='past_events/')

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if self.image and self.image.name.split('.')[-1].lower() != 'webp':
			from PIL import Image
			import os
			img_path = self.image.path
			webp_path = os.path.splitext(img_path)[0] + '.webp'
			try:
				img = Image.open(img_path)
				img.save(webp_path, 'WEBP', quality=80)
				self.image.name = os.path.relpath(webp_path, settings.MEDIA_ROOT).replace('\\', '/')
				super().save(update_fields=['image'])
				os.remove(img_path)
			except Exception:
				pass

	def __str__(self):
		return self.title if self.title else "Past Event"

# Photos page images managed by admin
class Photo(models.Model):
	caption = models.CharField(max_length=200, blank=True)
	image = models.ImageField(upload_to='photos/')

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		if self.image and self.image.name.split('.')[-1].lower() != 'webp':
			from PIL import Image
			import os
			img_path = self.image.path
			webp_path = os.path.splitext(img_path)[0] + '.webp'
			try:
				img = Image.open(img_path)
				img.save(webp_path, 'WEBP', quality=80)
				self.image.name = os.path.relpath(webp_path, settings.MEDIA_ROOT).replace('\\', '/')
				super().save(update_fields=['image'])
				os.remove(img_path)
			except Exception:
				pass
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.caption or f"Photo {self.id}"
# Form submission model for ticket purchase
class UserFormData(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone_number = models.CharField(max_length=20)
	ticket_quantity = models.PositiveIntegerField(blank=True, null=True)
	total_amount = models.DecimalField(max_digits=10, decimal_places=2)
	payment_screenshot = models.ImageField(upload_to='payment_screenshots/', blank=True, null=True)
	events = models.CharField(max_length=200, blank=True, help_text="Comma separated selected events")

	def __str__(self):
		return f"{self.first_name} {self.last_name} ({self.email})"
from django.db import models

class Ticket(models.Model):
	holder_name = models.CharField(max_length=100)
	email = models.EmailField()
	phone_number = models.CharField(max_length=20, blank=True)
	ticket_quantity = models.PositiveIntegerField(blank=True, null=True)
	total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	payment_screenshot = models.ImageField(upload_to='payment_screenshots/', blank=True, null=True)
	purchase_date = models.DateTimeField(auto_now_add=True)
	seat_number = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return f"{self.holder_name}"


# Form submission model
from django.db import models

class Participant(models.Model):
	CATEGORY_CHOICES = [
		('Singing', 'Singing'),
		('Dance', 'Dance'),
		('Music Instrument', 'Music Instrument'),
		('Others', 'Others'),
	]

	name = models.CharField(max_length=100)
	AGE_CHOICES = [
		('5-10', '5 Yrs to 10 Yrs'),
		('11-20', '11 Yrs to 20 Yrs'),
		('21-40', '21 Yrs to 40 Yrs'),
		('41+', '41 Yrs and Above'),
	]
	age = models.CharField(max_length=10, choices=AGE_CHOICES, blank=True, null=True)
	image = models.ImageField(upload_to='participants/', blank=True, null=True)
	category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Others')
	city = models.CharField(max_length=100, blank=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

