from .models import Alert
from django.core.mail import send_mail
from django.conf import settings


def check_alerts(product):

    alerts = Alert.objects.filter(
        product=product,
        is_triggered=False
    )

    for alert in alerts:

        if product.current_price <= alert.target_price:

            alert.is_triggered = True
            alert.save()

            send_mail(
                subject="RateRanger Price Alert",
                message=(
                    f"{product.name} has dropped to ₹{product.current_price}.\n\n"
                    f"Your target price was ₹{alert.target_price}."
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[alert.user.email],
                fail_silently=False,
            )

            print(
                f"ALERT TRIGGERED: "
                f"{product.name} "
                f"is now {product.current_price}"
            )