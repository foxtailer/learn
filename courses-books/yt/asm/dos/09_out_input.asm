org 100h

Begin:
    call Wait_key
    cmp al, 27
    je Quit_prog
    cmp al, 0
    je Begin

    call Out_char
    jmp Begin

Quit_prog:
    mov al, 32
    call Out_char
    int 20h

Wait_key:
    mov ah, 10h
    int 16h
    ret

Out_char:
    push cx
    push ax
    push es

    push ax
    mov ax, 0B800h
    mov es, ax
    mov di, 0
    mov cx, 2000
    pop ax
    mov ah, 31

    Next_sym:
        mov [es:di], ax
        inc di
        inc di
        loop Next_sym

    pop es
    pop ax
    pop cx
    ret

