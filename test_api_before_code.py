

import os
import requests
from requests.auth import HTTPBasicAuth


# print "Getting paystack SL %s" % os.getenv('PAYSTACK_SK')



def test_paystack():
    paystack_url = 'https://api.paystack.co/transaction/initialize'
    paystack_payload = {
        'reference': '7PVGX8MEk85tgeEpVDtD',
        'amount': '500000',
        'email': 'fr33wayz@gmil.com'
    }
    headers = {
        'Authorization': 'Bearer ' + os.getenv('PAYSTACK_SK'),
        'Content-Type': 'application/json'
    }

    paystack_response = requests.post(paystack_url, data=paystack_payload, headers=headers)
    print paystack_response.content


class PayPalApi:
    def __init__(self):
        # run the get access toeke
        self.test_paypal_api_access_token()

    def test_paypal_api_access_token(self):
        url = "https://api.sandbox.paypal.com/v1/oauth2/token"
        payload = {
            "grant_type": "client_credentials"
        }

        http_headers = {
            "Accept": "application/json",
            "Accept-Language": "en_US"
        }
        client_id = os.getenv('PAYPAL_CLIENT_ID')
        secret_key = os.getenv('PAYPAL_SK')

        paypal_response = requests.post(url, data=payload, headers=http_headers,
                                        auth=HTTPBasicAuth(client_id, secret_key))
        print "getting paypal access token...."
        print paypal_response.json()
        # get the access_token url
        self.access_token = paypal_response.json()['access_token']
        print "Access token is %s" % self.access_token

    def test_paypal_payment(self):
        url = "https://api.sandbox.paypal.com/v1/payments/payment"
        http_header = {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + self.access_token
        }

        payload = {
            "intent": "sale",
            "redirect_urls": {
                "return_url": "http://example.com/your_redirect_url.html",
                "cancel_url": "http://example.com/your_cancel_url.html"
            },
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [
                {
                    "amount": {
                        "total": "7.47",
                        "currency": "USD"
                    }
                }
            ]
        }

        print "getting payment response ..... "
        paypal_payment_response = requests.post(url, data=payload, headers=http_header)
        print paypal_payment_response.json()


payPalApi = PayPalApi()
payPalApi.test_paypal_payment()
