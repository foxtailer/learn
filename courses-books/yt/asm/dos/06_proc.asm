org 100h

Start:
    mov ax, 0b800h
    mov es, ax
    mov al, 1   ; Starting character code
    mov ah, 31  ; Color attribute
    mov cx, 254 ; End character code

Next_screen:
    mov di, 0        ; Screen memory ofset
    call Out_chars
    inc al           ; Next char
    loop Next_screen

    mov ah, 10h
    int 16h
    int 20h

Out_chars:
    mov dx, cx    ; Save outer loop index
    mov cx, 2000  ; Inner loop index

Next_face:
    mov [es:di], ax
    add di, 2
    loop Next_face

    mov cx, dx    ; Restore outer loop index
    ret
