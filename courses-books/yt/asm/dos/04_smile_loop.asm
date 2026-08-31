org 100h

Begin:
    mov ax,0b800h
    mov es,ax
    mov di,0
    mov al,1
    mov ah,31
    mov cx,2000

Next_fase:
    mov [es:di],ax
    add di,2
    
    push ax
    push cx

    ; Delay
    mov ah, 86h         ; BIOS function: Wait / Delay
    mov cx, 0000h       ; Старшая часть 5000 (0x0000)
    mov dx, 1388h       ; Младшая часть 5000 (0x1388)
    int 15h             ; Call BIOS interrupt
    
    pop cx
    pop ax

    loop Next_fase

    mov ah,10h
    int 16h
    int 20h

