extends TileMap

var moisture = FastNoiseLite.new()
var temperature = FastNoiseLite.new()
var altitude = FastNoiseLite.new()
var width = 128
var height = 128
@onready var player = get_parent().get_child(1)

func _ready():
	moisture.seed = randi()
	temperature.seed = randi()
	altitude.seed = randi()
	altitude.frequency = 0.005

func _process(delta):
	generate_chunk(player.position)
	var tile_pos = local_to_map(position)
	

func generate_chunk(position):
	var tile_pos = local_to_map(position)
	for x in range(width):
		for y in range(height):
			var moist = moisture.get_noise_2d(tile_pos.x-width/2 + x, tile_pos.y-height/2 + y)*10
			var temp = temperature.get_noise_2d(tile_pos.x-width/2 + x, tile_pos.y-height/2 + y)*10
			var alt = altitude.get_noise_2d(tile_pos.x-width/2 + x, tile_pos.y-height/2 + y)*10
			
			if alt < 2:
				set_cell(0, Vector2i(tile_pos.x-width/2 + x, tile_pos.y-height/2 + y), 0, Vector2(3, round((temp+10)/5)))
			else:
				set_cell(0, Vector2i(tile_pos.x-width/2 + x, tile_pos.y-height/2 + y), 0, Vector2(round((moist+10)/5), round((temp+10)/5)))

func setPlayerPositionOnDryTile(playerPosition):
	var tile_pos = local_to_map(playerPosition)
	var foundDryTile = false
	var maxIterations = 100  # Maximum number of iterations to prevent infinite loop
	while !foundDryTile and maxIterations > 0:
		var x = randi() % width
		var y = randi() % height
		var alt = altitude.get_noise_2d(tile_pos.x-width/2 + x, tile_pos.y-height/2 + y)*10
		if alt >= 2:  # Check if the tile is not water
			var world_position = map_to_local(Vector2(x, y))
			player.position = world_position
			foundDryTile = true
		maxIterations -= 1
