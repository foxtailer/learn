txt = "ddsjfkj sfjskjfs sjfdsk KEY sdkfjjj jfs j  jfdjfkjs"

x = lambda s, key: s[s.find(key)-5:s.find(key)+5+len(key)] if key in s else -1
print(x(txt, "KEY"))