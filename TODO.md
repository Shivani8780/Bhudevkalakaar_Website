# TODO: Implement Participants Profile Page with Filters

## Completed Tasks
- [x] Update Participant model to add category and city fields
- [x] Create database migration for new fields
- [x] Update main/admin.py ParticipantAdmin to use ('name', 'category', 'city', 'image') in list_display and fields
- [x] Update participants_profiles.html template to add category filter buttons, city dropdown, and JavaScript for client-side filtering
- [x] Ensure grid layout shows 3-4 cards per row

## Next Steps
- [ ] Run database migrations: `python manage.py makemigrations` and `python manage.py migrate`
- [ ] Test the new participants profile page with filters
- [ ] Populate sample data for participants with categories and cities
- [ ] Verify filtering works correctly on the frontend

## Notes
- Category choices: Singing, Dance, Music Instrument, Others
- Client-side filtering implemented with JavaScript
- Grid is responsive with 3-4 cards per row
- City dropdown appears after selecting a category
