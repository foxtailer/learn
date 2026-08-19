org 100h
use16

_beg:
    mov ax,0b800h
    mov es,ax
    mov di,0
    mov ah,31
    mov al,1
    mov [es:di],ax
    mov ah,10h
    int 16h
    int 20h
