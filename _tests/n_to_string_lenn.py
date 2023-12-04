def convert(n: int) -> str:
    """
    Return a stging len n
    """
    return "".join(map(str, range(n+1)))

# join worcs faster then concatination

print(convert(12))