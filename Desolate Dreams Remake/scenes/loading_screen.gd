extends Control

@onready var timer = $Timer

func _ready():
	timer = $Timer
	timer.set_wait_time(5)  # Set the waiting time to 6 seconds
	timer.start()


func _on_Timer_timeout():
	get_tree().change_scene("res://scenes/tile_map.tscn")
