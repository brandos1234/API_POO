from consumApi import api_num
import pandas as pd

class ordenar:  

    def __init__(self):
        self.df = pd.DataFrame()
        
        

    def main(self, var, metodo):
        api = api_num('https://www.datos.gov.co/resource/ha6j-pa2r.json', var)
        print(var)
        arreglo, datos = api.consumo()
        self.datos = datos
        print(arreglo)
        ordenar.definirMetodo(self, metodo, arreglo)
        return self.df

    def ordenarDFrame(self, arreglo):
      #self.datos[self.var] = pd.Categorical(self.datos[self.var], categories=arreglo, ordered=True)

        # Ordenar el DataFrame basado en la columna categórica
      #df_ordenado = self.datos.sort_values(self.var)
        df = pd.DataFrame()
        df = self.datos
        mapa_orden = {valor: idx for idx, valor in enumerate(arreglo)}
    
    # Crear una columna temporal que asigna el valor de 'var' al índice en el mapa de orden
        df['orden_temp'] = df[self.var].map(mapa_orden)
    
    # Ordenar el DataFrame según la columna temporal
        df = df.sort_values(by='orden_temp', na_position='last')
    
    # Eliminar la columna temporal de orden
        df.drop(columns=['orden_temp'], inplace=True)
        print(df)
        return df

    def definirMetodo(self, metodo, arreglo):
        #print(arreglo)
        if metodo == 'insertion':
            self.df = ordenar.insertion(self, arreglo)
            #print('esta es la data de ordenamiento', self.data)
        elif metodo == 'Selection':
            ordenar.selection(self, arreglo)
            self.df = ordenar.selection(self, arreglo)
            #return data
        else:
            Arreglito = ordenar.quick(self, arreglo)
            self.df = ordenar.ordenarDFrame(self, Arreglito)
        return self.df

    def insertion(self, arreglo):
        for i in range(1, len(arreglo)):
            valor = arreglo[i]
            anterior = i - 1

            while anterior >= 0 and arreglo[anterior] > valor:
                arreglo[anterior + 1] = arreglo[anterior]
                anterior -= 1
        
            arreglo[anterior + 1] = valor
        print('arreglo del metodo', arreglo)
        df = ordenar.ordenarDFrame(self, arreglo)
        return df

    def selection(self, arreglo):
        for i in range(len(arreglo)):
            min = i
            for j in range(i + 1, len(arreglo)):
                if arreglo[j] < arreglo[min]:
                    min = j
            arreglo[i], arreglo[min] = arreglo[min], arreglo[i]
            df = ordenar.ordenarDFrame(self, arreglo)
        #print(arreglo)
        return df

    def quick(self, arreglo):
        base = len(arreglo)

        if base <= 1:
            return arreglo

        pivote = arreglo.pop()
        lista_derecha = []
        lista_izquierda = []

        for i in arreglo:
            if i <= pivote:
                lista_izquierda.append(i)
            else:
                lista_derecha.append(i)
    
        lista_derecha = ordenar.quick(self, lista_derecha)
        lista_izquierda = ordenar.quick(self, lista_izquierda)
        

        return lista_izquierda + [pivote] + lista_derecha

          
    




    