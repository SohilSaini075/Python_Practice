# Write a program to convert given seconds into hours, minutes and remaining seconds.

Total_Seconds = int(input("Enter total seconds: "))

Hours = Total_Seconds // 3600
Minutes = (Total_Seconds % 3600) // 60
Seconds = Total_Seconds % 60
print(Hours, "hours", Minutes, "minutes", Seconds, "seconds")
