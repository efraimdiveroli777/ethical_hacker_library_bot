import yookassa
from yookassa import Payment

from config import config
import uuid

def create_oplata(email, amount):

        yookassa.Configuration.account_id = config.API_ID
        yookassa.Configuration.secret_key = config.API_TOKEN

        idempotence_key = str(uuid.uuid4())
        response = Payment.create({
            "amount": {
                "value": f"{amount}",
                "currency": "RUB"
            },
            "receipt": {
                "customer": {
                    "email": f"{email}"
                },
                "items": [
                    {
                        "description": "Пополнение баланса",
                        "quantity": "1",
                        "vat_code": "1",
                        "amount": {
                            "value": f"{amount}",
                            "currency": "RUB"
                        }
                    }
                ]
            },
            "payment_method_data": {
                "type": "bank_card"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "https://t.me/SSB_yo_bot"
            },
            "description": f"Оплата на {amount} рубля",
            "capture": True
        }, idempotence_key)

        url = response.confirmation.confirmation_url

        return url, response

def oplata_check(id):
    payment = yookassa.Payment.find_one(id)
    if payment.status == 'succeeded':
        return True
    else:
        return False
