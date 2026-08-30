# late_fee.py
import config


def calculate_late_fee(days_late):
    fee = days_late * config.RATE_PER_DAY
    return min(fee, config.MAX_FEE)


if __name__ == '__main__':
    for d in (0, 1, 3, 50, 100):
        print(d, 'days late ->', calculate_late_fee(d))
