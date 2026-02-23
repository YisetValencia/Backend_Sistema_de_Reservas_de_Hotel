from sources.Habitacion import Habitacion


class HabitacionPresidencial(Habitacion):
    """
    Representa una habitación presidencial con servicio opcional
    de cine integrado.
    """

    def __init__(
        self,
        id,
        numero_habitacion,
        tipo_habitacion,
        precio,
        servicio_cine_integrado: bool = False,
    ):
        super().__init__(id, numero_habitacion, tipo_habitacion, precio)
        self.servicio_cine_integrado = servicio_cine_integrado

    def calcular_costo(self, dias: int) -> float:
        """
        Calcula el costo del servicio adicional (cine integrado)
        y retorna el valor total.
        """
        if self.servicio_cine_integrado:
            return (self.precio * dias) + 100000

        return self.precio * dias
