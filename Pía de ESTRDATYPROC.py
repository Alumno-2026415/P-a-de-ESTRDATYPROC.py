import datetime
import pandas as pd

class TallerMecanico:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.notas = []

    def obtener_fecha_actual(self):
        return datetime.datetime.now().strftime("%m/%d/%Y")

    def mostrar_menu_principal(self):
        # Implementa la lógica para mostrar el menú principal
        pass

    def mostrar_menu_notas(self):
        # Implementa la lógica para mostrar el menú de notas
        pass

    def registrar_nota(self):
        # Implementa la lógica para registrar una nueva nota
        pass

    def cancelar_nota(self):
        # Implementa la lógica para cancelar una nota
        pass

    def recuperar_nota(self):
        # Implementa la lógica para recuperar una nota cancelada
        pass

    def consultar_por_periodo(self):
        fecha_inicial = input("Ingresa la fecha inicial (mm/dd/aaaa) (deja en blanco para 01/01/2000): ")
        fecha_final = input("Ingresa la fecha final (mm/dd/aaaa) (deja en blanco para la fecha actual): ")

        if fecha_inicial == "":
            fecha_inicial = "01/01/2000"
        if fecha_final == "":
            fecha_final = self.obtener_fecha_actual()

        # Validar que la fecha final sea igual o posterior a la fecha inicial
        if datetime.datetime.strptime(fecha_final, "%m/%d/%Y") < datetime.datetime.strptime(fecha_inicial, "%m/%d/%Y"):
            print("Error: La fecha final debe ser igual o posterior a la fecha inicial.")
            return

        notas_periodo = [nota for nota in self.notas if fecha_inicial <= nota['fecha'] <= fecha_final]

        if not notas_periodo:
            print("No hay notas para el período seleccionado.")
            return

        # Calcular el monto promedio de las notas del período
        monto_promedio = sum([nota['monto_pagar'] for nota in notas_periodo]) / len(notas_periodo)

        # Mostrar reporte tabular de notas
        print("Reporte de notas por período:")
        print(f"{'Folio':<10}{'Fecha':<12}{'Clave Cliente':<15}{'Monto a Pagar':<18}")
        for nota in notas_periodo:
            print(f"{nota['folio']:<10}{nota['fecha']:<12}{nota['clave_cliente']:<15}{nota['monto_pagar']:<18}")

        print(f"\nMonto Promedio de Notas: {monto_promedio}")

        # Opciones para exportar a CSV o Excel
        opcion_exportar = input("¿Deseas exportar el reporte? (CSV/Excel/No): ")
        if opcion_exportar.upper() == "CSV":
            self.exportar_a_csv(notas_periodo, f"ReportePorPeriodo_{fecha_inicial}_{fecha_final}.csv")
            print("Reporte exportado a CSV.")
        elif opcion_exportar.upper() == "EXCEL":
            self.exportar_a_excel(notas_periodo, f"ReportePorPeriodo_{fecha_inicial}_{fecha_final}.xlsx")
            print("Reporte exportado a Excel.")
        else:
            print("Regresando al menú principal.")

    def exportar_a_csv(self, datos, nombre_archivo):
        dataframe = pd.DataFrame(datos)
        dataframe.to_csv(nombre_archivo, index=False)

    def exportar_a_excel(self, datos, nombre_archivo):
        dataframe = pd.DataFrame(datos)
        writer = pd.ExcelWriter(nombre_archivo, engine='xlsxwriter')
        dataframe.to_excel(writer, index=False, sheet_name='Sheet1')
        writer.save()

    def ejecutar(self):
        while True:
            self.mostrar_menu_principal()
            opcion_principal = input("Selecciona una opción del menú principal: ")

            if opcion_principal == "1":
                while True:
                    self.mostrar_menu_notas()
                    opcion_notas = input("Selecciona una opción de Notas: ")

                    if opcion_notas == "1":
                        self.registrar_nota()
                    elif opcion_notas == "2":
                        self.cancelar_nota()
                    elif opcion_notas == "3":
                        self.recuperar_nota()
                    elif opcion_notas == "4":
                        self.consultar_por_periodo()
                    elif opcion_notas == "5":
                        break
                    else:
                        print("Opción no válida. Inténtalo de nuevo.")
            elif opcion_principal == "5":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")

# Ejemplo de uso
if __name__ == "__main__":
    taller = TallerMecanico()
    taller.ejecutar()
