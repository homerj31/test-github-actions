import csv

total = 0.0

def es_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  for row in reader:
    if (es_numero(row["Quantity"]) and es_numero(row["Cost"])):
        total += float(row["Quantity"]) * float(row["Cost"])
    else:
        print(f"Invalid data in row: {row}")

print(f"Total: ${round(total,2)}")