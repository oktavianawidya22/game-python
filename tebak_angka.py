import random

def pilih_mode():
    print("=== Pilih Mode Permainan ===")
    print("1. Easy (angka 1-50, 10 percobaan)")
    print("2. Hard (angka 1-100, 7 percobaan)")
    while True:
        mode = input("Pilih mode (1 atau 2): ")
        if mode == '1':
            return 1, 50, 10
        elif mode == '2':
            return 2, 100, 7
        else:
            print("Pilihan tidak valid. Coba lagi.")

def main():
    best_score = None

    while True:
        mode, max_num, max_attempts = pilih_mode()
        secret_number = random.randint(1, max_num)
        print(f"\nSaya sudah memilih angka antara 1 dan {max_num}.")
        print(f"Coba tebak dalam {max_attempts} percobaan!\n")

        for attempt in range(1, max_attempts + 1):
            try:
                guess = int(input(f"Tebakan ke-{attempt}: "))
            except ValueError:
                print("Masukkan angka yang valid!")
                continue

            if guess < 1 or guess > max_num:
                print(f"Tebakan harus antara 1 dan {max_num}!")
                continue

            if guess == secret_number:
                print(f"\n🎉 Selamat! Kamu menebak dengan benar dalam {attempt} percobaan!")

                # Cek skor terbaik
                if best_score is None or attempt < best_score:
                    best_score = attempt
                    print("🏆 Skor terbaik baru!")
                else:
                    print(f"Skor terbaik saat ini: {best_score} percobaan")
                break
            elif guess < secret_number:
                print("📉 Terlalu rendah!")
            else:
                print("📈 Terlalu tinggi!")

            if attempt == max_attempts:
                print(f"\n😢 Kamu kalah! Angka yang benar adalah {secret_number}.")

        # Main lagi?
        ulang = input("\nMau main lagi? (y/n): ").lower()
        if ulang != 'y':
            print("\nTerima kasih sudah bermain! Sampai jumpa! 👋")
            break

if __name__ == "__main__":
    main()
