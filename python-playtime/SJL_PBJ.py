bread = 6
peanutbutter = 3
jelly = 2

if bread == peanutbutter + jelly:
	print "Peanut butter jelly time! You can make {0} sandwich(es).".format(bread/2)
elif bread % 2:
	print "So close! You can make {0} and a half sandwich(es).".format(bread/2)
elif peanutbutter == 0:
	print "Peanut butter is missing from your life, but you can settle for just jelly."
elif jelly == 0:
	print "Jelly is missing from your life, but you can settle for just peanut butter."
elif peanutbutter > jelly:
	print "You can make {0} PB&J sandwich(es)".format(jelly)
	print "and {0} just peanut butter sandwiches.".format(peanutbutter-jelly)
elif peanutbutter < jelly:
	print "You can make {0} PB&J sandwich(es)".format(peanutbutter)
	print "and {0} just jelly sandwiches.".format(jelly-peanutbutter)
elif bread == 0:
	print "You need bread to make a sandwich. You have no bread. Be smarter. Buy bread."
else:
	print "Sorry, it's not peanut butter jelly time for you."

