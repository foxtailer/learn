format binary
use16
org 100h

begin:
    call Our_proc

    int 20h


Our_proc:
    ret
