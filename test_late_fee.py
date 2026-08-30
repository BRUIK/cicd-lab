from late_fee import calculate_late_fee


def test_no_late_days():
    assert calculate_late_fee(0) == 0


def test_one_day_late():
    assert calculate_late_fee(1) == 10


def test_two_days_late():
    assert calculate_late_fee(2) == 20


def test_three_days_late():
    assert calculate_late_fee(3) == 30


def test_seven_days_late():
    assert calculate_late_fee(7) == 70


def test_nine_days_late_just_below_threshold():
    assert calculate_late_fee(9) == 90


def test_ten_days_late_hits_cap():
    assert calculate_late_fee(10) == 500


def test_twelve_days_late_still_capped():
    assert calculate_late_fee(12) == 500


def test_thirteen_days_late_still_capped():
    assert calculate_late_fee(13) == 500


def test_twenty_days_late_still_capped():
    assert calculate_late_fee(20) == 500


def test_fifty_days_late_still_capped():
    assert calculate_late_fee(50) == 500


def test_hundred_days_late_still_capped():
    assert calculate_late_fee(100) == 500
