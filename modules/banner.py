from .bootstrapy import Strapy
def banner():
	logo = Strapy.BOLD + """
  ______   __                      _______               __
 /      \ /  |                    /       \             /  |
/$$$$$$  |$$/   ______    ______  $$$$$$$  |  ______   _$$ |_
$$ | _$$/ /  | /      \  /      \ $$ |__$$ | /      \ / $$   |
$$ |/    |$$ |/$$$$$$  | $$$$$$  |$$    $$< /$$$$$$  |$$$$$$/
$$ |$$$$ |$$ |$$ |  $$ | /    $$ |$$$$$$$  |$$ |  $$ |  $$ | __
$$ \__$$ |$$ |$$ \__$$ |/$$$$$$$ |$$ |__$$ |$$ \__$$ |  $$ |/  |
$$    $$/ $$ |$$    $$ |$$    $$ |$$    $$/ $$    $$/   $$  $$/
 $$$$$$/  $$/  $$$$$$$ | $$$$$$$/ $$$$$$$/   $$$$$$/     $$$$/
              /  \__$$ | """+ Strapy.WHITE +"""Amazing World | v.0.01"""+ Strapy.END+ """ 
              $$    $$/
               $$$$$$/  

"""+Strapy.BGCYAN + Strapy.BOLD + """Twitter"""+Strapy.END+""" ~ @joaquimroque_
""" + Strapy.END
	print(logo)

def menu():
	menu = Strapy.WHITE + Strapy.BOLD + """
	[1] ~ JOGAR
	[2] ~ VER QUESTÕES SALVAS
	[3] ~ OUTRO
	[4] ~ GOOGLE
	""" + Strapy.END

	print(menu)