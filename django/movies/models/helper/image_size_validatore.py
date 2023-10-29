from django.core.exceptions import ValidationError



def validate_image_size(value):
    max_size_mb = 10  # Maximum size in megabytes (100 MB)

    if value.size >= max_size_mb * 1024 * 1024:
        raise ValidationError(f"Video size should not exceed {max_size_mb} MB or larger.")