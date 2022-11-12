import datetime as dt

from pytz import timezone


class DateService:
    @staticmethod
    def get_seconds_left(datetime_to_count: dt.datetime, hours: int) -> int:
        return int(hours * 3600 - (dt.datetime.today() - datetime_to_count).total_seconds())

    @staticmethod
    def get_seconds_until_end_of_day() -> int:
        now_date = dt.datetime.now(timezone('Europe/Moscow'))
        return int(((24 - now_date.hour - 1) * 60 * 60) + ((60 - now_date.minute - 1) * 60) + (60 - now_date.second))

    @staticmethod
    def seconds_to_str(seconds: int) -> str | None:
        if seconds <= 0:
            return None

        format_num = lambda n: n if len(str(n)) == 2 else '0' + str(n)

        h = seconds // 3600
        m = (seconds - h * 3600) // 60
        s = seconds - h * 3600 - m * 60

        return f'{format_num(h)}:{format_num(m)}:{format_num(s)}'
