from django.urls import path
from .views import MagicNumberView

app_name = 'number'

urlpatterns = [
    path('', MagicNumberView.as_view(), name='magic-number'),
]
