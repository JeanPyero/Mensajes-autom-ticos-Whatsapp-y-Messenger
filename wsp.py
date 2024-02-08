#import the requests library
import requests
#Whatsapp official API URL (Facebook for developers)
#url = YOUR_TOKEN (generate it on your own, to be sure)
url = "https://graph.facebook.com/v18.0/233608479832225/messages"
#Using the token generated in Facebook for developers (Facebook Business Manager)
headers = {
    #Bearer YOUR_TOKEN (valid for 24 hours)
    "Authorization": "Bearer EAAPX2jmeHNsBOyTyEVLyH6ZAoUWN26nOHWeJ06o8gDLo1JrjoZBtPdUt7vJhfoZBt4fHcg6LHn8otKDZCPhQ7IaBOZAqfqcvLHSaWAA9POw1RNWkh7v0kQfQvZBejKgAleS7lvjAbzJaRZCYipnxOB88kZAqugoZAZAHFAZCJmoMLA0ZB4VHcJ2x6gwZBiUZAngOTRNbKLnH8ZAeGNEJ3cKZC46XsICX",
    "Content-Type": "application/json",
}
#indicate the number to send, and the template with the message (written in FacebookBusinessManager)
data = {
    "messaging_product": "whatsapp",
    "to": "51998320568",
    "type": "template",
    "template": {
        #name: YOUR_TEMPLATE (by default, hello_world)
        "name": "auto",
        #languague: YOUR_LANGUAGE (by default, en_US)
        "language": {"code": "es_ES"},
    }
}
#request the POST to the defined url
response = requests.post(url, json=data, headers=headers)
#print the status of the message
print(response.status_code)
print(response.json())