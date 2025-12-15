print("Hello Ubuntu")
import subprocess

def ping_host(ip):
    try:
        result = subprocess.run(
            ["ping", "-c", "1", ip],  # "-c 1" = 1 Ping senden
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception as e:
        print(f"Fehler beim Pingen: {e}")
        return False

if ping_host("192.168.125.1"):
    print("Roboter erreichbar!")
else:
    print("Keine Verbindung.")
