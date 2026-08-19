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
    loop Next_fase

    mov ah,10h
    int 16h
    int 20h
