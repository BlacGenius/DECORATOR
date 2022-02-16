
def decorator(temperature):
    if temperature > 10:
        print("На улице тепло, давай погуляем, я не против!")
    elif temperature > 0 and temperature < 10:
        print("Прохладно. Надо одеться!")
    elif temperature > -10 and temperature < 0:
        print("Холодно. Потеплее оденься и пойдем!")
    elif temperature < -10:
        print("Мороз. Лучше давай дома посидим, фильм посмотрим!")
        
    def outer(func):
        
        def wapper():
            result = func()
            return result
        return wapper
    return outer

while True: # я думаю, что такая реализация более практичным
    temperature = input()
    if temperature.isdigit() == True:
        @decorator(int(temperature))
        def go_for_a_walk():
            return f'Давай, пойдем погуляем на улице!'
        
        print(go_for_a_walk())




