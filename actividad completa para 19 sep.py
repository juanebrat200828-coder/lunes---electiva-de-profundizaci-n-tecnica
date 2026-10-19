
class VehiculoT1:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

# Pide los datos al usuario en la terminal
marca_input = input("Ingresa la marca del vehículo: ")
modelo_input = input("Ingresa el modelo del vehículo: ")

moto_t1 = VehiculoT1(marca_input, modelo_input)
print("\n--- Resultado ---")
moto_t1.mostrar_info()


print("\n==================================================")
print(" 2. TEMA 2: HERENCIA Y REUTILIZACIÓN DE CÓDIGO")
print("==================================================")
class VehiculoT2:
    def __init__(self, marca: str):
        self.marca = marca

    def arrancar(self):
        print("El vehículo está arrancando.")

class MotoT2(VehiculoT2):
    def __init__(self, marca: str, cilindraje: int):
        super().__init__(marca)
        self.cilindraje = cilindraje

# Pide los datos de la moto
marca_moto = input("Ingresa la marca de la moto: ")
cilindraje_moto = int(input("Ingresa el cilindraje (ejemplo: 150): "))

moto_t2 = MotoT2(marca_moto, cilindraje_moto)
print("\n--- Resultado ---")
print(f"Marca: {moto_t2.marca}")
print(f"Cilindraje: {moto_t2.cilindraje} cc")
moto_t2.arrancar()


print("\n==================================================")
print(" 3. TEMA 3: POLIMORFISMO (DUCK TYPING)")
print("==================================================")
class MotoPoli:
    def arrancar(self):
        print("La moto arranca con su botón.")

class CarroPoli:
    def arrancar(self):
        print("El carro arranca con su llave.")

def iniciar_vehiculo(vehiculo):
    vehiculo.arrancar()

iniciar_vehiculo(MotoPoli())
iniciar_vehiculo(CarroPoli())


print("\n==================================================")
print(" 4. TEMA 4: ENCAPSULAMIENTO Y @PROPERTY")
print("==================================================")
class CuentaBancaria:
    def __init__(self, titular: str, saldo: float):
        self.titular = titular
        self.__saldo = saldo

    def depositar(self, monto: float):
        if monto > 0:
            self.__saldo += monto
            print("Depósito realizado con éxito.")
        else:
            print("Monto inválido.")

    @property
    def saldo(self) -> float:
        return self.__saldo

cuenta = CuentaBancaria("Carlos", 5000.0)
cuenta.depositar(1000.0)
print(f"Titular: {cuenta.titular}")
print(f"Saldo actual: {cuenta.saldo}")


print("\n==================================================")
print(" PROPUESTO 1: SISTEMA DE CALIFICACIONES")
print("==================================================")
class Estudiante:
    def __init__(self, nombre: str):
        self.__nombre = nombre
        self.__notas = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def notas(self) -> list:
        return self.__notas.copy()

    def agregar_nota(self, nota: float):
        if 0.0 <= nota <= 5.0:
            self.__notas.append(nota)
        else:
            raise ValueError("La nota debe estar entre 0.0 y 5.0.")

    def calcular_promedio(self) -> float:
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

est = Estudiante("Ana")
est.agregar_nota(4.5)
est.agregar_nota(3.8)
est.agregar_nota(5.0)
print(f"Estudiante: {est.nombre}")
print(f"Notas registradas: {est.notas}")
print(f"Promedio académico: {round(est.calcular_promedio(), 2)}")


print("\n==================================================")
print("  PROPUESTO 2: TARJETAS DE CRÉDITO")
print("==================================================")
class TarjetaCredito:
    def __init__(self, titular: str):
        self.titular = titular

    def calcular_cashback(self, monto: float) -> float:
        return 0.0

class TarjetaGold(TarjetaCredito):
    def calcular_cashback(self, monto: float) -> float:
        return monto * 0.02

class TarjetaBlack(TarjetaCredito):
    def calcular_cashback(self, monto: float) -> float:
        return monto * 0.05

tarjetas = [
    TarjetaCredito("Ana"),
    TarjetaGold("Luis"),
    TarjetaBlack("Marta")
]
monto_compra = 1000.0

print(f"Cálculo de Cashback para una compra de ${monto_compra:.2f}:\n")
for tarjeta in tarjetas:
    cashback = tarjeta.calcular_cashback(monto_compra)
    print(f"Titular: {tarjeta.titular} | Categoría: {tarjeta.__class__.__name__} | Cashback: ${cashback:.2f}")