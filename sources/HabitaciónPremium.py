from sources.Habitacion import Habitacion

""" Importamos la clase Habitacion desde el módulo Habitacion para que la clase HabitacionPremium pueda heredar de ella. """


class HabitacionPremium(Habitacion):
    def __init__(
        self,
        id,
        numero_habitacion,
        tipo_habitacion,
        precio,
        servicio_yacuzzi: bool = False,
    ):
        super().__init__(id, numero_habitacion, tipo_habitacion, precio)
        self.servicio_yacuzzi = servicio_yacuzzi

    def calcular_precio_total_yacuzzi(self) -> float:
        """Calcula el precio total de la habitación premium, incluyendo el servicio de jacuzzi si está habilitado."""

        if self.servicio_yacuzzi:
            return 50000
        return 0

    """ La clase HabitacionPremium hereda de la clase Habitacion y agrega un atributo adicional para indicar si el servicio de jacuzzi está habilitado. Además, incluye un método para calcular el precio total de la habitación premium, sumando el costo del servicio de jacuzzi si está habilitado. """
