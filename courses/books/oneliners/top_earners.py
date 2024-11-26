data = {
    "Sem":1000,
    "Din":1500,
    "Kas":2000
}

print([(k,v) for k,v in data.items() if v>1500])