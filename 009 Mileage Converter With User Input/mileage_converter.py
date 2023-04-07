print("Geben Sie an, wieviele Kilometer in Meilen umgerechnet werden sollen:")
kilometers = input()
miles = float(kilometers)/1.60934
miles = round(miles,2)
print(f"{kilometers}km sind umgerechnet {miles}mi.")