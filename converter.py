def converter(hour, minute, period):
    if period == "am":
        hour = hour % 12
    elif period == "pm":
        hour = (hour % 12) + 12
    else:
        print("Invalid input")

    hour_str = str(hour).zfill(2)
    minute_str = str(minute).zfill(2)
    return hour_str + minute_str

time = converter(6, 7, "am")
print(time)