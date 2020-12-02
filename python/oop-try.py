# class Perulangan:
#     count = 0
#     def cetak_count(self):
#         while (self.count < 5):
#             self.count += 1
#             print(self.count, 'Kurang dari 5')
#         print(self.count, 'Lebih dari 5')
        
# obj = Perulangan()
# obj.cetak_count()

# num = 1

# while (num > 5):
#     num += 1
#     print('inside while ', num)

# else:
#     num -= 1
#     print('inside else ', num)

# print('last one ', num)

cond = True
while not cond:
    print('ini true')
    cond = False
    break
else:
    print('ini apa yah ', cond)