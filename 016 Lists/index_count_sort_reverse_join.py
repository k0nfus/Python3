#   _____           _           
#  |_   _|         | |          
#    | |  _ __   __| | _____  __
#    | | | '_ \ / _` |/ _ \ \/ /
#   _| |_| | | | (_| |  __/>  < 
#  |_____|_| |_|\__,_|\___/_/\_\
                             

# Index [ shows where the vaule of .. occurs ]
liste = ["fleisch", "fisch", "wurst", "schuppen", "tomate", "fleisch"]
print(liste.index("fleisch"))

# Index mit Startpunkt 4, including Index 4
print(liste.index("fleisch", 4))

# Index mit Startpunkt 0 und Endpunkt 2
print(liste.index("fleisch", 0, 2))

#    _____                  _   
#   / ____|                | |  
#  | |     ___  _   _ _ __ | |_ 
#  | |    / _ \| | | | '_ \| __|
#  | |___| (_) | |_| | | | | |_ 
#   \_____\___/ \__,_|_| |_|\__|

numbers = [1, 2, 3 , 4, 5, 6, 3, 8, 14, 345, 11]

# wie oft wird der value .. in der liste gefunden?
print(numbers.count(2))
print(numbers.count(23))
print(numbers.count(3))

# Reverse
print(numbers)
numbers.reverse()
print(numbers)

# Sort
numbers.sort()
print(numbers)