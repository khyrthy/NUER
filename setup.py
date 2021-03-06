import cx_Freeze

exe = [cx_Freeze.Executable("NU-ER.py", base = "Win32GUI", icon="icon.ico")] # <-- HERE

cx_Freeze.setup(
    name = "Nao's Universe : Endless Run",
    version = "0.1.02",
    options = {"build_exe": {"packages": ["pygame", "random", "time"],  
        "include_files": ["Assets", "savegame.dat", "icon.png"]}},
    executables = exe
) 