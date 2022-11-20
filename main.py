import requests

url = "https://email-api.myworldbox.repl.co"

data = {
"sender_name": "your_name",
"sender_email": "your_email@gmail.com",
  
"receiver_name": "receiver_name",  
"receiver_email": "receiver_name@gmail.com",
  
"title": "title",
"message": "message"
}

print("[Email send]: " , requests.post(url, json=data))
