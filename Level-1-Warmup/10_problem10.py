# Write a program to read seconds and convert them into hours, minutes and seconds.

seconds = 3670

hour = int(seconds/3600)
rem_minute = seconds % 3600
minute = int(rem_minute / 60)
rem_seconds = seconds % 60
print(f"{seconds} seconds is equal to {hour} hours, {minute} minute and {rem_seconds} seconds.")