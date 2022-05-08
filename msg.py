from email import message
import requests
from twilio.rest import Client

API_TOKEN="6e96cbd2ae39a896774d9fe263332211"
API_SID="ACc353cc13386e614b9e7355593eb86e87"
PHN_NO='+18455168530'


client = Client(API_SID, API_TOKEN)
def sendsms(phn,name,nis):
 message = client.messages \
                .create(
                     body=f'''\nHey {name}! \n 
                     
Thanks for registering with Cultyvate. 

The information about the weather forecast is as follows:
Max Temperature: {nis["tempmax"]}
Min Temperature: {nis["tempmin"]}
Humidity:{nis["humidity"]}
Chances of rain: 95%
Wind speed: 1.83
Pressure:{nis["pres"]}

As predicted by our forecast, the chances of rain is more than 80 %. So, you don't have to water your crop to ensure a healthy harvest. 

Thank you 
Team Cultyvate
Cultivating Ideas for your Growth
                     
                     ''',
                     from_=PHN_NO,
                     to=phn
                 )



