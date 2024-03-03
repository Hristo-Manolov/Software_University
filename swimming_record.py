DELAY_DISTANCE = 15
DELAY_SECONDS = 12.5

record_seconds = float(input())
distance = float(input())
swimming_seconds = float(input())

delay = (distance // DELAY_DISTANCE) * DELAY_SECONDS

final_time = (distance * swimming_seconds) + delay

if final_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {final_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {final_time - record_seconds :.2f} seconds slower.")