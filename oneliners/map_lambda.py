txt = ["perfect anonimous", "firefox", "global scope"]

print(list(map(lambda s:(True, s) if "anonimous" in s else (False, s), txt)) == 
          [(True, s) if "anonimous" in s else (False, s) for s in txt]
)