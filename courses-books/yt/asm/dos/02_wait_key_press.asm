org 100h

Start:
    mov ah, 9  ; 9 - number of 'Print String' function
    mov dx, String
    int 21h  ; DOS Function Dispatcher

    mov ah, 10h  ; Read Extended Keystroke function
    int 16h  ; BIOS Keyboard Services

    int 20h

String db 'Press any key...$'
