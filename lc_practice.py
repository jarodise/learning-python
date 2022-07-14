names = ["Jarod", "Agnes", "Chatty"]
answer = [ char[0] for char in names]
print(answer)

nums = [1, 2, 3, 4, 5, 6]
answer2 = [num for num in nums if num % 2 == 0]
print(answer2)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
answer3 =[x for x in list1 if x in list2]
print(answer3)

answer4 = [ x for x in range(1, 101) if x % 12 == 0]
print(answer4)

list3 = [x for x in range(1, 101)]
print(list3)

list4 = list("amazing")
print(list4)
answer5 = [x for x in list4 if x not in ["a", "e", "i", "o", "u"]]
print(answer5)