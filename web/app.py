from flask import Flask, request
import os
import stripe
import sqlite3

app = Flask(__name__)

stripe.api_key = os.environ.get("STRIPE_SECRET_KEY")
endpoint_secret = os.environ.get("STRIPE_WEBHOOK_SECRET")

conn = sqlite3.connect("cita.db", check_same_thread=False)
cur = conn.cursor()


def activate_vip(user_id):
    cur.execute("UPDATE users SET plan='vip' WHERE user_id=?", (user_id,))
    conn.commit()


@app.route("/webhook", methods=["POST"])
def webhook():
    payload = request.data
    sig_header = request.headers.get("Stripe-Signature")

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except Exception as e:
        return str(e), 400

    # 💳 payment success
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        user_id = session["metadata"].get("user_id")

        if user_id:
            activate_vip(user_id)
            print("✅ VIP ACTIVATED:", user_id)

    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
