from email import message
import requests
from twilio.rest import Client

API_TOKEN="45d2ddc00e6f8b0bfda5dc99ed36ac35"
API_SID="ACc353cc13386e614b9e7355593eb86e87"
PHN_NO='+18455168530'


client = Client(API_SID, API_TOKEN)
def sendsms(phn,name):
 message = client.messages \
                .create(
                     body=f"\nHey {name}! \n You have made one step closer to your safety by making the right choice\n Thank you for registring up with Clade Alerta Your safety is our priority",
                     from_=PHN_NO,
                     to=phn
                 )



