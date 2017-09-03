def make_averager():
    count = 0
    total = 0

    def averager(newvalue):
        nonlocal count, total
        count += 1
        total += newvalue
        return total / count

    return averager
