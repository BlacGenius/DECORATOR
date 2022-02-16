
def decor(func):
    def say():
        print("Я - декоратор")
        result = func()
        print("Я все сделал")
        return result
    return say

@decor
def say_my_name():
    print(f'my name is Beka')

say_my_name()