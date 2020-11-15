import pandas as pd

# чтение данных из csv формата по ТЗ
data = pd.read_csv("/Users/lubovmakareva/Documents/ognp3/part2/Aids2.csv")

# Блок начальных сведений о данных
dataFrame = pd.DataFrame(data)

# Информация о типах столбцов
print(dataFrame.dtypes)
# Общая размерность объекта
print(dataFrame.size)
# Кортеж, в котором хранится количество строк и столбцов
print(dataFrame.shape)
allList = dataFrame.shape[0]

# Фильтрация данных
menList = dataFrame.filter(like='sex').values
mensHalf = 0
for i in range(len(menList)):
    if menList[i][0] == 'M':
        mensHalf += 1
womensHalf = allList - mensHalf

# Вывод процентных соотношений
print(mensHalf/allList*100)
print(womensHalf/allList*100)

# Процент выживших мужчин до 45 к общему числу mensHalf
Alive = 'A'
Age = '45'
menQuery = dataFrame.query('status == @Alive').query('age < @Age').shape[0]
print(menQuery/allList*100)
