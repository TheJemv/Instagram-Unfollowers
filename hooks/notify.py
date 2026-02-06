def callNotify(new_users):
    """
    new_users: set[str]
    """

    print("🚨 NUEVOS QUE NO TE SIGUEN:")
    for u in new_users:
        print(f"https://www.instagram.com/{u}/")

    # 👇 EJEMPLOS
    # send_telegram(new_users)
    # send_discord(new_users)
    # send_email(new_users)
