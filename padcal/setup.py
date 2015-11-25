from cx_Freeze import setup, Executable


setup(
    name = "PADCAL" ,
    version = "1.0" ,
    description = "Calculator for NET Emission of PADCAL Mine" ,
    executables = [Executable("main.py")]  ,
)
