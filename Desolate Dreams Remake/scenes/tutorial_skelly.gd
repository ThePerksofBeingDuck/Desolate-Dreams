extends CharacterBody2D


@onready var sprite = $skelly

func _ready():
	sprite.play("default")

