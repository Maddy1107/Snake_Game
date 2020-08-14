import cx_Freeze

executables = [cx_Freeze.Executable("Snakef.py")]
cx_Freeze.setup(
    name="The Snake Game",
	#options={"build.exe":{"packages":["pygame"],"include_files":["images/apple.png","images/Grass.jpg","images/Snake1.png","images/sadsnake.png"]}},
	description="Snake Game",
	executables=executables
	)