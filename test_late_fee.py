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


def test_ten_days_late():
    assert calculate_late_fee(10) == 100


def test_twenty_days_late():
    assert calculate_late_fee(20) == 200


def test_thirty_four_days_late():
    assert calculate_late_fee(34) == 340


def test_forty_nine_days_late_just_below_cap():
    assert calculate_late_fee(49) == 490


def test_fifty_days_late_hits_cap_exactly():
    assert calculate_late_fee(50) == 500


def test_fifty_seven_days_late_still_capped():
    assert calculate_late_fee(57) == 500


def test_hundred_days_late_still_capped():
    assert calculate_late_fee(100) == 500
