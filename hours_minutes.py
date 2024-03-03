BONUS_MINUTES = 15

hours = int(input())
minutes = int(input())

minutes += BONUS_MINUTES

if minutes > 59:
    hours += 1
    minutes -= 60

if hours > 23:
    hours -= 24

print(f"{hours}:{minutes:02d}")