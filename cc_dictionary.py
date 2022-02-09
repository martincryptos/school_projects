inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

# total = inches_snow["Monday"] + inches_snow["Tuesday"] + inches_snow["Wednesday"]
# print("Total snowfall inches: ", total)


def print_total_snowfall(inches_snow):
    total_inches = 0
    for inches in inches_snow:
        total_inches += inches_snow[inches]
    print("Total snowfall inches: ", total_inches)


print_total_snowfall(inches_snow)

thursday = input("How many inches of snow fell on Thursday?  ")
inches_snow["Thursday"] = int(thursday)

print_total_snowfall(inches_snow)
