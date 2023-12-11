#Задание:
#1.Прочитать в виде списков набор данных titanic.csv, взятый из открытых источников:
#https://tproger.ru/translations/the-best-datasets-for-machine-learning-and-data-science/
#https://vc.ru/ml/150241-15-proektov-dlya-razvitiya-navykov-raboty-s-mashinnym-obucheniem
#https://archive.ics.uci.edu/ml/index.php
#https://habr.com/ru/company/edison/blog/480408/
#https://www.kaggle.com/datasets/
#2.Для прочитанного набора выполнить обработку в соответствии со своим вариантом.
# Библиотекой pandas пользоваться нельзя.

#28.Определить суммарную стоимость билетов мужчин на борту в возрастном интервале мода  5 позиций

import csv
with open("titanic.csv", "r", encoding="latin-1") as f:
    reader = csv.reader(f)
    header = next(reader)
    data = [row for row in reader]
i_age = header.index('age')
i_price = header.index('fare')
i_sex = header.index('sex')
age = []
for p in data:
    if p[i_age] != '' and p[i_sex] == 'male':
        age.append(p[i_age])
maxi = int(max(age, key = age.count))
min_int = maxi - 5
max_int = maxi + 5
sum = 0.0
for p in data:
    if p[i_age] != '' and float(p[i_age]) <= max_int and float(p[i_age]) >=min_int and p[i_sex] == 'male':
        sum = sum + float(p[i_price])
print("Мода: ",maxi)
print(f"Интервал: {min_int} - {max_int}")
print('Сумма стоимости билетов: ',sum)




