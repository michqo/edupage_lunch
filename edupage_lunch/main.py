import sys, os
from dotenv import load_dotenv
from .utils import EdupageUser
from .order import order_lunch

if __name__ == "__main__":
    load_dotenv(".env")

    weeks_count = 1  # Number of weeks to order lunch for
    username = os.getenv("EDUPAGE_USERNAME")
    password = os.getenv("EDUPAGE_PASSWORD")
    subdomain = os.getenv("EDUPAGE_SUBDOMAIN")

    if username == None or password == None or subdomain == None:
        print("Set env variables")
        sys.exit(1)
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        weeks_count = int(sys.argv[1])

    user = EdupageUser(username, password, subdomain)
    print("Ordering lunch...")
    try:
        order_lunch(user, weeks_count)
        print("Successfully ordered lunch")
    except Exception as e:
        print(f"Error occured while ordering lunch: {e}")
