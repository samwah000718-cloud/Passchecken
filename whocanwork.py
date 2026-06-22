import csv

employees = []
logs = []

# Read employee data
with open("Anstälda.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, skipinitialspace=True)

    for row in reader:
        employee = row["employee"]
        wage = int(row["wage"])
        hours = int(row["hours"])

        total_wage = wage * hours

        message = f"{employee} earns {total_wage} kr"
        print(message)
        logs.append(message)

        if hours > 40:
            message = f"{employee} has worked more than 40 hours this week."
            print(message)
            logs.append(message)

        if hours < 20:
            message = f"{employee} has worked less than 20 hours this week."
            print(message)
            logs.append(message)

        employees.append({
            "name": employee,
            "hours": hours,
            "wage": wage
        })

logs.append("")
logs.append("Open Shift Assignments:")
logs.append("-" * 30)

print("\nOpen Shift Assignments:")
print("-" * 30)

# Read week schedule
with open("week.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file, skipinitialspace=True)

    for row in reader:
        day = row["day"]
        opening = row["opening"]
        closing = row["closing"]
        openshift = row["openshift"]

        if openshift.lower() == "yes":

            available = [e for e in employees if e["hours"] < 40]

            if available:
                selected = min(available, key=lambda e: e["hours"])

                message = (
                    f"{selected['name']} is assigned to the open shift on "
                    f"{day} ({opening}-{closing}) because they have worked "
                    f"{selected['hours']} hours."
                )

                print(message)
                logs.append(message)

                # Add 8 hours after assignment
                selected["hours"] += 8

            else:
                message = f"No employee available for {day}."
                print(message)
                logs.append(message)
import datetime
x = datetime.datetime.now()
filename = f"log.txt"
with open(filename, "w", encoding="utf-8") as f:
    for line in logs:
        f.write(line + "\n")