class Mascota:
    def __init__(self, nombre, tipo, edad):
        self._nombre = nombre  # atributo privado
        self._tipo = tipo      # atributo privado
        self.edad = edad       # atributo público

    def __str__(self):
        return f"Mascota: Nombre: {self._nombre}, Tipo: {self._tipo}, Edad: {self.edad} años"

class Dueño:
    def __init__(self, nombre, telefono):
        self._nombre = nombre     # atributo privado
        self._telefono = telefono # atributo privado
        self.mascotas = []        # lista para almacenar las mascotas del dueño

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def __str__(self):
        mascotas_info = "\n".join(str(mascota) for mascota in self.mascotas)
        return f"Dueño: Nombre: {self._nombre}, Teléfono: {self._telefono}\nMascotas:\n{mascotas_info}"

class Consulta:
    def __init__(self, fecha, motivo, mascota):
        self.fecha = fecha    # atributo público
        self.motivo = motivo  # atributo público
        self.mascota = mascota  # instancia de Mascota

    def __str__(self):
        return f"Consulta - Fecha: {self.fecha}, Motivo: {self.motivo}, Mascota: {self.mascota._nombre}"

mascota1 = Mascota("Porfilio", "Perro", 5)
mascota2 = Mascota("Tertulio", "Gato", 2)

dueno1 = Dueño("Juan Pérez", "123456789")
dueno1.agregar_mascota(mascota1, mascota2)

consulta1 = Consulta("2024-10-31", "Vacunación", mascota1, mascota2)

print(mascota1, mascota2)
print(dueno1)
print(consulta1)


