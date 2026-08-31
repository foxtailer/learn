org 100h

Begin:
    mov sp, Lab_1
    mov ax, 9090h
    push ax
    int 20h

Lab_1:
    mov ah, 9
    mov dx, Mess
    int 21h

    int 20h

Mess db 'Message!$'

