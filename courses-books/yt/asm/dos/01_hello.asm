org 100h          ; Указываем FASM, что делаем .COM файл для DOS

Begin:
    mov ah, 9
    mov dx, Message
    int 21h
    
    int 20h       ; Выход из программы

Message db 'Hello, world$' ; Обязательно добавьте $ в конце строки!

