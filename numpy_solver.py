import numpy as np


def get_type(x):
    if x < 256:
        return 'uint8'
    elif x < 65536:
        return 'uint16'
    elif x < 4294967296:
        return 'uint32'
    elif x < 18446744073709551616:
        return 'uint64'
    else:
        raise Exception('The number is too large')


def get_last_max(data):
    max_val = data.max()
    pos = data.shape[0] - np.flip(data).argmax() - 1

    return max_val, pos


def get_first_min(data):
    min_val = data.min()
    pos = data.argmin()

    return min_val, pos


def accumulate_min(data):
    return np.minimum.accumulate(data)


def accumulate_max(data):
    return np.maximum.accumulate(data)


def get_max_profit(stock_prices_yesterday):
    if stock_prices_yesterday.shape[0] == 0:
        return None

    (max_val, pos_max) = get_last_max(stock_prices_yesterday)
    (min_val, pos_min) = get_first_min(stock_prices_yesterday)
    if pos_min <= pos_max:
        return max_val - min_val

    start = min(pos_max, pos_min)
    end = max(pos_max, pos_min)

    acc_min = accumulate_min(stock_prices_yesterday[:pos_min + 1])
    acc_max = np.flip(accumulate_max(np.flip(stock_prices_yesterday[pos_max:])))

    res = (acc_max[:end + 1 - start] - acc_min[start:]).max()

    return res


if __name__ == '__main__':
    stock_prices_yesterday = np.array([9, 2, 12, 4, 1, 3, 8, 6, 11])
    stock_prices_yesterday = stock_prices_yesterday.astype(get_type(stock_prices_yesterday.max()))
    res = get_max_profit(stock_prices_yesterday)

    print(res)
