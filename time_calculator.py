

def am_pm_checker(days_passed, daytime, st_hours, st_mins, duration_hours, duration_mins):
    # single day switch
    if 12 >= duration_hours >= 0:
        duration_hours_timer = duration_hours
        # check if minutes add up to an extra hour
        if st_mins + duration_mins > 60:
            duration_hours_timer +=1
        if daytime == "AM" and st_hours+duration_hours_timer >= 12:
            daytime = "PM"
        elif daytime == "PM" and st_hours + duration_hours_timer >= 12:
            daytime = "AM"
            days_passed += 1
    # switch after +1 days
    if st_hours + duration_hours > 24:
        days_passed += int(duration_hours / 24)
        rest_hour = duration_hours % 24

        if rest_hour != 0:  # no rest_hours means just a day passed and no hours to add after it
            if daytime == "AM" and st_hours + rest_hour >= 12:
                daytime = "PM"
            elif daytime == "PM" and st_hours + rest_hour >= 12:
                daytime = "AM"
                days_passed += 1
        else:
            daytime, days_passed = am_pm_checker(days_passed, daytime, st_hours, st_mins, rest_hour, duration_mins)
    return daytime, days_passed


def hour_min_typing(st_hours, st_mins, duration_hours, duration_mins):
    rest_hour = duration_hours % 24
    if st_hours + duration_hours > 24:
        if st_hours + rest_hour > 13:
            st_hours += (rest_hour - 12)
        else:
            st_hours = st_hours + rest_hour
        if st_mins + duration_mins < 60:   # checks spare mins
            st_mins += duration_mins
        elif st_mins + duration_mins > 60:
            st_hours += 1
            st_mins = (st_mins + duration_mins) - 60
            st_mins = "0" + str(st_mins) if st_mins < 10 else st_mins
        else:
            st_mins = st_mins+duration_mins
            st_mins ="0" + str(st_mins) if st_mins < 10 else st_mins
    else:
        if st_hours+duration_hours >= 13:
            st_hours = (st_hours+duration_hours)-12
        else:
            st_hours = st_hours + duration_hours
        if st_mins+duration_mins > 60:
            st_hours += 1
            st_mins = (st_mins + duration_mins) - 60
            st_mins = "0" + str(st_mins) if st_mins < 10 else st_mins
        else:
            st_mins = st_mins + duration_mins
            st_mins = "0" + str(st_mins) if st_mins < 10 else st_mins
    return st_hours, st_mins


def weekday_checker(days_passed, weekday):
    weeday_list = {"monday": 1,
                   "tuesday": 2,
                   "wednesday": 3,
                   "thursday": 4,
                   "friday": 5,
                   "saturday": 6,
                   "sunday": 7}
    # same week day
    if weekday.lower() in weeday_list:
        day_number = weeday_list.get(weekday.lower())
    if day_number+days_passed <= 7:
        weekday = list(weeday_list.keys())[list(weeday_list.values()).index(day_number+days_passed)]
    # past week day
    elif ((day_number+days_passed) % 7) != 0:
        weekday = list(weeday_list.keys())[list(weeday_list.values()).index((day_number+days_passed) % 7)]
    return weekday.capitalize()


def add_time(*args):
    if len(args) == 3:
        weekday = args[2]
    start_time = args[0]
    duration = args[1]

    st_hours = int(start_time.split(":")[0])
    st_mins = int(start_time.split(":")[1].split(" ")[0])
    daytime = start_time.split(":")[1].split(" ")[1]

    duration_hours = int(duration.split(":")[0])
    duration_mins = int(duration.split(":")[1])

    days_passed = 0
    daytime, days_passed = am_pm_checker(days_passed, daytime, st_hours, st_mins, duration_hours, duration_mins)
    st_hours, st_mins = hour_min_typing(st_hours, st_mins, duration_hours, duration_mins)
    if len(args) == 3:
        weekday_final = weekday_checker(days_passed, weekday)

    if days_passed == 0:
        if len(args) == 3:
            return f"{st_hours}:{st_mins} {daytime}, {weekday_final}"
        else:
            return f"{st_hours}:{st_mins} {daytime}"
    elif days_passed == 1:
        if len(args) == 3:
            return f"{st_hours}:{st_mins} {daytime}, {weekday_final} (next day)"
        else:
            return f"{st_hours}:{st_mins} {daytime} (next day)"
    elif days_passed > 1:
        if len(args) == 3:
            return f"{st_hours}:{st_mins} {daytime}, {weekday_final} ({days_passed} days later)"
        else:
            return f"{st_hours}:{st_mins} {daytime} ({days_passed} days later)"
