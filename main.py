import time
from dotenv import load_dotenv
import os

from session import create_session
from services.instagram import graphql_request
from utils.compare import users_not_following_back
from utils.storage import load_previous, save_current
from hooks.notify import callNotify

load_dotenv()
def main():
    session = create_session()
    ds_user_id = session.cookies.get("ds_user_id")

    print("👀 Instagram watcher iniciado")
    while True:
        try:
            print("🔄 Comprobando...")

            followers = graphql_request(
                session,
                os.environ["FOLLOWERS_QUERY_HASH"],
                ds_user_id,
                "edge_followed_by"
            )

            following = graphql_request(
                session,
                os.environ["FOLLOWING_QUERY_HASH"],
                ds_user_id,
                "edge_follow"
            )

            current = users_not_following_back(followers, following)
            previous = load_previous(os.environ["DATA_FILE"])

            new_users = current - previous

            if new_users:
                callNotify(new_users)

            save_current(os.environ["DATA_FILE"], current)

        except Exception as e:
            print("❌ Error:", e)

        print("⏳ Esperando 5 minutos...\n")
        time.sleep(int(os.environ["CHECK_INTERVAL"]))


if __name__ == "__main__":
    main()
