import pandas as pd
import plotly.express as ps
import matplotlib.pyplot as plt
from multipledispatch import dispatch

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
print(menQuery / mensHalf * 100)

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
fig.update_xaxes(range=(1, 2000), title_text='Quantity')
fig.update_yaxes(title_text='Age')
# Отрисовка с помощью plotly
# fig.show()


# Построить круговую диаграмму, отражающую процентное соотношение умерших пациентов
# в возрасте до 30 лет, распределение по региона Австралии
ausAge = '30'
str = '---------'
# общее количество по критерию
# ausQuery = dataFrame.query('age <= @ausAge and age != @str')[['age','state']].shape[0]
ausQuery = dataFrame.query('age <= @ausAge and age != @str and status == @dedIncide')
# количество по штатам (NSW,QLD,Other,VIC)
nsw = 'NSW'
qld = 'QLD'
vic = 'VIC'
other = 'Other'
quanNSW = ausQuery.query('state == @nsw').shape[0]
quanQLD = ausQuery.query('state == @qld').shape[0]
quanVIC = ausQuery.query('state == @vic').shape[0]
quanOther = ausQuery.query('state == @other').shape[0]
arr = [quanNSW, quanQLD, quanVIC, quanOther]
gt = pd.DataFrame({
    'stateQuntyties': arr
}, index=['NCW', 'QLD', 'VIC', 'Other'])
plit = gt.plot.pie(y='stateQuntyties')

# Отрисовка при помощи matplotlib
fig, ax = plt.subplots()
ax.pie(arr,labels=['NCW', 'QLD', 'VIC', 'Other'])
ax.axis('equal')

# Посчитать средний возраст умерших в датасете
taskQuery = dataFrame.query('age <= @ausAge and age != @str')


def middleOfAge(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)


# Для всей Австралии
allAustralia = middleOfAge(taskQuery['age'].astype(int))
# По штатам
agedNSW = middleOfAge(taskQuery.query('state == @nsw')['age'].astype(int))
agedQLD = middleOfAge(taskQuery.query('state == @qld')['age'].astype(int))
agedVIC = middleOfAge(taskQuery.query('state == @vic')['age'].astype(int))
agedOther = middleOfAge(taskQuery.query('state == @other')['age'].astype(int))
print("All Australia", allAustralia)
print("The other states", agedNSW, agedQLD, agedVIC, agedOther)

# Создание фрейма
agedFrame = pd.DataFrame({
    'aus': [allAustralia, allAustralia,allAustralia,allAustralia],
    'values': [agedNSW, agedQLD, agedVIC, agedOther]
}, index=['NCW', 'QLD', 'VIC', 'Other'])

# отрисовка диаграммы
axel = agedFrame.plot.barh()


# Определите возраст самого молодого и самого старого пациента в регионе
def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


def smallestInRegion(listing):
    smallest = 1000
    for age in listing:
        if age < smallest:
            smallest = age
    return smallest


def oldestInRegion(listing):
    oldest = 0
    for age in listing:
        if age > oldest:
            oldest = age
    return oldest


def more55(people):
    quantity = 0
    for age in people:
        if age >= 55:
            quantity += 1
    return quantity


def more31less54(people):
    quantity = 0
    for age in people:
        if 31 <= age <= 54:
            quantity += 1
    return quantity


def less30(people):
    quantity = 0
    for age in people:
        if age <= 30:
            quantity += 1
    return quantity


# Трекер валидации возраста
trackFrame = dataFrame.query('age != @str').query('status == @dedIncide')

# Самые маленькие по регионам
smallNSW = smallestInRegion(trackFrame.query('state == @nsw')['age'].astype(int))
smallQLD = smallestInRegion(trackFrame.query('state == @qld')['age'].astype(int))
smallVIC = smallestInRegion(trackFrame.query('state == @vic')['age'].astype(int))
smallOther = smallestInRegion(trackFrame.query('state == @other')['age'].astype(int))
print('The smallest in Regions', smallNSW, smallQLD, smallVIC, smallOther)

# Самые старшие по регионам
oldNSW = oldestInRegion(trackFrame.query('state == @nsw')['age'].astype(int))
oldQLD = oldestInRegion(trackFrame.query('state == @qld')['age'].astype(int))
oldVIC = oldestInRegion(trackFrame.query('state == @vic')['age'].astype(int))
oldOther = oldestInRegion(trackFrame.query('state == @other')['age'].astype(int))
print('The oldest in Regions', oldNSW, oldQLD, oldVIC, oldOther)

# Регион с наибольшим количеством инфицированных людей старше 55
more55dict = {}
more55NSW = more55dict['NSW'] = more55(trackFrame.query('state == @nsw')['age'].astype(int))
more55QLD = more55dict['QLD'] = more55(trackFrame.query('state == @qld')['age'].astype(int))
more55VIC = more55dict['VIC'] = more55(trackFrame.query('state == @vic')['age'].astype(int))
more55Other = more55dict['Other'] = more55(trackFrame.query('state == @other')['age'].astype(int))
print(get_key(more55dict, max(more55dict.values())))

# Регион с наибольшим количество инфицированных людей от 31 до 54
more31less54dict = {}
more31less54NSW = more31less54dict['NSW'] = more31less54(trackFrame.query('state == @nsw')['age'].astype(int))
more31less54QLD = more31less54dict['QLD'] = more31less54(trackFrame.query('state == @qld')['age'].astype(int))
more31less54VIC = more31less54dict['VIC'] = more31less54(trackFrame.query('state == @vic')['age'].astype(int))
more31less54Other = more31less54dict['Other'] = more31less54(trackFrame.query('state == @other')['age'].astype(int))
print(get_key(more31less54dict, max(more31less54dict.values())))

# Регион с наибольшим количеством инфицированных людей до 30
less30dict = {}
less30NSW = less30dict['NSW'] = less30(trackFrame.query('state == @nsw')['age'].astype(int))
less30QLD = less30dict['QLD'] = less30(trackFrame.query('state == @qld')['age'].astype(int))
less30VIC = less30dict['VIC'] = less30(trackFrame.query('state == @vic')['age'].astype(int))
less30Other = less30dict['Other'] = less30(trackFrame.query('state == @other')['age'].astype(int))
print(get_key(less30dict, max(less30dict.values())))


# Анализ и диаграмма способов заражения по регионам
def waysInState(ste):
    return set(dataFrame.query('state == @ste')['T.categ'])


def quentityOf(ste):
    resDict = {}
    for ider in categ:
        resDict[ider] = 0
    dataList = dataFrame.query('state == @ste')['T.categ']
    for dat in dataList:
        resDict[dat] += 1
    return resDict


stat = set(dataFrame['state'])
categ = set(dataFrame['T.categ'])
for state in stat:
    resutl = quentityOf(state)
    framer = pd.DataFrame({
        'catg': resutl.keys(),
        'values': resutl.values()
    })
    rimb = framer.plot.barh(x='catg', y='values',title=state)

# Анализ выживших и умерших пациентов
@dispatch(object)
def procent(age):
    alive = 'A'
    adead = 'D'
    aller = dataFrame.query('age <= @age')['age'].shape[0]
    live = dataFrame.query('age <= @age').query('status == @alive')['age'].shape[0] * 100 / aller
    death = dataFrame.query('age <= @age').query('status == @adead')['age'].shape[0] * 100 / aller
    if live > death:
        print("In group of " + age + " more live")
    else:
        print("In group of " + age + " more die")
    return


@dispatch(object, object)
def procent(minAge, maxAge):
    alive = 'A'
    adead = 'D'
    aller = dataFrame.query('age >= @minAge and age <= @maxAge')['age'].shape[0]
    live = dataFrame.query('age >= @minAge and age <= @maxAge').query('status == @alive')['age'].shape[0] * 100 / aller
    death = dataFrame.query('age >= @minAge and age <= @maxAge').query('status == @adead')['age'].shape[0] * 100 / aller
    if live > death:
        print("In group of " + minAge + " and " + maxAge + " more live")
    else:
        print("In group of " + minAge + " and " + maxAge + " more die")
    return


procent('30')
procent('31', '54')
procent('55')

plt.show()