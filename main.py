import turtle
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
 
screen = turtle.Screen()
screen.setup(width=600,height=600,)
screen.bgcolor("Black")
screen.tracer(0)
 
player = Player()
car_manager = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(player.go_up,"Up")
# screen.onkey(player.go_down,"Down")
# screen.onkey(player.go_right,"Right")
# screen.onkey(player.go_left,"Left")

game_is_on = True

while game_is_on:
	time.sleep(0.1)
	screen.update()
	
	car_manager.create_car()
	car_manager.move_cars()
	
	#collision with cars
	for cars in car_manager.all_cars:
		if cars.distance(player) < 26:
			score.game_over()
			game_is_on = False
	
	#successful crossing
	if player.is_at_finish_line():
		player.go_to_start()
		car_manager.level_up()
		score.increase_level()
screen.exitonclick()