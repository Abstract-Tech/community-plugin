from .views import send_contact_form_email
from django.urls import re_path as url


urlpatterns = [
    url(
        r"^send_contact_email$",
        send_contact_form_email,
        name="send_contact_email",
    ),
]
