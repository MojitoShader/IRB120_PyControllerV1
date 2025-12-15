! ------------------------------------------------------------------
! Module: RemoteControl
! Description:
!   Simple TCP socket server module for ABB Rapid controllers.
!   Listens on all interfaces (0.0.0.0) port 1025 and accepts a
!   single client connection at a time. Receives a plain-text
!   command string and executes the corresponding routine.
!
! Usage:
!   - Send the ASCII string "ROUTINE1" to trigger `Routine1`.
!   - Send the ASCII string "ROUTINE2" to trigger `Routine2`.
!
! Behavior:
!   - Accepts a client and keeps the connection open to process
!     multiple commands until the client disconnects or sends
!     "CLOSE". Unknown commands are reported via TPWrite.
!
! Notes:
!   - Intended for testing/demonstration. Add authentication and
!     proper error handling before use in production.
! ------------------------------------------------------------------
MODULE RemoteControl
    VAR socketdev listenSock;
    VAR socketdev clientSock;
    VAR string cmdStr;

    PROC socket_loop()
        SocketCreate listenSock;
        SocketBind listenSock, "0.0.0.0", 1025;
        SocketListen listenSock;
        TPWrite "Warte auf Verbindung...";

        WHILE TRUE DO
            SocketAccept listenSock, clientSock;
            TPWrite "Client verbunden.";
            cmdStr := "";

            WHILE TRUE DO
                SocketReceive clientSock \Str:=cmdStr;
                IF cmdStr = "" THEN
                    TPWrite "Keine Daten erhalten - Client vermutlich getrennt.";
                    EXIT;
                ENDIF
                TPWrite "Empfange: " + cmdStr;

                IF cmdStr = "ROUTINE1" THEN
                    Routine1;
                ELSEIF cmdStr = "ROUTINE2" THEN
                    Routine2;
                ELSEIF cmdStr = "CLOSE" THEN
                    TPWrite "Client fordert Trennung an.";
                    EXIT;
                ELSE
                    TPWrite "Unbekannter Befehl.";
                ENDIF

                cmdStr := "";
            ENDWHILE

            SocketClose clientSock;
            TPWrite "Verbindung getrennt. Warte auf neuen Client.";
        ENDWHILE
    ENDPROC

    PROC Routine1()
        TPWrite "Routine1 wurde ausgefuehrt.";
    ENDPROC

    PROC Routine2()
        TPWrite "Routine2 wurde ausgefuehrt.";
    ENDPROC
ENDMODULE
