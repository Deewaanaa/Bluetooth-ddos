# Termux Bluetooth L2CAP Stress Tester

A Python-based threading tool for testing Bluetooth L2CAP connection stability. Adapted from the GMU CYSE 425 project for the Termux environment.

## ⚠️ Requirements
* **Termux** (Android)
* **Root Access** (Required for `l2ping` raw socket access)
* **BlueZ** utilities

## 🛠️ Installation & Setup

1. **Update Termux & Install Dependencies:**
   ```bash
   pkg update && pkg upgrade
   pkg install python bluez tsu -y
