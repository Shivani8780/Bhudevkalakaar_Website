from django.contrib import admin
from .models import OtherPlaceEvent
from .models import ContactMessage, Participant

@admin.register(OtherPlaceEvent)
class OtherPlaceEventAdmin(admin.ModelAdmin):
	list_display = ('title', 'event_datetime', 'location')
from django.contrib import admin
from .models import Ticket, UserFormData, HomePageImage, PastEvent, Photo, ContactMessage
# ...existing code...

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'message', 'created_at')


# Custom Age Filter for Participant
from django.utils.translation import gettext_lazy as _

class AgeRangeFilter(admin.SimpleListFilter):
	title = _('Age')
	parameter_name = 'age_range'

	def lookups(self, request, model_admin):
		return [
			('5-10', _('5 Yrs to 10 Yrs')),
			('11-20', _('11 Yrs to 20 Yrs')),
			('21-40', _('21 Yrs to 40 Yrs')),
			('41+', _('41 Yrs and Above')),
		]

	def queryset(self, request, queryset):
		value = self.value()
		if value == '5-10':
			return queryset.filter(age__gte=5, age__lte=10)
		elif value == '11-20':
			return queryset.filter(age__gte=11, age__lte=20)
		elif value == '21-40':
			return queryset.filter(age__gte=21, age__lte=40)
		elif value == '41+':
			return queryset.filter(age__gte=41)
		return queryset

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
	list_display = ('name', 'age', 'category', 'city', 'image')
	fields = ('name', 'age', 'category', 'city', 'image')
	list_filter = ('age', AgeRangeFilter)

@admin.register(UserFormData)
class UserFormDataAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email', 'phone_number', 'ticket_quantity', 'total_amount', 'events', 'payment_screenshot')
	search_fields = ('first_name', 'last_name', 'email', 'phone_number')
	ordering = ['-id']

@admin.register(HomePageImage)
class HomePageImageAdmin(admin.ModelAdmin):
	list_display = ('title', 'image')

@admin.register(PastEvent)
class PastEventAdmin(admin.ModelAdmin):
	list_display = ('title', 'image')
	fields = ('title', 'image')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
	list_display = ('caption', 'image', 'uploaded_at')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	list_display = ('holder_name', 'email', 'phone_number', 'ticket_quantity', 'total_amount', 'payment_screenshot', 'purchase_date')
	search_fields = ('holder_name', 'email', 'phone_number')

