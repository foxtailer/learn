import datetime

class A:

    @staticmethod
    def get_carent_datatime():
        return datetime.time()

print(A.get_carent_datatime())
a = A()
print(a.get_carent_datatime())