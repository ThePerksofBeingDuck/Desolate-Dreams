extends CharacterBody2D

const SPEED = 100
@onready var sprite = $Player

func _physics_process(_delta):
	velocity.x = Input.get_axis("Walk Left", "Walk Right")
	velocity.y = Input.get_axis("Walk Up", "Walk Down")
	velocity = velocity.normalized()*SPEED
	move_and_slide()
	if Input.is_physical_key_pressed(KEY_SHIFT):
		const SPEED = 350
	else:
		const SPEED = 200
	if velocity.length() > 0:
		if velocity.x > 0:
			sprite.play("walk_right")
		elif velocity.x < 0:
			sprite.play("walk_left")
		if velocity.y > 0:
			sprite.play("walk_down")
		elif velocity.y < 0:
			sprite.play("walk_up")
	else:
		if sprite.get_animation() == "walk_right":
			sprite.play("idle_right")
		elif sprite.get_animation() == "walk_left":
			sprite.play("idle_left")
		if sprite.get_animation() == "walk_up":
			sprite.play("idle_up")
		elif sprite.get_animation() == "walk_down":
			sprite.play("idle_down")
