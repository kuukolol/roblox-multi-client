# Roblox Multi-Client Tool

A lightweight **GUI-based Roblox multi-client enabler** that allows running multiple Roblox clients on one system by managing the `ROBLOX_singletonMutex`.

Built with **Python**, **CustomTkinter**, and **pywin32**.
Packaged as a **single EXE** using **Nuitka**  no console window, GUI only.

**Built by shinonomechan**

---

## ✨ Features

* ✅ Enables Roblox multi-client support
* 🧹 Automatically kills running Roblox processes on launch
* 🔒 Creates and holds the `ROBLOX_singletonMutex`
* 🖥️ Modern, clean GUI (CustomTkinter)
* 🚫 No console window (GUI only)
* 📦 One-file EXE build
* 🪟 Windows-only (by design)

---

## 🧠 How It Works

1. Kills any running `RobloxPlayerBeta.exe` processes
2. Detects and recreates the `ROBLOX_singletonMutex`
3. Keeps the mutex alive while the GUI is open
4. Closing the app releases the mutex automatically

As long as the app is running, Roblox will allow multiple instances.

---

## 📋 Requirements (for source usage)

* Windows 10 / 11
* Python 3.10+ (tested on 3.13)
* Required packages:

  ```bash
  pip install customtkinter psutil pywin32 nuitka
  ```

---

## ▶ Running from Source

```bash
python main.py
```

A small window will appear indicating that multi-client mode is active.

---

## 📦 Building the EXE (Nuitka)

A ready-to-use `build.bat` is provided.

### Build command (summary)

* Onefile EXE
* GUI only (no console)
* Output: `dist/RobloxMultiClient.exe`

To build:

```bat
build.bat
```

After a successful build, run:

```
dist\RobloxMultiClient.exe
```

---

## ⚠ Notes & Limitations

* This tool **does not modify Roblox files**
* Mutex ownership is managed safely using Windows APIs
* Windows automatically releases the mutex when the app exits
* Antivirus software may flag compiled EXEs (false positives are common)

---

## ❓ FAQ

**Q: Why does Roblox close when I open the app?**
A: The app kills existing Roblox processes to ensure a clean mutex state.

**Q: Do I need to keep the app open?**
A: Yes. Closing the app releases the mutex and disables multi-client mode.

**Q: Is this bannable?**
A: This tool does not inject or modify Roblox. Use at your own discretion.

---

## 📜 License

This project is provided as-is for educational and personal use.
No warranty is provided.

---

## 👤 Author

**shinonomechan**
CustomTkinter UI · Windows API · Nuitka build

---
