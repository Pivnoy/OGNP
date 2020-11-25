import pandas as pd
import matplotlib.pyplot as plt

# чтение данных из csv формата по ТЗ
data = pd.read_csv("/home/anna/PycharmProjects/ognp32/avocado.csv")

# блок начальных сведений о данных
dataFrame = pd.DataFrame(data)

# информация о типах столбцов
print(dataFrame.dtypes)
# общая размерность объекта
print(dataFrame.size)
# кортеж, в котором хранится количество строк и столбцов
print(dataFrame.shape)

# количество всех записей
countAll = dataFrame.shape[0]

# процентное соотношение conventional и organic
conventional = 'conventional'
organic = 'organic'
conventionalCount = dataFrame.query('type == @conventional').shape[0]
organicCount = dataFrame.query('type == @organic').shape[0]

print(conventionalCount / countAll * 100)
print(organicCount / countAll * 100)

# количество записей за 2015 год
year = 2015
count2015 = dataFrame.query('year == @year').shape[0]
yearQuery = dataFrame.query('year == @year')['AveragePrice']


def countAveragePriceYear(df, year):
    yearQuery = df.query('year == @year')['AveragePrice']
    count = df.query('year == @year').shape[0]
    averageSum = 0
    for value in yearQuery:
        averageSum += value
    return averageSum / count


average2015 = countAveragePriceYear(dataFrame, 2015)

print("Average sum is " + str(average2015))


# количество проданных больших мешков авокадо за разные года

def countBags(year):
    count = 0
    for value in dataFrame.query('year == @year')['Large Bags']:
        count += value
    return count


years = ['2015', '2016', '2017', '2018']
arr = []

for year in years:
    arr.append(countBags(year))

# график процентного соотношения
gt = pd.DataFrame({
    'large bags quantity': arr
}, index=years)
plit = gt.plot.pie(y='large bags quantity')
plt.show()

# средняя цена за 2016 год в нескольких регионах
average2016 = countAveragePriceYear(dataFrame, 2016)

atl = 'Atlanta'
chr = 'Charlotte'
bst = 'Boston'
den = 'Denver'
regions = [atl, chr, bst, den]

averageAtlanta = countAveragePriceYear(dataFrame.query('region == @atl'), 2016)
averageCharlotte = countAveragePriceYear(dataFrame.query('region == @chr'), 2016)
averageBoston = countAveragePriceYear(dataFrame.query('region == @bst'), 2016)
averageDenver = countAveragePriceYear(dataFrame.query('region == @den'), 2016)

print("Average is " + str(average2016))
print("Average in Atlanta " + str(averageAtlanta))
print("Average in Charlotte " + str(averageCharlotte))
print("Average in Boston " + str(averageBoston))
print("Average in Denver " + str(averageDenver))

# создание диаграммы
priceFrame = pd.DataFrame({
    'av2016': [average2016, average2016, average2016, average2016],
    'regions': [averageAtlanta, averageCharlotte, averageBoston, averageDenver]
}, index=regions)

axel = priceFrame.plot.barh()
plt.show()

# количество разных закупленных мешков в 2017 году

bagTypes = ['Small Bags', 'Large Bags', 'XLarge Bags']


def typeOfBags(state, year):
    bagDict = {}
    df = dataFrame.query('year == @year and region == @state')
    for bagType in bagTypes:
        bags = df[bagType]
        bagCount = 0
        for value in bags:
            bagCount+=value
        bagDict[bagType] = bagCount
    return bagDict


for region in regions:
    result = typeOfBags(region, 2017)
    framer = pd.DataFrame({
        'bags': list(result.keys()),
        'values': list(result.values())
    })
    rimb = framer.plot.barh(x='bags', y='values', title=region)
    plt.show()
