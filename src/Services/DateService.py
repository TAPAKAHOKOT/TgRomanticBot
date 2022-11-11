import datetime as dt


class DateService:
    @staticmethod
    def get_seconds_left(datetime_to_count: dt.datetime, hours: int) -> int:
        return int(hours * 3600 - (dt.datetime.today() - datetime_to_count).total_seconds())

    @staticmethod
    def seconds_to_str(seconds: int) -> str | None:
        if seconds <= 0:
            return None

        h = seconds // 3600
        m = (seconds - h * 3600) // 60
        s = seconds - h * 3600 - m * 60

        return f'{h}:{m}:{s}'
