extends Resource

# Define the properties and data structure for your world data
class_name WorldData

# Add properties to store information about the world
var world_name : String
var player_position : Vector2
var world_state : int

# Add methods to set and get world data
func set_world_name(name: String) -> void:
	world_name = name

func get_world_name() -> String:
	return world_name

func set_player_position(position: Vector2) -> void:
	player_position = position

func get_player_position() -> Vector2:
	return player_position

func set_world_state(state: int) -> void:
	world_state = state

func get_world_state() -> int:
	return world_state
