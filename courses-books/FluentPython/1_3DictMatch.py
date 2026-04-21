def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': 2, 'authors': [*names]}:
            return names
        case {'type': 'book', 'api': 1, 'author': name}:
            return [name]  # >>> [['Douglas Hofstadter', 'Gunter E. Zeigler']]
        case {'type': 'book'}:
            raise ValueError(f"Invalid 'book' record: {record!r}") # !r call repr() of record
        case {'type': 'movie', 'director': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')
        

b1 = dict(api=2, authors=['Douglas Hofstadter', 'Gunter E. Zeigler'],
          type='book', title='Gödel, Escher, Bach')
print(get_creators(b1))


####################

food = dict(category='ice cream', flavor='vanilla', cost=199)
match food:
    case {'category': 'ice cream', **details}:
        print(f'Ice cream details: {details}')