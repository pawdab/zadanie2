models = ['Volkswagen - Golf', 'Renault - Clio','Volkswagen - Polo',
'Ford - Fiesta','Nissan - Qashqai','Peugeot - 208','VW - Tiguan','Skoda - Octavia',
'Toyota - Yaris','Opel - Corsa','Dacia - Sandero','Renault - Captur','Citroen - C3',
'Peugeot - 3008','Ford - Focus','Fiat - 500','Dacia - Duster','Peugeot - 2008',
'Skoda - Fabia','Fiat - Panda','Opel - Astra','VW - Passat','Mercedes-Benz - A-Class',
'Peugeot - 308','Ford - Kuga']

sales2018 = ['445,754','26,268','299,920','270,738','233,026','230,049','224,788',
'223,352','217,642','217,036','216,306','214,720','210,082','204,197','196,583',
'191,205','182,100','180,204','172,511','168,697','160,275','157,986','156,020',
'155,925','154,125']

sales2017 = ['483,105','337,395','272,061','254,539','247,939','244,615','234,916',
'230,116','199,182','232,738','196,067','212,768','207,299','166,784','214,661',
'189,928','NA','180,868','180,136','187,322','217,813','184,123','NA','NA','NA']

sales2016 = ['492,952','315,115','308,561','300,528','234,340','249,047','180,198',
'230,255','193,969','264,844','170,300','217,105','134,560','NA','214,435',
'183,730','NA','NA','177,301','191,617','253,483','208,575','NA','195,653','NA']


i = 0
#for model in models:
#    if model == 'VW':
#        models[i] = "Volkswagen"
#    i = i +1

i = 0
for sales in sales2018:
    if sales == 'NA':
        sales2018[i] = 0
    else:
        sales2018[i] = int(sales2018[i].replace(",",""))
    i = i +1



i = 0   
for sales in sales2017:
    if sales == 'NA':
        sales2017[i] = 0
    else:
        sales2017[i] = int(sales2017[i].replace(",",""))
    i = i +1


i = 0
for sales in sales2016:
    if sales == 'NA':
        sales2016[i] = 0
    else:
        sales2016[i] = int(sales2016[i].replace(",",""))
    i = i +1

cars = {}
car = {}

i = 0
for model in models:
    car[model[(model.find(" ")+3):(len(model))]] = {"sales": {'2016': sales2016[i], '2017': sales2017[i], '2018': sales2018[i]}}
    if model[0:(model.find(" "))] in cars.keys():
        cars[model[0:(model.find(" "))]].update( {model[(model.find(" ")+3):(len(model))]:car[model[(model.find(" ")+3):(len(model))]]})
    else:
        cars[model[0:(model.find(" "))]] = {model[(model.find(" ")+3):(len(model))]:car[model[(model.find(" ")+3):(len(model))]]}
    i = i + 1

carsx = {}
car = {}

i = 0
for model in models:
    carsx[model[0:(model.find(" "))]] = []
    i = i + 1

i = 0
for model in models:
    car[model[(model.find(" ")+3):(len(model))]] = [sales2018[i], sales2017[i], sales2016[i]]
    carsx[model[0:(model.find(" "))]].append( {model[(model.find(" ")+3):(len(model))]:car[model[(model.find(" ")+3):(len(model))]]})
    i = i + 1


answer1 = models[sales2017.index(max(sales2017))]

sales_total = []

i = 0 
for carItem in carsx.items():
    sales_total.append(0)
    for carItem2 in carItem[1]:
        for carItem3, car_sales in carItem2.items():
            sales_total[i] = sales_total[i] + car_sales[0]
    i = i + 1

i = 0 
for carItem, x in carsx.items():
    if i == sales_total.index(max(sales_total)):
        answer2 = carItem
        break
    i = i + 1

unsold2016 = []
i = 0 
for carItem in carsx.items():
    for carItem2 in carItem[1]:
        for carItem3, car_sales in carItem2.items():
            if car_sales[2] == 0 and car_sales[1] != 0:
                unsold2016.append(carItem3)
    i = i + 1
answer3 = unsold2016

minimum_sales = max(sales_total)

i = 0 
for carItem in carsx.items():
    for carItem2 in carItem[1]:
        for carItem3, car_sales in carItem2.items():
            if car_sales[0] + car_sales[1] + car_sales[2] < minimum_sales:
                answer4 = carItem3
                minimum_sales = car_sales[0] + car_sales[1] + car_sales[2]
        i = i + 1


sales_ford18 = 0
sales_ford17 = 0
i = 0 
for carItem, x in carsx.items():
    if carItem == "Ford":
        for carItem2 in x:
            for carItem3, car_sales in carItem2.items():
                sales_ford18 = sales_ford18 + int(car_sales[0])
                sales_ford17 = sales_ford17 + car_sales[1]
        i = i + 1


answer5 = str((int(round((sales_ford18 / sales_ford17 - 1) * 100,0)))) + "%"

print(answer1)
print(answer2)
print(answer3)
print(answer4)
print(answer5)
print(cars)
