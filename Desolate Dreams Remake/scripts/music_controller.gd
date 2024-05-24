extends Node

# Declare member variables
var music_player: AudioStreamPlayer
var music_list: Array = ["res://sfx/Melody.wav", "res://sfx/main_theme.mp3"]
var music_delay: float = 30.0

func _ready():
	music_player = $AudioStreamPlayer
	start_music()

func start_music():
	# Shuffle the music list for random playback
	music_list.shuffle()
	play_music(0)

func play_music(index: int):
	if index < music_list.size():
		music_player.stream = load(music_list[index])
		music_player.play()
		await wait_for_music_to_end()
		# Wait for some time before playing the next song
		await wait_for_delay()
		play_music(index + 1)
	else:
		# Restart the music list once all tracks have been played
		start_music()

func wait_for_music_to_end():
	# Yield until the music has finished playing
	await music_player.finished

func wait_for_delay():
	# Yield for a delay before playing the next song
	await get_tree().create_timer(music_delay).timeout
