import os
import stripe

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

def create_checkout(user_id):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="payment",
        line_items=[{
            "price_data": {
                "currency": "eur",
                "product_data": {
                    "name": "Cita VIP Plan"
                },
                "unit_amount": 999,
            },
            "quantity": 1,
        }],
        success_url="https://t.me/YOUR_BOT_USERNAME",
        cancel_url="https://t.me/YOUR_BOT_USERNAME",
        metadata={"user_id": str(user_id)}
    )
    return session.url
