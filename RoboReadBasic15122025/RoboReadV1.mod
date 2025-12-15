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
            SocketReceive clientSock \Str:=cmdStr;
            TPWrite "Empfange: " + cmdStr;

            IF cmdStr = "ROUTINE1" THEN
                Routine1;
            ELSEIF cmdStr = "ROUTINE2" THEN
                Routine2;
            ELSE
                TPWrite "Unbekannter Befehl.";
            ENDIF

            SocketClose clientSock;
            TPWrite "Verbindung getrennt.";
            cmdStr := "";
        ENDWHILE
    ENDPROC

    PROC Routine1()
        TPWrite "Routine1 wurde ausgeführt.";
    ENDPROC

    PROC Routine2()
        TPWrite "Routine2 wurde ausgeführt.";
    ENDPROC
ENDMODULE
