name = input("Введите имя студента ")
surname = input("Введите фамилию студента ")
year = int(input("Введите год рождения студента "))
print(name, surname, year, sep = "_")
name, surname = surname, name
year += 60
print(name, surname, year, sep = "_")