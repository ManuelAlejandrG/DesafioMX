from django.urls import path
from data import views
from django.conf.urls import url

urlpatterns = [


    path('grap1', views.udi_plot_view),
    path('grap2', views.tasa_plot_view),
    path('grap3', views.tie_plot_view),
    path('udi',views.data_udi ),
    path('tasa', views.data_peso_dolar)
    

]