import random

def main():
    print("=== Game Tebak Angka ===")
    print("Saya sudah memilih angka antara 1 sampai 100.")
    print("Coba tebak angkanya! Kamu punya 7 kesempatan.\n")

    secret_number = random.randint(1, 100)
    max_attempts = 7

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Tebakan ke-{attempt}: "))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if guess < 1 or guess > 100:
            print("Tebakan harus antara 1 dan 100!")
            continue

        if guess == secret_number:
            print(f"🎉 Selamat! Kamu menebak dengan benar dalam {attempt} percobaan!")
            break
        elif guess < secret_number:
            print("📉 Terlalu rendah!")
        else:
            print("📈 Terlalu tinggi!")

        if attempt == max_attempts:
            print(f"\n😢 Kesempatan habis! Angka yang benar adalah {secret_number}.")

if __name__ == "__main__":
    main()
