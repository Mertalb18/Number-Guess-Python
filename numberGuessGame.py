import random

def numberGuessGame():
    number = random.randint(1,100)
    tries = 5
    while True:
        tries -= 1
        guess = int(input("1 ile 100 arasında bir tahminde bulunun: "))

        if guess == number:
            print(f"Tebrikler, doğru sayıyı buldunuz. Sayı: {number}.\nKalan hakkınız: {tries}")
            break

        elif tries == 0:
            print(f"Tahmin hakkınız bitti. Bulmanız gereken sayı: {number}")
            break

        elif guess < number:
            if abs(guess - number) < 10:
                print(f'Çok yaklaştınız, sayıyı yükseltmeniz gerekiyor.\nKalan hakkınız: {tries}')
            else:
                print(f'Yükseltin.\nKalan hakkınız: {tries}')

        elif guess > number:
            if abs(guess - number) < 10:
                print(f'Çok yaklaştınız, sayıyı azaltmanız gerekiyor.\nKalan hakkınız: {tries}')
            else:
                print(f'Azaltın.\nKalan hakkınız: {tries}')

        else:
            print("Hatalı giriş yaptınız.")
            

numberGuessGame()