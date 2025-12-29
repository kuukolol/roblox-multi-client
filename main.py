import sys
import psutil
import customtkinter as ctk
import win32event
import win32api

MUTEX_NAME = "ROBLOX_singletonMutex"
ERROR_ALREADY_EXISTS = 183
mutex = None


def kill_roblox_processes():
    try:
        killed = 0
        for proc in psutil.process_iter(["pid", "name"]):
            try:
                if proc.info["name"] == "RobloxPlayerBeta.exe":
                    proc.kill()
                    killed += 1
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        if killed > 0:
            print(f"Killed {killed} Roblox process(es).")

    except Exception as e:
        print(f"Error killing Roblox processes: {e}")


def setup_mutex():
    global mutex

    temp_mutex = win32event.CreateMutex(None, False, MUTEX_NAME)
    last_error = win32api.GetLastError()

    if last_error == ERROR_ALREADY_EXISTS:
        print("Existing mutex detected. Clearing handle.")
        win32api.CloseHandle(temp_mutex)
    else:
        win32api.CloseHandle(temp_mutex)

    mutex = win32event.CreateMutex(None, True, MUTEX_NAME)
    print("Mutex created and owned.")


def on_close():
    global mutex
    if mutex:
        win32api.CloseHandle(mutex)
        print("Mutex handle closed.")

    app.destroy()
    sys.exit(0)


kill_roblox_processes()
setup_mutex()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Roblox Multi Client")
app.geometry("330x170")
app.resizable(False, False)


app.update_idletasks()
x = (app.winfo_screenwidth() // 2) - (330 // 2)
y = (app.winfo_screenheight() // 2) - (170 // 2)
app.geometry(f"+{x}+{y}")

frame = ctk.CTkFrame(app, corner_radius=14)
frame.pack(expand=True, fill="both", padx=15, pady=15)

title = ctk.CTkLabel(
    frame, text="Roblox Multi-Client", font=ctk.CTkFont(size=20, weight="bold")
)
title.pack(pady=(20, 5))

status = ctk.CTkLabel(
    frame, text="🟢 Multi-client is active", font=ctk.CTkFont(size=14)
)
status.pack(pady=5)

credit = ctk.CTkLabel(
    frame, text="Built by shinonomechan", font=ctk.CTkFont(size=11), text_color="gray"
)
credit.pack(pady=(10, 20))

app.protocol("WM_DELETE_WINDOW", on_close)
app.mainloop()
