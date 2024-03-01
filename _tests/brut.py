n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


x = "15328014"
_x = ""

for i in n:
    _x += i
    for j in n:
        _x += j
        for g in n:
            _x += g
            for h in n:
                _x += h
                for k in n:
                    _x += k
                    for l in n:
                        _x += l
                        for a in n:
                            _x += a
                            for q in n:
                                _x += q
                                if _x == x:
                                    print("Finish")
                                _x = _x[:7]
                            _x = _x[:6]
                        _x = _x[:5]
                    _x = _x[:4]
                _x = _x[:3]
            _x = _x[:2]
        _x = _x[:1]
    _x = ""
    