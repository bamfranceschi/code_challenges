def lateRide(n):
    hours = n // 60  # gives us the floor int of hours
    minutes = n % 60  # gives us the leftover value of minutes

    hours_str = str(hours)
    minutes_str = str(minutes)

    all_together = hours_str + minutes_str

    sum_time = 0

    for char in all_together:
        sum_time += int(char)

    return sum_time
