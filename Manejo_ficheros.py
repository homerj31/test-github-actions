import csv, os

total = 0.0

os.system ("clear")

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

with open("Day54Totals.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if (es_numero(row["Quantity"]) and es_numero(row["Cost"])):
            total += int(row["Quantity"]) * float(row["Cost"])
            print (f"Del producto {row['Name']} tenemos {row['Quantity']} unidades y cada una cuesta {row['Cost']}€")
        else:
            print(f"Invalid data in row: {row}")

print(f"Total: {round(total,2)}€")
