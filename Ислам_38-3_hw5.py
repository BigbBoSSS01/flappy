# data = ("O!", "Megacom", "0705", "Beeline", "0550", "0770", "Katel", "0510", "Fonex", "0543")

# designations = []
# codes = []

# for i in data:
#     if i.isdigit():
#         codes.append(i)
#     else:
#         designations.append(i)

# count = 0
# operators = {}
# while count < 5:
#     operators[designations[count]] = set()
#     operators[designations[count]].add(codes[count])
#     count +=1

# del operators['Katel']
# del operators['Fonex']

# nums = {'0703','0505'}
# nums2 = {'0555','0999'}
# nums3 = {'0777','0772'}

# operators['O!'].update(nums)
# operators['Megacom'].update(nums2)
# operators['Beeline'].update(nums3)

# for i ,l in operators.items():
#     print(f'{i}:{l}')