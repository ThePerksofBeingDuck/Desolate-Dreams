extends Node2D

@onready var new_world_button = $Control/NewWorldButton
@onready var world_list = $Control/WorldList

func _ready():
	new_world_button.pressed.connect(_on_NewWorldButton_pressed)
	update_world_list()

func update_world_list():
	# Here you should update the world_list with the existing worlds
	# If there are no worlds, display a message saying there are no existing worlds
	pass

func _on_NewWorldButton_pressed():
	get_tree().change_scene("res://NewWorld.tscn")
