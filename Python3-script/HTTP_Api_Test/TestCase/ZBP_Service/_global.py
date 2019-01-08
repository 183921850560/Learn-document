# coding=utf-8
import re
import os
import random
from Lib.read_yml import ReadYml
import datetime
headers = {
    "User-Agent": "Mozilla/6.0 ",
    "Content-Type": "application/x-www-form-urlencoded"
}

host = "192.168.4.72"
timeout = 15

err_code = '^(\d+\#){4}$'


def get_elevatorIds(elevatorIds, num):
    data = random.sample(elevatorIds, num)
    return data


def get_elevatorId(elevatorIds):
    return random.sample(elevatorIds, 1)[0]


date_format = {
    "day": "%Y%m%d",
    "month": "%Y%m"
}


def get_day(day, _format="day"):
    if _format == "m" or _format == "M":
        _format = "month"
        day = day * 30
    elif _format == "d" or _format=="D":
        _format = "day"
    return (datetime.datetime.now()-datetime.timedelta(days=day)).strftime(date_format[_format])

