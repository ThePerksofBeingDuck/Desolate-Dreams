extends CharacterBody2D
#movement variables
const SPEED = 100
const SPRINT_SPEED = 200
@onready var sprite = $Player

#movement
func _physics_process(_delta):
	'''velocity.x = Input.get_axis("Walk Left", "Walk Right")
	velocity.y = Input.get_axis("Walk Up", "Walk Down")
	velocity = velocity.normalized()*SPEED
	move_and_slide()'''
	velocity.x = Input.get_axis("Walk Left", "Walk Right")
	velocity.y = Input.get_axis("Walk Up", "Walk Down")
	velocity = velocity.normalized() * SPEED
	move_and_slide()
	
	
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

#magical moves

#variables for magic

var equipped_moves = {"1": null, "2": null}
var move_fireball
var move_firecrystal

func _ready():
	#loading moves
	move_fireball = preload("res://scenes/Attacks/Fire/basic_fire_attack.tscn")
	move_firecrystal = preload("res://scenes/Attacks/Fire/fire_crystal_attck.tscn")

func _process(_delta):
	if Input.is_action_just_pressed("Attack Slot 1"):
		if equipped_moves["1"]:
			trigger_move(equipped_moves["1"])

	if Input.is_action_just_pressed("Attack Slot 2"):
		if equipped_moves["2"]:
			trigger_move(equipped_moves["2"])

func trigger_move(move_scene):
	var move_instance = move_scene.instantiate()
	add_child(move_instance)
	move_instance.global_position = global_position

func equip_move(slot, move):
	equipped_moves[slot] = move