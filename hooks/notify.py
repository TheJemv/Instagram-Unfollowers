import requests
import os
from datetime import datetime
def callNotify(new_users):
     """
     new_users: set[str]
     """

     print("🚨 NUEVOS QUE NO TE SIGUEN:")
     for u in new_users:
          print(f"https://www.instagram.com/{u}/")


     now = datetime.now().strftime("%Y-%m-%d %H:%M")
     if not new_users:
          return
     else:
          users = "\n".join(
               f"• [**{user}**](https://www.instagram.com/{user}/)"
               for user in new_users
          )
          embed = {
               "title": "🚨 Unfollowers detectados",
               "description": users,
               "color": 0xED4245,  # rojo
               "footer": {
                    "text": f"{len(new_users)} usuarios · {now}"
               }
          }
        
     payload = {
          "username": "Instagram Tracker",
          "embeds": [embed],
          "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Instagram_icon.png/500px-Instagram_icon.png" 
     }
     
     response = requests.post(os.environ["DISCORD_WEBHOOK"], json=payload)
     if response.status_code not in (200, 204):
          print("Error enviando webhook:", response.text)