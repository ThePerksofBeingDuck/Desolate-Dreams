extends AnimatedSprite2D

var move_direction = 0
var speed = 200
var animated_sprite

func _process(delta):
	move_direction = Vector2.ZERO
	if Input.is_action_pressed("ui_left"):
		move_direction.x -= 1
	if Input.is_action_pressed("ui_right"):
		move_direction.x += 1
		
