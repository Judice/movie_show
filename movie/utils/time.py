# _*_ coding: utf-8 _*_
import arrow

utcnow = arrow.utcnow


def prcnow():
    return utcnow().to('prc')


def prc_int_day(arrow_time=prcnow()):
    return int(arrow_time.format('YYYYMMDD'))


def get_year_month_day(arrow_time=prcnow()):
    date = arrow_time.date()
    return date.year, date.month, date.day


def format_arrow_time(year=get_year_month_day()[0], month=get_year_month_day()[1], day=get_year_month_day()[2]):
    return prcnow().replace(year=year, month=month, day=day)

current_year, current_month, current_day = get_year_month_day()


def to_datetime(arrow_time=prcnow()):
    return arrow_time.datetime
