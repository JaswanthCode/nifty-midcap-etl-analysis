import csv

with open("config/top10_stocks.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["symbol"], row["company_name"])
