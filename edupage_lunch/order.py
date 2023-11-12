from time import sleep
from datetime import datetime, timedelta
from edupage_api import Edupage
from .lunch import Lunch, get_boarder_id
from .utils import EdupageUser


def getDay(date: datetime, day: int) -> datetime:
    return date + timedelta(days=(day - date.weekday()) % 7)


def order_lunch(user: EdupageUser, weeks: int):
    edupage = Edupage()
    edupage.login(user.username, user.password, user.subdomain)

    for _ in range(weeks):
        date = getDay(datetime.now() + timedelta(weeks=weeks - 1), 0)
        boarder_id = get_boarder_id(edupage, date)
        lunch = Lunch(edupage, boarder_id)
        for _ in range(5):
            try:
                lunch.choose(1, date)
            except:
                pass
            date += timedelta(days=1)
            sleep(0.2)
