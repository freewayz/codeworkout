from django.test import TestCase
import  unittest
from  api import *
# Create your tests here.




class ApiTestCase(TestCase):

    def setUp(self):
        self.paypalApi = PayPalApi()

    def test_that_access_token_is_gotten(self):
        token = self.paypalApi.test_paypal_api_access_token()
        self.assertIsNotNone(token, "Access token is not gotten")

    def test_that_paypal_payment_recv_ok_status(self):
        status = self.paypalApi.test_paypal_payment_with_info()
        self.assertEqual(status, 200, "Status is not ok")



class IndexPageView(TestCase):


    def setUp(self):
        pass



