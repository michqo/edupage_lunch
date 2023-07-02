import sys, os
from dotenv import load_dotenv
from .utils import EdupageUser
from .order import order_weeks

load_dotenv()

WEEKS_COUNT = 2  # How many weeks to order lunch for
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
subdomain = os.getenv("SUBDOMAIN")

if username == None or password == None or subdomain == None:
    print("Set env variables")
    sys.exit(1)

user = EdupageUser(username, password, subdomain)

print("Ordering lunch...")
try:
    order_weeks(user, WEEKS_COUNT)
    print("Successfully ordered lunch")
except:
    print("Error occured while ordering lunch")
