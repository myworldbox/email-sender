import requests

url = "https://email-api.myworldbox.repl.co"

data = {
  "app_email": 'provider_email',
  "app_password": 'provider_password',
  
  "receiver_name": "receiver_name",
  "receiver_email": "receiver_email",
  
  "title": "title",
  "message": "message",
  
  "sender_name": "sender_name",
  "sender_email": "sender_email",
  
  "sender_image": "https://myworldbox.github.io/resources/images/myworldbox.jpg",
  "sender_company":"VL Blockchain",
  "sender_website": "https://myworldbox.github.io",
  "sender_copyright": "© 2021 VL Blockchain. All rights reserved.",
  
  "motto_1": "Time is precious",
  "motto_2": "So makes it counts",
}

print("[Email sent]: ", requests.post(url, json=data))
