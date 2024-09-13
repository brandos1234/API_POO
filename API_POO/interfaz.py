import tkinter as tk
import customtkinter as ctk
import util.generic as utl
from tkinter import messagebox
from CTkMessagebox import CTkMessagebox
from ordenamiento import ordenar
from tkinter import ttk
import os

class interfaz:
    def capDatos(self):
        met = self.cmbMetodoOrdenamiento.get()
        metodo = met
            
        self.var = self.cmbVariableNumerica.get()
        
        variable = self.var
        if metodo == "Seleccione uno" or self.var == "Seleccione uno":
            
            CTkMessagebox(title='Advertencia',
                              message='Debe seleccionar método y variable')
            return  
        data = ordenar.main(self, self.var, metodo)
        print('esta es la data de interfaz', data)
        
        
        for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
    
    
        if not data.empty:
        
                tree = ttk.Treeview(self.scrollable_frame, columns=list(data.columns), show="headings")

        
                for col in data.columns:
                        tree.heading(col, text=col)
                        tree.column(col, width=100, stretch=tk.YES)  

        
                for index, row in data.iterrows():
                        tree.insert("", tk.END, values=list(row))
        
        
                vsb = ttk.Scrollbar(self.scrollable_frame, orient="vertical", command=tree.yview)
                hsb = ttk.Scrollbar(self.scrollable_frame, orient="horizontal", command=tree.xview)
                tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
            
            
                tree.grid(row=0, column=0, sticky='nsew')
                vsb.grid(row=0, column=1, sticky='ns')
                hsb.grid(row=1, column=0, sticky='ew')
                
                self.scrollable_frame.grid_rowconfigure(0, weight=1)
                self.scrollable_frame.grid_columnconfigure(0, weight=1)

        else:
                lbl = ctk.CTkLabel(master=self.scrollable_frame, text="No hay datos disponibles")
                lbl.pack(pady=5, fill='x')    
        
    

    def __init__(self):       

        app = ctk.CTk()
        app.title('Ordenamiento')
        w, h = app.winfo_screenwidth(), app.winfo_screenheight()
        app.geometry("950x650")
        app.config(bg="#fcfcfc")
        app.resizable(width=0, height=0)
    
        ruta_base = os.getcwd()
        nombre_imagen = 'data-processing.png' 
        ruta_completa = os.path.join(ruta_base, 'API_POO', 'API_POO', 'imagenes', nombre_imagen)
        logo = utl.leer_imagen(ruta_completa, (200, 200))

        frame_logo = tk.Frame(app, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frame_logo.pack(side='left', expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='#3a7ff6')
        label.place(x=0, y=0, relwidth=1, relheight=1)


        frame_form = tk.Frame(app, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side='right', expand=tk.YES, fill=tk.BOTH)


        frame_form_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_form_top.pack(side='top', fill=tk.X)
        title = tk.Label(frame_form_top, text='Ordenamiento de datos', font=('Times', 25), fg='#666a88', bg='#fcfcfc', pady=40)
        title.pack(expand=tk.YES, fill=tk.BOTH)

        frame_from_fill = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_from_fill.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        lblMetodoOrdenamiento = ctk.CTkLabel(frame_from_fill,
                               text="Seleccione el método deseado:",
                               font=("Times", 18),
                               anchor='w'

                               )
        lblMetodoOrdenamiento.pack(fill=tk.X, padx=30, pady=15)

        self.cmbMetodoOrdenamiento = ctk.CTkComboBox(frame_from_fill, font=('Times', 18),
                        values=["insertion", "Selection", "quick"] )
        self.cmbMetodoOrdenamiento.set("Seleccione uno")
        self.cmbMetodoOrdenamiento.pack(fill=tk.X, padx=30, pady=5)



        lblVariable = ctk.CTkLabel(frame_from_fill,
                               text="Seleccione el método deseado:",
                               font=("Times", 18),
                               anchor='w',
                               )
        lblVariable.pack(fill=tk.X, padx=30, pady=15)


        self.cmbVariableNumerica = ctk.CTkComboBox(frame_from_fill, font=('Times', 18),
                        values=["cantidad", "codigo_dane", "departamento"])
        self.cmbVariableNumerica.set("Seleccione uno")
        self.cmbVariableNumerica.pack(fill=tk.X, padx=30, pady=5)


        btnConsultar = ctk.CTkButton(frame_from_fill, text="Consultar", font=('Times', 18), command=self.capDatos)
        btnConsultar.pack(fill=tk.X, padx=30, pady=20)
       

        self.scrollable_frame = ttk.Scrollbar(frame_from_fill)
        self.scrollable_frame.pack(fill=tk.X, padx=30, pady=20)
        

        app.mainloop()


interfaz()