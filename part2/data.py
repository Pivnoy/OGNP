import pandas as pd
import plotly.express as ps
import matplotlib.pyplot as plt

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
print(mensHalf / allList * 100)
print(womensHalf / allList * 100)

# Процент выживших мужчин до 45 к общему числу mensHalf
Alive = 'A'
Age = '45'
menQuery = dataFrame.query('status == @Alive').query('age < @Age').shape[0]
print(menQuery / allList * 100)

# Показать как соотносятся возраст и смертность у пациентов старше 14 лет. Постройте график
# функции
dedIncide = 'D'
altQuery = dataFrame.query('status == @dedIncide')['age']
ageArray = []
for i in altQuery:
    if i != '---------' and int(i) >= 14:
        ageArray.append(int(i))
ageArray.sort()
# Задание параметров отрисовки
ls = pd.Series(ageArray)
lines = ls.plot.line()
lines.set_xlabel('Quantity')
lines.set_ylabel('Age')
# Отрисовка с помощью plot
# plt.show()

# Задание параметров для plotly
fig = ps.line(ageArray, title='Death of people high then 14 age')
fig.update_xaxes(range=(1,2000),title_text='Quantity')
fig.update_yaxes(title_text='Age')
# Отрисовка с помощью plotly
# fig.show()


# Построить круговую диаграмму, отражающую процентное соотношение умерших пациентов
# в возрасте до 30 лет, распределение по региона Австралии
ausAge = '30'
str = '---------'
ausQuery = dataFrame.query('age <= @ausAge and age != @str')[['age','state']]
print(ausQuery)
