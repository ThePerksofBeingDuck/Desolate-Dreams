extends Control

func _ready():
	# Connect signals for buttons
 # Hide all menus except the press any button label
	$Menus/AllMenus/Menu1.hide()
	$Menus/AllMenus/StartMenu.hide()
	$Menus/AllMenus/NewWorldMenu.hide()
	$Menus/AllMenus/OptionsMenu.hide()
	$Menus/AllMenus/LoadWorldMenu.hide()
	$Menus/AllMenus/pressany.show()
	# Set process input to true to detect input
	set_process_input(true)

func _input(event):
	if event is InputEventKey or event is InputEventMouseButton:
		_on_press_any_input()

func _on_press_any_input():
	$Menus/AllMenus/pressany.hide()
	$Menus/AllMenus/Menu1.show()
	set_process_input(false)

func _on_start_game_button_pressed():
	$Menus/AllMenus/Menu1.hide()
	$Menus/AllMenus/StartMenu.show()

func _on_quit_game_button_pressed():
	get_tree().quit()

func _on_create_new_world_button_pressed():
	$Menus/AllMenus/StartMenu.hide()
	$Menus/AllMenus/NewWorldMenu.show()
	var world_name = $Menus/AllMenus/NewWorldMenu/WorldNameInput.text.strip_edges()
	if world_name != "":
		var file_path = "user://" + world_name + ".ddworld"
		var file = FileAccess.open(file_path, FileAccess.WRITE)
		if file:
			var data = {
				"name": world_name,
				"created_at": Time.get_unix_time_from_system(),
				"data": {}
			}
			file.store_string(JSON.stringify(data))
			file.close()
			print("World created: " + file_path)
			_on_new_world_back_button_pressed()
		else:
			print("Failed to create world file!")
	else:
		print("World name cannot be empty!")
		
func _on_load_world_button_pressed():
	$Menus/AllMenus/StartMenu.hide()
	$Menus/AllMenus/LoadWorldMenu.show()
	$Menus/AllMenus/LoadWorldMenu.get_node("ItemList").populate_world_list()

func _on_options_button_pressed():
	$Menus/AllMenus/StartMenu.hide()
	$Menus/AllMenus/OptionsMenu.show()

func _on_start_menu_button_pressed():
	$Menus/AllMenus/StartMenu.hide()
	$Menus/AllMenus/Menu1.show()


func _on_new_world_back_button_pressed():
	$Menus/AllMenus/NewWorldMenu.hide()
	$Menus/AllMenus/StartMenu.show()

func _on_options_menu_back_button_pressed():
	$Menus/AllMenus/OptionsMenu.hide()
	$Menus/AllMenus/StartMenu.show()



func _on_start_button_dev_only_pressed():
	'''get_tree().change_scene_to_file("res://scenes/loading_screen.tscn")
	print("changing")'''
	get_tree().change_scene_to_file("res://scenes/loading_screen.tscn")
