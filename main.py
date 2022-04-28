import sys
sys.path.insert(1, './modules')
from modules import *
from src.totareadme import readme
import pandas as pnd
import notas as jmp
import numpy as np

array_ejercicios = {
  1: 'module.funtion()'
}

if __name__ == "__main__":
    readme('C:/Users/marti/Documents/GitHub/serie-de-notas')

    #--- CREACION DE UN DATAFRAME ----
    observaciones = pnd.DataFrame({'NOTAS':np.array([3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16])})

    #--- ANALISIS DE UNA CARACTERISTICA ---
    stats = jmp.notas(observaciones['NOTAS'])
    stats.analisisCaracteristica()