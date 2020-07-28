def centuryFromYear(year):
    year_str = str(year)

    if len(year_str) == 4:

        first_half = year_str[:2]
        sec_half = year_str[2:]

        if int(sec_half) == 0:
            return int(first_half)
        else:
            return int(first_half) + 1

    if len(year_str) == 3:
        first_pos = year_str[:1]
        last_bit = year_str[1:]

        if int(last_bit) == 0:
            return int(first_pos)
        else:
            return int(first_pos) + 1

    if len(year_str) <= 2:
        return 1
