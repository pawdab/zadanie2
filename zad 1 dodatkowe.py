numbers = [5,32,56,2,2,16,7,10,23,100]
numbers = [round(number+1e-15, -1) for number in numbers]

print(numbers)

numbers.remove(min(numbers))
numbers.remove(max(numbers))

print(numbers)
#for number in numbers:
#    if number == max numbers:
#        najmniejszanumbers.remove(number)
    

def mean(lista):
    average = 0
    for element in lista:
        average = average + element

    return average/len(lista)



mean_number = mean(numbers)
print(mean_number)

