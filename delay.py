tip = """
ldi r16, {}
d0:
    ldi r17, {}
    d1:
        ldi r18, {}
        d2:
            dec r18
            brne d2
        dec r17
        brne d1
    dec r16
    brne d0
"""

def f(y, delay, tick):
    x = delay * 1.0 / (4 + 769 * y) / tick
    return x

def f2(y, delay, tick):
    x = (delay / tick + 2) / (3 * (1 + 256 * y))
    return x

frequency = float(input('Частота в МГц (4 по умолчанию): ') or 4)
tick = 1.0 / (frequency * 1000000)
print("1 такт:", tick)
delay = float(input('Задержка в мс (200 мс - 12 с): ')) / 1000

z = 255
delta = 1.0
answer = []
for y in range(256):
    x = f2(y, delay, tick)
    if x > 1 and x < 256:
        d = abs(x - round(x))
        if d < delta:
            delta = d
            answer = [x, y, z]

if answer:
    print(tip.format(int(answer[0]), answer[1], answer[2]))
else:
    print('Что-то пошло не так. Задержка слишком маленькая или слишком большая.')


