import requests
import os

def create_session():
    s = requests.Session()

    s.headers.update({
        "User-Agent": "Mozilla/5.0",
        "Accept": "*/*",
        "X-IG-App-ID": "936619743392459"
    })

    # ⬇️ PEGA AQUÍ TUS COOKIES ⬇️
    s.cookies.update({
        "sessionid": os.environ["SESSIONID"],
        "ds_user_id": os.environ["DS_USER_ID"],
        "csrftoken": os.environ["CSRFTOKEN"]
    })

    return s