@tool
class_name NoiseGeneratorSettings
extends GeneratorSettings2D

## Array of [NoiseGeneratorData]´s that contain the thresholds, titles and tiles.
## If a new element is empty, it fills it with a new [NoiseGeneratorData].
@export var tiles: Array[NoiseGeneratorData]:
## Removed the sorting since now we have max and min thresholds
	set(value):
		## If the last element of the array is not a [param NoiseGeneratorData],
		## then create a new one.
		if value.size() > 0:
			value[-1] = value[-1] if value[-1] is NoiseGeneratorData else NoiseGeneratorData.new()

		tiles = value
		for tile_data in tiles:
			tile_data.settings = self
@export var noise: FastNoiseLite = FastNoiseLite.new()
## Infinite worlds only work with a [ChunkLoader].
@export var infinite: bool = false
@export var world_size: Vector2i = Vector2i(256, 256):
	set(value):
		world_size = value
		if is_instance_valid(falloff_map):
			falloff_map.size = world_size
@export_group("Falloff", "falloff_")
## Enables the usage of a [FalloffMap], which makes tiles
## farther away from the center be lower in the heightmap,
## forming islands. Doesn't work if [param infinite] is [code]true[/code].
@export var falloff_enabled: bool = false
## Enables the usage of a [FalloffMap], which makes tiles
## farther away from the center be lower in the heightmap,
## forming islands. Doesn't work if [param infinite] is [code]true[/code].
@export var falloff_map: FalloffMap:
	set(value):
		falloff_map = value
		if falloff_map != null:
			falloff_map.size = world_size
