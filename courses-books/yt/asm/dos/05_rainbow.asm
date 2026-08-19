org 100h            ; .COM program starts at offset 100h (256 bytes)— DOS reserves this space for the PSP (Program Segment Prefix)

Begin:
    mov ax,0b800h    ; segment address of text-mode video memory (fixed, standard address)
    mov es,ax        ; load that address into es — es now "points to" video memory
    mov di,0         ; offset 0 — first cell on screen (top-left corner, row 0, column 0)
    mov bh,0         ; bh = counter for the current screen row (0..24), start at zero

Row_loop:
    mov al,219       ; square symbol — code for the "solid block" █ character (CP437), goes into al = low byte of ax
    mov ah,bh        ; copy the row number into ah — will be used as the color attribute
    and ah,0fh       ; keep only the lower 4 bits (0..15) — valid range for text color,
                     ; so that bh, which grows up to 24, doesn't exceed the allowed color value
    mov cx,80        ; 80 - screen length — 80 characters per screen row, counter for the inner loop

Col_loop:
    mov [es:di],ax   ; write 2 bytes at once: al (symbol) + ah (attribute) into the current video memory cell
    add di,2         ; move pointer to the next cell (each cell = 2 bytes)
    loop Col_loop     ; --cx; if cx != 0 jump — decrement cx, repeat until all 80 columns of the row are filled

    inc bh           ; move to the next row: bh = bh + 1
    cmp bh,25        ; 25 lines - screen height — compare bh against the total number of screen rows (25)
    jl Row_loop      ; jump if less — if bh < 25, there are more rows to fill, jump back to the start

    mov ah,10h       ; BIOS function: wait for a keypress (blocking read)
    int 16h          ; call BIOS keyboard interrupt — pauses here until any key is pressed
    int 20h          ; standard DOS interrupt to terminate a .COM program cleanly
