import cx_Freeze

executables = [cx_Freeze.Executables("Snakef.py")]
cx_Freeze.setup(
    name="The Snake Game",
	options={"build.exe":{"packages":["pygame"],"include_files":["apple.png","Grass.jpg","Snake1.png","sadsnake.png"]}},
	description="Snake Game",
	executables=executables
	)