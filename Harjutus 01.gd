#Erik Teppan
#Harjutus 01
#31.03.2022
extends Node



func _ready():
	print("Tere maailm")
	var nimi = ("Peeter")
	var elu = ("100")
	var rng = RandomNumberGenerator.new()

	print(nimi," ", elu,"HP")
	print(len(nimi))
	print(int(elu) + 2)
	rng.randomize()
	var num = round(rng.randf_range(1, 19))
	print(num)
