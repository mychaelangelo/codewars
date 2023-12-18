def past(h, m, s):
    if h in range(0,24) and m in range(0,60) and s in range(0,60):
        total_mins = (h * 60) + m
        total_seconds = (total_mins * 60) + s
        return total_seconds * 1000

    