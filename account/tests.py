from django.test import TestCase
import os
from dotenv import read_dotenv
# Create your tests here.
read_dotenv('../.env')
def testi():
    data = os.environ.get('EMAIL_PASS')
    envv = os.environ.get('EMAIL_USER')
    print(data, envv)

testi()