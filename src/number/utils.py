from .models import MagicNumber


def get_magic_number():
    magic_numbers = MagicNumber.objects.all()
    magic_number = magic_numbers.first() if magic_numbers.exists() else None
    return magic_number
