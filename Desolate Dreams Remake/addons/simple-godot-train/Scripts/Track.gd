@tool
# A piece of track that TrainWheel nodes follow along
class_name Track
extends Path2D

signal wheel_at_head
signal wheel_at_tail

@export var crosstie_distance = 10
@onready var _crosstie_mesh_instance = $Crosstie
@onready var _crosstie_multimesh = $MultiMeshInstance2D

func _ready():
	_update_sprites()

# Connect the "from_side" of this track to the "to_side" of the other track
#
# This links both tracks to each other, so only call it once per connection
func link_track(other_track, from_side, to_side):
	connect("wheel_at_" + from_side, Callable(other_track, "enter_from_" + to_side))
	other_track.connect("wheel_at_" + to_side, Callable(self, "enter_from_" + from_side))

# A wheel enters from the head side
func enter_from_head(wheel: PathFollow2D, extra, is_forward):
	wheel.set_track(self)
	wheel.progress = extra
	wheel.head_to_tail() if is_forward else wheel.tail_to_head()

# A wheel enters from the tail side
func enter_from_tail(wheel: PathFollow2D, extra, is_forward):
	wheel.set_track(self)
	wheel.progress_ratio = 1
	wheel.progress -= extra
	wheel.tail_to_head() if is_forward else wheel.head_to_tail()

# The wheel has reached the head
func on_wheel_at_head(wheel, extra, is_forward):
	wheel_at_head.emit(wheel, extra, is_forward)

# The wheel has reached the tail
func on_wheel_at_tail(wheel, extra, is_forward):
	wheel_at_tail.emit(wheel, extra, is_forward)

func _update_sprites():
	$Line2D.points = curve.get_baked_points()
	_update_crossties()
	$HeadPoint.progress_ratio = 0
	$TailPoint.progress_ratio = 1

func _update_crossties():
	var crossties = _crosstie_multimesh.multimesh
	crossties.mesh = _crosstie_mesh_instance.mesh
	
	var curve_length = curve.get_baked_length()
	var crosstie_count = round(curve_length / crosstie_distance)
	crossties.instance_count = crosstie_count
	
	for i in range(crosstie_count):
		var t = Transform2D()
		var crosstie_position = curve.sample_baked((i * crosstie_distance) + crosstie_distance/2)
		var next_position = curve.sample_baked((i + 1) * crosstie_distance)
		t = t.rotated((next_position - crosstie_position).normalized().angle())
		t.origin = crosstie_position
		crossties.set_instance_transform_2d(i, t)
