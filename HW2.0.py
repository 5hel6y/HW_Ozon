import random
balanse = 10000
s = 1000
print("Здравствуйте вы попали в виртуальное казино с прекрасным названием HW2.0")
print("Ваш стартовый дипозит 10000 рублей \nПравила такие играем в угадай число ставка 1000 руб0лей\nКрупье бросает кости максимум может выпасть 12 минимум 2 при совпадении + 1000 не угадал ставка сгорает\nНадеюсь все понятно")
while True :
  number = ("Загадывай число")
  print(number)
  number = int(input())
  randomnumb = random.randint(2, 13)
  print("Вы загадали цифру", number)
  print("Число которое выпало у крупье равно", randomnumb)
  if randomnumb == int(number):
    print("Вы выиграли на ваш баланс зачисленно 1000\nВаш баланс сейчас\nПовторите Ваш успех!")
    balanse = (balanse + s)
    print(balanse)
  else:
    print("Вы не угадали число, ставка сгорела\nПопробуйте снова! я уверен Вам повезет\nВаш баланс сейчас")
    balanse = (balanse - s)
    print(balanse)
    if balanse <= 0 :
     print ("GAMEOWER")
     break
