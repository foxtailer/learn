org 100h

Start:
    mov ax, 0B800h      ; Text video segment
    mov es, ax
    mov al, 1
    mov ah, 31          ; White text on Blue background
    mov cx, 254         ; Number of ASCII characters to cycle through

Next_screen:
    mov di, 0
    push cx             ; Save outer loop counter
    call Out_char       
    inc al

    ; --- DELAY START ---
    ; int 15h/ah=86h uses a 64-bit value in CX:DX (microseconds)
    ; 100,000 microseconds = 0x000186A0
    mov ah, 86h
    mov cx, 0001h       ; High word of delay
    mov dx, 86A0h       ; Low word of delay (100,000 ms)
    int 15h
    ; --- DELAY END ---

    pop cx              ; Restore outer loop counter
    loop Next_screen

    ; Wait for keystroke
    mov ah, 10h
    int 16h
    
    ; Exit to DOS
    int 20h

Out_char:
    mov cx, 2000        ; 80x25 screen size

Next_face:
    mov [es:di], ax     
    add di, 2           
    loop Next_face

    ret

