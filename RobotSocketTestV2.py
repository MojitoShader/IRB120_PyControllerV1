import socket
import tkinter as tk
from tkinter import messagebox

ROBOT_IP = "192.168.125.1"
ROBOT_PORT = 1025

class RobotClient:
    def __init__(self, master):
        self.master = master
        self.master.title("ABB Routine-Steuerung")
        self.sock = None

        # Buttons
        tk.Button(master, text="Starte ROUTINE1", width=30, command=lambda: self.send_command("ROUTINE1")).pack(pady=5)
        tk.Button(master, text="Starte ROUTINE2", width=30, command=lambda: self.send_command("ROUTINE2")).pack(pady=5)
        tk.Button(master, text="Verbindung trennen", width=30, command=self.disconnect).pack(pady=20)

        self.status_label = tk.Label(master, text="Verbindungsaufbau...", fg="blue")
        self.status_label.pack(pady=5)

        self.connect()

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((ROBOT_IP, ROBOT_PORT))
            self.status_label.config(text="Verbunden mit Roboter", fg="green")
        except Exception as e:
            self.status_label.config(text="Verbindung fehlgeschlagen", fg="red")
            messagebox.showerror("Fehler", f"Verbindung fehlgeschlagen: {e}")
            self.master.destroy()

    def send_command(self, command):
        try:
            self.sock.sendall(command.encode('utf-8'))
            self.status_label.config(text=f"Befehl gesendet: {command}", fg="black")
        except Exception as e:
            messagebox.showerror("Fehler", f"Fehler beim Senden: {e}")
            self.disconnect()

    def disconnect(self):
        if self.sock:
            try:
                self.sock.close()
            except:
                pass
            self.sock = None
            self.status_label.config(text="Verbindung getrennt", fg="gray")
            self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = RobotClient(root)
    root.mainloop()
