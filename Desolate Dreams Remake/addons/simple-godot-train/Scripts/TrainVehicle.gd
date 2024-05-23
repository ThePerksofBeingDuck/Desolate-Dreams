# Sits on top of two TrainWheels to move along a Track
class_name TrainVehicle
extends Node2D

signal towed_mass_changed

@export var wheel_distance = 58
@export var follow_distance = 26
@export var mass = 10

var towed_mass = 0
var total_mass = mass

@onready var front_wheel : TrainWheel = $TrainWheel
@onready var back_wheel : TrainWheel = $TrainWheel2
@onready var body : Node2D = $Body

func _ready():
	front_wheel.moved.connect(back_wheel.move_as_follower)

func _process(delta):
	global_position = lerp(global_position, front_wheel.global_position, 0.8)
	body.look_at(back_wheel.global_position)

# Place this vehicle (and all of its wheels) on the track
func add_to_track(track: Path2D, offset = 1):
	front_wheel.set_track(track)
	back_wheel.set_track(track)
	front_wheel.progress = offset
	back_wheel.follow(front_wheel, wheel_distance)
	global_position = front_wheel.global_position

# Link another TrainVehicle to follow this one
func set_follower_car(car):
	car.add_to_track(back_wheel.current_track)
	car.front_wheel.follow(back_wheel, follow_distance)
	car.back_wheel.follow(car.front_wheel, car.wheel_distance)
	back_wheel.moved.connect(car.front_wheel.move_as_follower)
	car.towed_mass_changed.connect(change_towed_mass)
	change_towed_mass(car.total_mass)

# Disconnect this car's signals from its followers
func remove_follower_car(car):
	back_wheel.moved.disconnect(car.front_wheel.move_as_follower)
	car.towed_mass_changed.disconnect(change_towed_mass)
	change_towed_mass(-car.total_mass)

# Share the knowledge of the new total mass
func change_towed_mass(mass_delta):
	towed_mass += mass_delta
	total_mass = mass + towed_mass
	towed_mass_changed.emit(mass_delta)

func _on_RailFollower_track_changed():
	add_to_track(front_wheel.get_parent(), front_wheel.offset)
