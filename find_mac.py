import os

def main():
    os.system('clear')
    print("="*45)
    print("   BLUETOOTH TARGET MANUAL ENTRY")
    print("="*45)
    print("\n[!] Automatic scanning is blocked by Android security.")
    print("[*] 1. Open 'nRF Connect' app on your phone.")
    print("[*] 2. Scan for your target device.")
    print("[*] 3. Copy the MAC Address (AA:BB:CC:DD:EE:FF).")
    
    target = input("\n[>] Paste Target MAC Address here: ").strip()
    
    if len(target) == 17: # Standard MAC length
        with open("target_mac.txt", "w") as f:
            f.write(target)
        print(f"\n[+] Saved {target} to target_mac.txt")
    else:
        print("\n[!] Error: Invalid MAC address format.")

if __name__ == "__main__":
    main()
