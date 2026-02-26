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

    def calcular_precio_servicio_adicional(self) -> float:
        """
        Calcula el costo del servicio adicional (cine integrado)
        y retorna el valor sin modificar el precio base.
        """
        if self.servicio_cine_integrado:
            return 300000
        return 0
