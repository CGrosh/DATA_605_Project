from date_util import time_cleaner

def test_time_cleaner_before_8():
    cleaned = time_cleaner('2021-05-12 07:30:22')

    assert cleaned == '2021-05-12 19:30:22'

def test_time_cleaner_after_8():
    cleaned = time_cleaner('2021-05-12 09:30:22')

    assert cleaned == '2021-05-12 09:30:22'

def test_time_cleaner_at_8():
    cleaned = time_cleaner('2021-05-12 08:00:00')

    assert cleaned == '2021-05-12 08:00:00'
