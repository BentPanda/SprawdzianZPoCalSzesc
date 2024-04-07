def calk_szesc(number):
    if number < 1:
        return "Błąd: Podaj liczbę całkowitą dodatnią."

    szesc_digits = "0123456789ABCDEF"
    szesc_result = ""

    while number > 0:
        remainder = number % 16
        szesc_result = szesc_digits[remainder] + szesc_result
        number //= 16

    return szesc_result

def main():
    try:
        user_input = int(input("Proszę podać liczbę całkowitą dodatnią: "))
        szesc_result = calk_szesc(user_input)
        print(f"Reprezentacja szesnastkowa: {szesc_result}")
    except ValueError:
        print("Błąd: Podano nieprawidłowy argument. Proszę podać liczbę całkowitą.")

if __name__ == "__main__":
    main()
