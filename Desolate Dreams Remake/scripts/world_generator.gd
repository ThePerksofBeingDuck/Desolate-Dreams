extends Node2D

var width = 600
var height = 200
@onready var tilemap = $TileMap
var temperature = {}
var moisture = {}
var altitude = {}
var biome = {}
var openSimpleNoise = FastNoiseLite.new()

func generate_map(per, oct):
	openSimpleNoise.seed = randi()
	openSimpleNoise.period = per
	openSimpleNoise.fractal_octaves - oct
	var gridName = {}
	for x in width:
		for y in height:
			var rand =- 2*(abs(openSimpleNoise.get_noise_2d(x,y)))
			gridName[Vector2(x,y)] = rand
	return gridName
	
	
func _ready():
	temperature = generate_map(300, 5)
	moisture = generate_map(300, 5)
	altitude = generate_map(150, 5)
	
func determineTileIndex(temp, moist, alt) -> int:
	if alt < 0.2:
		return 0  # Tile index for deep water from the atlas
	elif alt < 0.4:
		return 1  # Tile index for shallow water from the atlas
	elif alt > 0.8:
		return 2  # Tile index for mountains from the atlas
	elif temp < 0.3 and moist > 0.7:
		return 3  # Tile index for swamp from the atlas
	elif temp < 0.4 and moist < 0.3:
		return 4  # Tile index for snow from the atlas
	elif temp < 0.5 and moist < 0.4:
		return 5  # Tile index for desert from the atlas
	else:
		return 6  # Default to grass tile index from the atlas

func set_tile(width, height):
	for x in width:
		for y in height:
			var pos = Vector2(x, y)
			var alt = altitude[pos]
			var temp = temperature[pos]
			var moist = moisture[pos]

			var tileIndex = determineTileIndex(temp, moist, alt)
			tilemap.set_cellv(pos, tileIndex)
