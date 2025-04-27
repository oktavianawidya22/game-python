import time
import random

def main():
    print("Selamat datang di Reaction Timer Game!")
    print("Saat tulisan 'GO!' muncul, segera tekan Enter secepat mungkin!")
    input("Tekan Enter untuk mulai...")

    # Tunggu waktu acak antara 2-5 detik
    wait_time = random.uniform(2, 5)
    print("Bersiap...")
    time.sleep(wait_time)

    print("GO!")
    start_time = time.time()
    input()  # Tunggu pemain tekan Enter
    end_time = time.time()

    reaction_time = end_time - start_time
    print(f"Waktu reaksi kamu: {reaction_time:.3f} detik.")

    # Memberikan komentar berdasarkan kecepatan
    if reaction_time < 0.2:
        print("⚡ Kilat! Super cepat!")
    elif reaction_time < 0.5:
        print("👍 Bagus! Cepat juga.")
    elif reaction_time < 1.0:
        print("👌 Lumayan, masih bisa lebih cepat.")
    else:
        print("🐢 Lambat banget, ayo coba lagi!")

if __name__ == "__main__":
    main()
