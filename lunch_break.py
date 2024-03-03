from math import ceil

series_name = input()
series_length = int(input())
break_length = int(input())

lunch_break = break_length / 8
leisure_break = break_length / 4

time_taken = series_length + leisure_break + lunch_break
time_left = break_length - time_taken

if time_left >= 0:
    print(f"You have enough time to watch {series_name} and left with {ceil(time_left)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(abs(time_left))} more minutes.")