extends Node2D

@onready var play_button = $Control/PlayButton
@onready var settings_button = $Control/SettingsButton

func _ready():
	play_button.pressed.connect(_on_PlayButton_pressed)
	settings_button.pressed.connect(_on_SettingsButton_pressed)

func _on_PlayButton_pressed():
	get_tree().change_scene("res://WorldSelection.tscn")

func _on_SettingsButton_pressed():
	get_tree().change_scene("res://Settings.tscn")
