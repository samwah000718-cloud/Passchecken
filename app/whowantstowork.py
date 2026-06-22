with open("Anstälda.csv", "r", encoding="utf-8") as file:
    data = file.read()
with open("week.csv", "r", encoding="utf-8") as file:
    data = file.read()
let = openweek = "12:00, 20:00"
let = openweekend = "12:00, 23:00"
print("On the weekend we open at " + openweekend + " and on the weekdays we open at " + openweek)
