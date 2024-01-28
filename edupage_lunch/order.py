from time import sleep
from datetime import datetime, timedelta
from edupage_api import Edupage
from .lunch import Lunch, get_boarder_id
from .utils import EdupageUser


def get_monday(date: datetime) -> datetime:
    return date + timedelta(days=(0 - date.weekday()) % 7)


def order_lunch(user: EdupageUser, weeks: int):
    edupage = Edupage()
    edupage.login(user.username, user.password, user.subdomain)
    boarder_id = get_boarder_id(edupage)

    for i in range(weeks):
        date = get_monday(datetime.now() + timedelta(weeks=i))
        lunch = Lunch(edupage, boarder_id)
        for _ in range(5):
            try:
                lunch.choose(1, date)
            except:
                pass
            date += timedelta(days=1)
            sleep(0.2)
