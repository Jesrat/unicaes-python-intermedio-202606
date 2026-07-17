class MyClass:
    def __init__(self):
        print("se ejecuta al instanciar un objeto")
        self._atributo = None

    @property
    def atributo(self):
        return self._atributo

    @atributo.setter
    def atributo(self, val):
        self._atributo = val

    def set_atributo(self, val):
        self._atributo = val
