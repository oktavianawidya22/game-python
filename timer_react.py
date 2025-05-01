import time
import random
import threading
import sys

def wait_for_go_event(go_event):
    try:
        input()
        if not go_event.is_set():
            print("🚫 Wah! Kamu terlalu cepat! Belum waktunya 'GO!'.")
            sys.exit()  # Keluar dari program
    except KeyboardInterrupt:
        print("\nGame dibatalkan.")
        sys.exit()

def main():
    print("=== Reaction Timer Game ===")
    print("Tekan Enter **setelah** tulisan 'GO!' muncul!")
    print("Kalau kamu tekan sebelum waktunya, kamu langsung kalah!\n")
    input("Tekan Enter untuk mulai...")

    go_event = threading.Event()
    listener = threading.Thread(target=wait_for_go_event, args=(go_event,))
    listener.daemon = True
    listener.start()

    # Tunggu waktu acak antara 3 - 7 detik
    wait_time = random.uniform(3, 7)
    print("Bersiap...")
    time.sleep(wait_time)

    print("GO!")
    go_event.set()  # Tandai bahwa waktu reaksi sudah dimulai
    start_time = time.time()
    input()  # Tunggu user tekan Enter setelah GO!
    end_time = time.time()

    reaction_time = end_time - start_time
    print(f"\n⚡ Waktu reaksi kamu: {reaction_time:.3f} detik.")

    if reaction_time < 0.2:
        print("🌩️ Gila cepat banget!")
    elif reaction_time < 0.5:
        print("🔥 Bagus! Cepat juga.")
    elif reaction_time < 1:
        print("👍 Lumayan.")
    else:
        print("🐢 Masih ngantuk ya?")

if __name__ == "__main__":
    main()
