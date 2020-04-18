numbers = [5,32,56,2,2,16,7,10,23,100]
numbers = [int(round(number+1e-15, -1)) for number in numbers]

print(numbers)

numbers = [number for number in numbers if number != min(numbers) and number != max(numbers)]

#smallest = min(numbers)
#biggest = max(numbers)

#for number in numbers[:]:
#    if smallest in numbers:
#        numbers.remove(smallest)
#    else:
#        break
#    if biggest in numbers:
#        numbers.remove(biggest)
#    else:
#        break

print(numbers)


def mean(lista):
    average = 0
    for element in lista:
        average = average + element
    return round(average/len(lista),2)


print(mean(numbers))

