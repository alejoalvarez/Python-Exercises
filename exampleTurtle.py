class Persona:
    name = 'Kevin'
    lastname = 'Guzmán'

    @staticmethod
    def pensar():
        print('Pensando')

    @classmethod
    def saludar(cls):
        cls.name = 'Kevin Guzmán'
        print('Hola a todos mi nombre es {}'.format(cls.name))

    def saludar_calurosamente(self):
        print('Hola caballeros, mi nombre completo es {}, ¿como están todos?'.format(self.name + ' ' + self.lastname))


persona1 = Persona()
# Llamada a método de instancia
persona1.saludar_calurosamente()
# Llamada a método de clase
Persona.saludar()
# Llamada a método estático
Persona.pensar()