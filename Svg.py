import os
import Rhino
import scriptcontext
import rhinoscriptsyntax as rs

rs.Command( "_SaveAsSVG _Pause c:\\Temp\\temp.svg _Enter")
os.system('cmd /k cd c:\Temp\ && file2clip.exe "temp.svg" && exit') 
