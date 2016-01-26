from animal import * 
import random
food=[" beef"," eggs"," sausage"]
name=[" jiries"," baseel"," mousa"," yousef"]
name2=["shai","noga","ilin"]
for x in range (50):
	dog = Animal("woof", name[random.randint(0,2)],12)
	dog.eat(food[random.randint(0,2)])
for i in range (30):
	cat = Animal("meowjegjasd",name[random.randint(0,2)],"9")
	cat.eat(food[random.randint(0,2)])


 
