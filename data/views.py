from django.shortcuts import render
import requests as req 
from plotly.offline import plot
import plotly.graph_objects as go



def data_udi(request):
    """
    funcion que hace petición de datos en la api y retorna los como etiquetas a renderizar
    """
    udi, udi_date = [], [],        

    # pedir datos a la api con el token
    response = req.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP1/datos', 
                headers={'Bmx-Token': 'bfec49c15267dedac48b73225be0ba591c32c5f69c1126c72e6a52b1320b86b9'})
    
    # bucle de los datos
    for data in response.json()["bmx"]["series"][0]["datos"]:
        
        # verificamos que no sean datos vacíos
        if data["dato"]!="N/E":
            

            # lista para renderizar de las udi
            udi.append(float(data["dato"]))
            # lista para renderizar de las fechas
            udi_date.append(str(data["fecha"]))
    
    # union de udi con fechas
    udi_date = zip(udi_date, udi)
    return render(request, 'udi.html', context={
        'udi_date': udi_date,
        'mean':sum(udi)/len(udi),
        'min': min(udi),
        'max': max(udi)

    } )


def data_peso_dolar(request):
    """
    funcion que hace petición de datos en la api y retorna los como etiquetas a renderizar
    """
    peso_dolar, peso_dolar_date = [], [],        
   
    # pedir datos a la api con el token
    response2 = req.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF17868/datos', 
                    headers={'Bmx-Token': 'bfec49c15267dedac48b73225be0ba591c32c5f69c1126c72e6a52b1320b86b9'})
    
    # bucle de los datos
    for data in response2.json()["bmx"]["series"][0]["datos"]:
        
        # verificamos que no sean datos vacíos
        if data["dato"]!="N/E":
            
            # lista para renderizar de la tasa peso-dolar
            peso_dolar.append(float(data["dato"]))
            # lista para renderizar de las fechas
            peso_dolar_date.append(str(data["fecha"]))
    
    # union de las tasas con fechas
    peso = zip(peso_dolar_date, peso_dolar)
    return render(request, 'peso.html', context={
        'data': peso_dolar,
        'mean':sum(peso_dolar)/len(peso_dolar),
        'min': min(peso_dolar),
        'max': max(peso_dolar),
        'peso': peso,

    } )


def udi_plot_view(request):

    
    udi, udi_date = [], [],        

    # pedir datos a la api con el token
    response = req.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/SP1/datos', 
                headers={'Bmx-Token': 'bfec49c15267dedac48b73225be0ba591c32c5f69c1126c72e6a52b1320b86b9'})
    
    # bucle de los datos
    for data in response.json()["bmx"]["series"][0]["datos"]:
        
        # verificamos que no sean datos vacíos
        if data["dato"]!="N/E":
            

            # lista para renderizar de las udi
            udi.append(float(data["dato"]))
            # lista para renderizar de las fechas
            udi_date.append(str(data["fecha"]))


    # lista de gráficos
    graphs = []

    # agregando prmer gráfico tipo lines
    graphs.append(
        go.Scatter(x=udi_date, y=udi, mode='lines', name='udi')
    )

    # agregando segundo gráfico tipo lines
    udi_min =[min(udi) for i in range(len(udi))] 
    graphs.append(
        go.Scatter(x=udi_date, y=udi_min, mode='lines', opacity=0.8, name='minimo')
   )
    # agregando tercer gráfico tipo lines
    udi_max =[max(udi) for i in range(len(udi))] 
    graphs.append(
        go.Scatter(x=udi_date, y=udi_max, mode='lines', opacity=0.8, 
                   name='maximo')
   )
   # agregando cuarto gráfico tipo lines
    udi_median =[sum(udi)/len(udi) for i in range(len(udi))] 
    graphs.append(
        go.Scatter(x=udi_date, y=udi_median, mode='lines', opacity=0.8, 
                  name='median')
   )
    # configuración general de la figura
    layout = {
        'title': 'Udi data',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 820,
        'width': 1640,
    }

    # HTML para el plot
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')

    return render(request, 'grap.html', 
                  context={'plot_div': plot_div})




def tasa_plot_view(request):

    
    peso_dolar, peso_dolar_date = [], [],         

    # pedir datos a la api con el token
    response2 = req.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF17868/datos', 
                    headers={'Bmx-Token': 'bfec49c15267dedac48b73225be0ba591c32c5f69c1126c72e6a52b1320b86b9'})
    
    # bucle de los datos
    for data in response2.json()["bmx"]["series"][0]["datos"]:
        
        # verificamos que no sean datos vacíos
        if data["dato"]!="N/E":
            

            # lista para renderizar de las udi
            peso_dolar.append(float(data["dato"]))
            # lista para renderizar de las fechas
            peso_dolar_date.append(str(data["fecha"]))


    # lista de gráficos
    graphs = []

    # agregando prmer gráfico tipo lines
    graphs.append(
        go.Scatter(x=peso_dolar_date, y=peso_dolar, mode='lines', name='peso dolar tasa')
    )

    # agregando segundo gráfico tipo lines
    tasa_min =[min(peso_dolar) for i in range(len(peso_dolar))] 
    graphs.append(
        go.Scatter(x=peso_dolar_date, y=tasa_min, mode='lines', opacity=0.8, name='minimo')
   )
    # agregando tercer gráfico tipo lines
    tasa_max =[max(peso_dolar) for i in range(len(peso_dolar))] 
    graphs.append(
        go.Scatter(x=peso_dolar_date, y=tasa_max, mode='lines', opacity=0.8, 
                   name='maximo')
   )
   # agregando cuarto gráfico tipo lines
    tasa_median =[sum(peso_dolar)/len(peso_dolar) for i in range(len(peso_dolar))] 
    graphs.append(
        go.Scatter(x=peso_dolar_date, y=tasa_median, mode='lines', opacity=0.8, 
                  name='median')
   )
    # configuración general de la figura
    layout = {
        'title': 'Tasa peso-dolar ',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 820,
        'width': 1640,
    }

    # HTML para el plot
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')

    return render(request, 'grap2.html', 
                  context={'plot_div': plot_div})

def tie_plot_view(request):
    """ 
    grafica los valores tie 
    """
    
    tie, tie_date = [], [],         

    # pedir datos a la api con el token
    response3 = req.get('https://www.banxico.org.mx/SieAPIRest/service/v1/series/SF283/datos', 
    headers={'Bmx-Token': 'bfec49c15267dedac48b73225be0ba591c32c5f69c1126c72e6a52b1320b86b9'})
    
    # bucle de los datos
    for data in response3.json()["bmx"]["series"][0]["datos"]:
        
        # verificamos que no sean datos vacíos
        if data["dato"]!="N/E":
            

            # lista para renderizar de las udi
            tie.append(float(data["dato"]))
            # lista para renderizar de las fechas
            tie_date.append(str(data["fecha"]))


    # lista de gráficos
    graphs = []

    # agregando primer gráfico tipo lines 
    graphs.append(
        go.Scatter(x=tie_date, y=tie, mode='lines', name='peso dolar tasa')
    )

    # agregando segundo gráfico tipo lines 
    tie_min =[min(tie) for i in range(len(tie))] 
    graphs.append(
        go.Scatter(x=tie_date, y=tie_min, mode='lines', opacity=0.8, name='minimo')
   )

    # agregando tercer gráfico tipo lines 
    tie_max =[max(tie) for i in range(len(tie))] 
    graphs.append(
        go.Scatter(x=tie_date, y=tie_max, mode='lines', opacity=0.8, 
                   name='maximo')
   )
   
    tie_median =[sum(tie)/len(tie) for i in range(len(tie))] 
   # agregando cuarto gráfico tipo lines 
    graphs.append(
        go.Scatter(x=tie_date, y=tie_median, mode='lines', opacity=0.8, 
                  name='median')
   )


    # configuración general de la figura
    layout = {
        'title': 'Tasa peso-dolar ',
        'xaxis_title': 'X',
        'yaxis_title': 'Y',
        'height': 820,
        'width': 16400,
    }

    # HTML para el plot
    plot_div = plot({'data': graphs, 'layout': layout}, 
                    output_type='div')

    return render(request, 'grap3.html', 
                  context={'plot_div': plot_div})

