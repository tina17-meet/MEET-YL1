from meet import *
cells=[]
for x in range (0,99):
	cell={"x":get_random_x(),"y":get_random_y(),"radius":5,"dy":0.1,"dx":0.1}
	z=create_cell(cell)
	cells.append(z)
for cell in cells:
	get_screen_width()
	get_screen_height()
	cell.xcor()
	cell.ycor()
	if(cell.xcor()>get_screen_width():
		dy=dy*1
	move_cells(cells)



