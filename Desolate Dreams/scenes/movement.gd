extends  CharacterBody2D

const ACCELERATION = 800
const FRICTION = 500
const MAX_SPEED = 120

enum {IDLE, RUN}
var state = IDLE

@onready var animationTree = 
