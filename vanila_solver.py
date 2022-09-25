def get_last_max(data):
    max_val = float('-inf')
    pos = None
    for n, el in enumerate(data):
        if max_val <= el:
            pos = n
            max_val = el
    return max_val, pos


def get_first_min(data):
    min_val = float('inf')
    pos = None
    for n, el in enumerate(data):
        if min_val > el:
            pos = n
            min_val = el
    return min_val, pos


def get_stat(data):
    min_val = float('inf')
    pos_min = None
    max_val = float('-inf')
    pos_max = None
    for n, el in enumerate(data):
        if min_val > el:
            pos_min = n
            min_val = el
        if max_val <= el:
            pos_max = n
            max_val = el
    return (min_val, pos_min), (max_val, pos_max)


def accumulate_min(data):
    last_val = None
    for val in data:
        if last_val is not None:
            val = val if val < last_val else last_val
        yield val
        last_val = val


def accumulate_max(data):
    last_val = None
    for val in data:
        if last_val is not None:
            val = val if val > last_val else last_val
        yield val
        last_val = val


def get_max_profit(stock_prices_yesterday):
    if not stock_prices_yesterday:
        return None

    (min_val, pos_min), (max_val, pos_max) = get_stat(stock_prices_yesterday)
    if pos_min <= pos_max:
        return max_val - min_val

    start = min(pos_max, pos_min)
    end = max(pos_max, pos_min)

    acc_min = tuple(val for n, val in enumerate(accumulate_min(stock_prices_yesterday[:pos_min + 1])) if n >= start)
    acc_max = tuple(accumulate_max(reversed(stock_prices_yesterday[pos_max:])))[::-1]

    max_res = float('-inf')
    for max_v, min_v in zip(acc_max, acc_min):
        max_res = max(max_v - min_v, max_res)

    return max_res


if __name__ == '__main__':
    stock_prices_yesterday = [9, 2, 12, 4, 1, 3, 8, 6, 11]
    res = get_max_profit(stock_prices_yesterday)
    print(res)
