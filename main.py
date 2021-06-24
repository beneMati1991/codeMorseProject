from utils import Utils

var_input = input("Ingresar palabra a traducir: ")

while var_input != "0":
    var_input_correct = var_input.lower()

    fun = Utils(var_input_correct)
    fun.soundMorse()

    var_input = input("Ingresar otra palabra a traducir (0-Stop): ")