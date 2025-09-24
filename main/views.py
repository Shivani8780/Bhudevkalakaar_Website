def infopage(request):
	return render(request, 'Infopage.html')
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from .models import ContactMessage

# ...existing code...

@csrf_exempt
@require_POST
def submit_contact_form(request):
	name = request.POST.get('name', '')
	email = request.POST.get('email', '')
	message = request.POST.get('message', '')
	if not (name and email and message):
		return JsonResponse({'success': False, 'error': 'All fields are required.'}, status=400)
	ContactMessage.objects.create(name=name, email=email, message=message)
	return JsonResponse({'success': True, 'message': 'Thank you for contacting us!'})
# Ticket purchase form submission view
@csrf_exempt  # For demonstration; use Django's form system for production
@require_POST
def submit_ticket_form(request):
	first_name = request.POST.get('first_name', '')
	last_name = request.POST.get('last_name', '')
	email = request.POST.get('email', '')
	phone_number = request.POST.get('phone_number', '')
	ticket_quantity = int(request.POST.get('ticket_quantity', 1))
	total_amount = request.POST.get('total_amount', '50.00')
	payment_screenshot = request.FILES.get('payment_screenshot') or request.FILES.get('paymentScreenshot')
	import logging
	logger = logging.getLogger('django')
	logger.info(f"Form submission received: first_name={first_name}, last_name={last_name}, email={email}, phone_number={phone_number}, ticket_quantity={ticket_quantity}, total_amount={total_amount}, payment_screenshot={payment_screenshot}")

	first_name = request.POST.get('first_name', '')
	last_name = request.POST.get('last_name', '')
	email = request.POST.get('email', '')
	phone_number = request.POST.get('phone_number', '')
	ticket_quantity = int(request.POST.get('ticket_quantity', 1))
	total_amount = request.POST.get('total_amount', '50.00')
	payment_screenshot = request.FILES.get('payment_screenshot') or request.FILES.get('paymentScreenshot')

	if not (first_name and phone_number):
		return JsonResponse({'success': False, 'error': 'Missing required fields'}, status=400)

	from .models import Ticket
	Ticket.objects.create(
		holder_name=f"{first_name} {last_name}",
		email=email,
		phone_number=phone_number,
		ticket_quantity=ticket_quantity,
		total_amount=total_amount,
		payment_screenshot=payment_screenshot
	)
	from django.shortcuts import redirect
	return redirect('/confirmation/')
from django.shortcuts import render
from .models import Ticket, UserFormData, HomePageImage, PastEvent, Photo
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
@csrf_exempt  # For demonstration; use Django's form system for production
@require_POST
def submit_form(request):

	first_name = request.POST.get('first_name')
	last_name = request.POST.get('last_name', '')
	email = request.POST.get('email', '')
	phone_number = request.POST.get('phone_number')
	ticket_quantity = int(request.POST.get('ticket_quantity', 1))
	total_amount = request.POST.get('total_amount', '50.00')
	payment_screenshot = request.FILES.get('payment_screenshot') or request.FILES.get('paymentScreenshot')
	events = request.POST.getlist('events[]')
	events_str = ', '.join(events)

	if not (first_name and phone_number and email):
		return JsonResponse({'success': False, 'error': 'Missing required fields'}, status=400)

	# Save all form fields to UserFormData model
	from .models import UserFormData
	UserFormData.objects.create(
		first_name=first_name,
		last_name=last_name,
		email=email,
		phone_number=phone_number,
		ticket_quantity=ticket_quantity,
		total_amount=total_amount,
		payment_screenshot=payment_screenshot,
		events=events_str
	)

	from django.shortcuts import redirect
	return redirect('confirmation')

def confirmation(request):
	return render(request, 'confirmation.html')

def index(request):
	homepage_images = HomePageImage.objects.all()
	photos_list = Photo.objects.all().order_by('-uploaded_at')
	from .models import OtherPlaceEvent
	other_events = OtherPlaceEvent.objects.filter(event_datetime__gte=timezone.now()).order_by('event_datetime')

	# Pagination for photos
	from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
	page = request.GET.get('page', 1)
	paginator = Paginator(photos_list, 12)  # 12 photos per page
	try:
		photos = paginator.page(page)
	except PageNotAnInteger:
		photos = paginator.page(1)
	except EmptyPage:
		photos = paginator.page(paginator.num_pages)

	return render(request, 'index.html', {
		'homepage_images': homepage_images,
		'photos': photos,
		'other_events': other_events,
		'paginator': paginator,
		'page_obj': photos,
	})
    
def participant_profile(request):
	from .models import Participant
	participants_list = Participant.objects.all()
	from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
	page = request.GET.get('page', 1)
	paginator = Paginator(participants_list, 12)  # 12 participants per page
	try:
		participants = paginator.page(page)
	except PageNotAnInteger:
		participants = paginator.page(1)
	except EmptyPage:
		participants = paginator.page(paginator.num_pages)

	return render(request, 'participants_profiles.html', {
		'participants': participants,
		'paginator': paginator,
		'page_obj': participants,
	})

def past_events(request):
	past_events_list = PastEvent.objects.all().order_by('-id')
	from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
	page = request.GET.get('page', 1)
	paginator = Paginator(past_events_list, 12)  # 12 events per page
	try:
		past_events = paginator.page(page)
	except PageNotAnInteger:
		past_events = paginator.page(1)
	except EmptyPage:
		past_events = paginator.page(paginator.num_pages)

	return render(request, 'past-events.html', {
		'past_events': past_events,
		'paginator': paginator,
		'page_obj': past_events,
	})

def photos(request):
	photos_list = Photo.objects.all().order_by('-uploaded_at')
	from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
	page = request.GET.get('page', 1)
	paginator = Paginator(photos_list, 12)  # 12 photos per page
	try:
		photos = paginator.page(page)
	except PageNotAnInteger:
		photos = paginator.page(1)
	except EmptyPage:
		photos = paginator.page(paginator.num_pages)

	return render(request, 'photos.html', {
		'photos': photos,
		'paginator': paginator,
		'page_obj': photos,
	})

def contact(request):
	return render(request, 'contact.html')

def get_tickets(request):
	return render(request, 'get-tickets.html')

def audience(request):
	return render(request, 'audience.html')

def participant_form(request):
	return render(request, 'participantForm.html')

def event_list(request):
	# Event model removed; this view is now obsolete or should be updated
	return render(request, 'event_list.html', {'events': []})

def ticket_list(request):
	tickets = Ticket.objects.select_related('event').order_by('-purchase_date')
	return render(request, 'ticket_list.html', {'tickets': tickets})

