import time
import msvcrt
finish=10
count=0
print "Game Controls:\nD-> Move right\nS-> Move down\n\nPress ENTER to get started"
raw_input()
s_time=time.time()
print "Press Right, Down, Right 10 consecutive times, and you win the game."
while 1:
	k=msvcrt.getch()
	if k=='d':
		count=count+1
		print "-->",
		if count==finish:
			count=0
			break
	else:
		print "\nYou pressed a wrong key, dumbo. You lost the game. Press ENTER to quit. :P"
		raw_input()
		exit()
print "Time to go 10 spaces down and then turn right again."
while 1:
	k=msvcrt.getch()
	if k=='s':
		count=count+1
		print "       				      |"
		if count==finish:
			count=0
			break
	else:
		print "\nYou pressed a wrong key, dumbo. You lost the game. Press ENTER to quit. :P"
		raw_input()
		exit()
print "Right turn, please.            	     ",
while 1:
	k=msvcrt.getch()
	if k=='d':
		count=count+1
		print "-->",
		if count==finish:
			count=0
			break
	else:
		print "\nYou pressed a wrong key, dumbo. You lost the game. Press ENTER to quit. :P"
		raw_input()
		exit()
time_elapsed=time.time()-s_time;
print "\n\nCongratulations, dummy! You've taken %f seconds to complete the game. :D"%(time_elapsed)
raw_input()