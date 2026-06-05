import os
import stripe

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")

conn = sqlite3.connect("cita.db", check_same_thread=False)
cur = conn.cursor()


def make_vip(user_id):
    cur.execute("UPDATE users SET plan='vip' WHERE user_id=?", (user_id,))
    conn.commit()


def handle_event(payload, sig, endpoint_secret):

    event = stripe.Webhook.construct_event(
        payload, sig, endpoint_secret
    )

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        user_id = session["metadata"]["user_id"]

        make_vip(user_id)

        print("💳 VIP ACTIVATED:", user_id)

    return True
