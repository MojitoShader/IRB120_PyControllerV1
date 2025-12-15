import socket

ROBOT_IP = "192.168.125.1"    # IP-Adresse des Roboters (an Ihr Setup anpassen)
ROBOT_PORT = 1025            # Port muss mit dem im RAPID-Programm übereinstimmen

# Socket-Verbindung zum Roboter herstellen
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((ROBOT_IP, ROBOT_PORT))
    print(f"Verbunden mit Roboter {ROBOT_IP}:{ROBOT_PORT}")
    
    # Beispieldaten senden (z.B. Befehl zum Starten einer Routine)
    command = input("Geben Sie den Routinen-Befehl ein (z.B. ROUTINE1): ")
    sock.sendall(command.encode('utf-8'))
    print("Befehl gesendet. Warte auf Antwort/Abschluss...")
    
    # (Optional) Auf Bestätigung vom Roboter warten - falls der Roboter etwas zurücksendet
    try:
        sock.settimeout(5.0)  # Timeout für Empfang
        response = sock.recv(1024)
        if response:
            print("Roboter-Antwort:", response.decode('utf-8'))
    except socket.timeout:
        print("Keine Antwort vom Roboter (Timeout).")
