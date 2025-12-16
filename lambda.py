# Labda is an anonymous function. A function that has no name
# It is used if you don't want to call on a value later

#this is for def, if you want to call the value later
# def multipy_by_2(val):
#     return val * 2

# print(multipy_by_2(10))

#using lambda, if you don't want to call the value later
# a = lambda val, num : val * num
# print(a(10, 20))

#map filter
# you can map through a list of numbers or anything
# nums = [10,20,30]
# result = list(map(lambda val : val - 5, nums))
# print(result)

#when you use normal for loop instead of map
# nums = [10,20,30]
# result = []
# for num in nums:
#     result.append(num - 5)
# print(result)

#Filter
# It allows value pass through if it meets the condition and also prevent values from passing through if it doesn't meet the condition
# nums = [5, 8, 6, 15, 2]
# res = tuple(filter(lambda val: val > 7, nums))
# print(res)

#Classwork
names = ["Tolu", "Ojo", "Abidakun", "Alekuwodo", "abcdef"]
result = filter(lambda name: len(name) > 5, names)
res = list(map(lambda val: len(val), result))
print(res)