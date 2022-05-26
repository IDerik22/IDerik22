extends Area2D



	



func _on_Area2D_body_exited(_body):
	get_tree().change_scene("res://next.tscn")
