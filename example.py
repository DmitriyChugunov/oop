# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __del__(self):
#         print("Обьект уничтожен")
#     def say(self, message):
#         print(message)
#     def say_hello(self):
#         self.say(f' Hello my name is {self.name} I"m {self.age} yers ')
#
#
# tom = Person('tom', 14)
# bob = Person('bob', 25)
# # print(tom.age, tom.kind)
# # print(bob.kind)
# # tom.say_hello()
# # tom.say("egegr")
# # print(bob.name)
# # print(tom.name)
# # tom.say_hello()
# # bob.say_hello()
# # bob.age = 16
# # bob.say_hello()
# # print(bob.age)
# # str = '1,2,3'
# # s = str.split()
# # print(s)
# del bob

################# 1 ##############
# class Point3D:
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x
#         self.y = y
#         self.z = z
#     def info(self):
#         print(f' x = {self.x}, y = {self.y}, z = {self.z}')
#
#     def distance(self, a, b):
#         return b - a
#
#     def distance2(self):
#         return f'Расстояние между x до y {self.distance(self.x, self.y)}. \nРасстояние между y и z: {self.distance(self.y, self.z)}'
#
# first = Point3D(2,5,8)
# second = Point3D(5,8,7)
# third = Point3D(8,7,3)
# first.info()
# print(first.distance2())
#
############### 2 ############
# class kva2:
#     def __init__(self, a = 0):
#         self.a = a
#
#     def plo(self, a):
#         return a * a
#
#     def per(self, a):
#         return a * 4
# inits = kva2(5)
# print(inits.plo(5))
# print(inits.per(5))

################ 3 #############
# class tre:
#     def __init__(self, a=0, b=0, c=0):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def per(self, a, b ,c):
#         return a + b + c
#     def plo(self, a, b, c):
#         return a * b * c
# res = tre
# print(res.per(2, 3,5, 6))
# print(res.plo(2, 3,5, 6))

################# 4 #############
# class tochki:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def res(self):
#         if self.a > self.b:
#             x = self.b - self.a
#             x = str([x])
#             print(x[2:-1])
#         else:
#             print( self.b - self.a)
# result = tochki(4,3)
# result.res()
################## 5 #############

# class CPerson:
#     def __init__(self, name, fam, ot, data, pol):
#         self.name = name
#         self.fam = fam
#         self.ot = ot
#         self.data = data
#         self.pol = pol
#
#     def say(self, message):
#
#         print(message)
#     def prin(self):
#         self.say(f'Ваше ФИО: {self.fam, self.name, self.ot}, ваша дата рождения: {self.data}, ваш пол: {self.pol}')
#
# res = CPerson('Дмитрий', 'Чугунов', 'Александрович', '03.12.2007', 'Мужской')
# res.prin()

################## 6 ################


# class Phone:
#     def __init__(self, number, model, weight, getNumber, receiveCall):
#         self.number = number
#         self.model = model
#         self.weight = weight
#         self.getNumber = getNumber
#         self.receiveCall = receiveCall
#     def say(self, message):
#         print(message)
#
#     def receiveCalls(self):
#         self.say(f'Звонит {self.receiveCall}')
#
#     def getNumbers(self):
#         self.say(f'Номер звонящего: {self.getNumber}')
#     def prin(self):
#         self.say(f'Ваш номер телефона: {self.number}, Ваша модель: {self.model}, Ваша ширина: {self.weight}')
#
# ress = Phone("+79803328307", "Honor", '10см', '+79155340924', 'Александр')
# ress.prin()
# ress.receiveCalls()
# ress.getNumbers()

################ 7 ############
# class Reader:
#     def __init__(self, fio, number_bilet, fak, data, number, takebooks, returnbooks):
#         self.fio = fio
#         self.number_bilet = number_bilet
#         self.fak = fak
#         self.data = data
#         self.number = number
#         self.takebooks = takebooks
#         self.returnbooks = returnbooks
#     def say(self,message):
#         print(message)
#     def takeBook(self):
#         self.say(f'{self.fio} взял {self.takebooks} книги')
#     def returnBook(self):
#         self.say(f'{self.fio} вернул {self.returnbooks} книги')
# result = Reader('Чугунов Дмитрий Александрович', '2', 'Грифиндор', '03.12.2007', '+79803328307', '3', '3')
# result.takeBook()
# result.returnBook()