"""
Generador de Reporte de Ventas Consolidadas (app de escritorio).

El usuario elige un rango de fechas y una carpeta de salida, y la app genera
el Excel consolidado (Bsale + Wivo + Notas de Crédito + Notas de Débito) con
exactamente los mismos cálculos y columnas que el backend original.

La primera vez que se abre, pide el archivo de credenciales (que se guarda como
.env en esta carpeta). Las siguientes veces ya no lo vuelve a pedir.
"""
import os
import shutil
import sys
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ENV_PATH = os.path.join(BASE_DIR, '.env')


# ==============================================================================
# CONFIGURACIÓN INICIAL (primera vez): cargar el archivo de credenciales
# ==============================================================================
def _env_tiene_db(path):
    if not os.path.exists(path):
        return False
    try:
        with open(path, 'r', encoding='utf-8') as f:
            contenido = f.read()
    except OSError:
        return False
    return 'DB_HOST' in contenido and 'DB_NAME' in contenido


def asegurar_credenciales():
    """Si no hay .env válido, pide el archivo de credenciales una sola vez."""
    if _env_tiene_db(ENV_PATH):
        return

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(
        "Configuración inicial",
        "Es la primera vez que abres la aplicación en este equipo.\n\n"
        "A continuación selecciona el archivo de credenciales que te enviaron "
        "(por ejemplo 'credenciales_dcic.env').\n\n"
        "Solo tendrás que hacerlo esta vez.")

    while True:
        path = filedialog.askopenfilename(
            title="Selecciona el archivo de credenciales",
            filetypes=[("Archivos de credenciales", "*.env *.txt"), ("Todos los archivos", "*.*")])

        if not path:
            if messagebox.askretrycancel(
                    "Sin archivo",
                    "No seleccionaste ningún archivo.\n¿Quieres reintentar?"):
                continue
            messagebox.showerror(
                "Configuración cancelada",
                "No se puede continuar sin el archivo de credenciales.")
            root.destroy()
            sys.exit(1)

        try:
            with open(path, 'r', encoding='utf-8') as f:
                contenido = f.read()
        except OSError as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo:\n{e}")
            continue

        if 'DB_HOST' not in contenido or 'DB_NAME' not in contenido:
            messagebox.showerror(
                "Archivo inválido",
                "El archivo seleccionado no parece contener las credenciales "
                "correctas (faltan DB_HOST / DB_NAME).\n\n"
                "Revisa que sea el archivo que te enviaron.")
            continue

        try:
            shutil.copyfile(path, ENV_PATH)
        except OSError as e:
            messagebox.showerror("Error", f"No se pudo guardar la configuración:\n{e}")
            continue

        messagebox.showinfo(
            "Listo",
            "Credenciales guardadas correctamente.\n"
            "No se volverán a pedir en este equipo.")
        break

    root.destroy()


# --- Asegurar credenciales ANTES de arrancar Django ---
asegurar_credenciales()

import django  # noqa: E402

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from tkcalendar import DateEntry  # noqa: E402
from reporte import generar_reporte  # noqa: E402


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Generador de Reporte de Ventas")
        self.resizable(False, False)

        self.output_dir = os.getcwd()
        self.dir_display_var = tk.StringVar()

        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(expand=True, fill=tk.BOTH)

        ttk.Label(main_frame, text="Rango de Fechas del Reporte",
                  font=('Helvetica', 11, 'bold')).grid(
            row=0, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)

        ttk.Label(main_frame, text="Fecha de Inicio:").grid(
            row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.start_date_entry = DateEntry(main_frame, width=15, date_pattern='dd/mm/yyyy', locale='es_ES')
        self.start_date_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        ttk.Label(main_frame, text="Fecha de Fin:").grid(
            row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.end_date_entry = DateEntry(main_frame, width=15, date_pattern='dd/mm/yyyy', locale='es_ES')
        self.end_date_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        ttk.Separator(main_frame, orient='horizontal').grid(
            row=3, column=0, columnspan=2, sticky='ew', pady=15)

        ttk.Label(main_frame, text="Directorio de Salida",
                  font=('Helvetica', 11, 'bold')).grid(
            row=4, column=0, columnspan=2, pady=(0, 5), sticky=tk.W)

        dir_frame = ttk.Frame(main_frame)
        dir_frame.grid(row=5, column=0, columnspan=2, sticky='ew')
        dir_frame.columnconfigure(0, weight=1)
        ttk.Entry(dir_frame, textvariable=self.dir_display_var, state='readonly').grid(
            row=0, column=0, sticky='ew', padx=(0, 5))
        ttk.Button(dir_frame, text="Examinar...", command=self.select_output_directory).grid(
            row=0, column=1)

        self.status_var = tk.StringVar(value="")
        ttk.Label(main_frame, textvariable=self.status_var, foreground='gray').grid(
            row=6, column=0, columnspan=2, pady=(10, 0), sticky=tk.W)

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=7, column=0, columnspan=2, pady=(20, 0), sticky=tk.E)
        self.generate_btn = ttk.Button(button_frame, text="Generar Excel", command=self.on_generate)
        self.generate_btn.pack(side=tk.RIGHT, padx=(5, 0))
        ttk.Button(button_frame, text="Salir", command=self.destroy).pack(side=tk.RIGHT)

        main_frame.columnconfigure(1, weight=1)
        self.update_dir_display()
        self._center()

    def _center(self):
        self.update_idletasks()
        w = self.winfo_reqwidth()
        h = self.winfo_reqheight()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"+{x}+{y}")

    def update_dir_display(self):
        display_path = self.output_dir
        if len(display_path) > 45:
            display_path = "..." + display_path[-42:]
        self.dir_display_var.set(f"📁 {display_path}")

    def select_output_directory(self):
        directory = filedialog.askdirectory(
            parent=self,
            title="Seleccionar directorio de salida",
            initialdir=self.output_dir
        )
        if directory:
            self.output_dir = directory
            self.update_dir_display()

    def _set_status(self, msg):
        self.status_var.set(msg)

    def on_generate(self):
        start_date = self.start_date_entry.get_date()
        end_date = self.end_date_entry.get_date()

        if start_date > end_date:
            messagebox.showerror(
                "Error de Fechas",
                "La fecha de inicio no puede ser posterior a la fecha de fin.",
                parent=self)
            return

        self.generate_btn.config(state=tk.DISABLED)
        self._set_status("Generando reporte, por favor espera...")

        def worker():
            try:
                output_path = generar_reporte(
                    start_date=start_date,
                    end_date=end_date,
                    output_dir=self.output_dir,
                    data_source='Testing',
                    log=lambda m: self.after(0, self._set_status, m),
                )
                self.after(0, self._on_success, output_path)
            except Exception as e:  # noqa: BLE001
                import traceback
                traceback.print_exc()
                self.after(0, self._on_error, str(e))

        threading.Thread(target=worker, daemon=True).start()

    def _on_success(self, output_path):
        self.generate_btn.config(state=tk.NORMAL)
        self._set_status("¡Listo!")
        messagebox.showinfo(
            "Exportación Completa",
            f"El archivo se ha generado con éxito en:\n{output_path}",
            parent=self)

    def _on_error(self, msg):
        self.generate_btn.config(state=tk.NORMAL)
        self._set_status("Ocurrió un error.")
        messagebox.showerror(
            "Error de Exportación",
            f"Ocurrió un error inesperado:\n{msg}",
            parent=self)


if __name__ == '__main__':
    App().mainloop()
