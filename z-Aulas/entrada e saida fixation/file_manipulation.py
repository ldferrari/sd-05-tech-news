file = open("arquivo.txt", mode="w")

file.write("nome idade\n")
file.write("Maria 45\n")
file.write("Miguel 33\n")

print("Túlio 22", file=file)

LINES = ["ALBERTO 34\n", "Betina 22\n", "João 42\n"]

file.writelines(LINES)

file.close()
