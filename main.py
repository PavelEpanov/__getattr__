class Empty:
    def __getattr__(self, attrname): # Вызывется для неопределенного атрибута в self
        if attrname == "age":
            return 40
        else:
            raise AttributeError(attrname)

A = Empty()
print(A.age)
print(A.name)
