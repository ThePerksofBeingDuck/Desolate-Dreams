extends VBoxContainer

@onready var load_world_back_button = $LoadWorldBackButton
@onready var item_list = $ItemList


func _on_back_button_pressed():
	hide()
	get_parent().get_parent().get_node("StartMenu").show()

func _on_item_activated(index):
	var world_name = item_list.get_item_text(index)
	load_world(world_name)

func load_world(world_name: String):
	var file_path = "user://" + world_name + ".ddworld"
	var file = FileAccess.open(file_path, FileAccess.READ)
	if file:
		var content = file.get_as_text()
		var world_data = JSON.stringify(content)
		file.close()
		if world_data:
			print("Loaded world: " + world_name)
			# Here you can add code to initialize your game with the loaded world data
		else:
			print("Failed to load world: " + world_name)
	else:
		print("World file does not exist!")

func populate_world_list():
	item_list.clear()
	var dir = DirAccess.open("user://")
	if dir:
		dir.list_dir_begin()
		var file_name = dir.get_next()
		while file_name != "":
			if file_name.ends_with(".ddworld"):
				item_list.add_item(file_name.replace(".ddworld", ""))
			file_name = dir.get_next()
		dir.list_dir_end()
	else:
		print("Failed to open user directory!")
