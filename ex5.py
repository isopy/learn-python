name = 'Zed A. Shaw'
age = 35 # not a lie
height_inches = 74 # inches
height_cm = height_inches * 2.54
weight_lbs = 180 # lbs
weight_kilos = weight_lbs * 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." %name
print "He's %d inches tall." %height_inches
print "He's %d centimeters tall" %height_cm
print "He's %d pounds heavy." %weight_lbs
print "He's %d kilograms heavy." %weight_kilos
print "No matter how you look it it, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %r." % (
    age, height_inches, weight_lbs, age + height_inches + weight_lbs)
print "If I add %d, %d, and %d I get %r." % (
    age, height_cm, weight_kilos, age + height_cm + weight_kilos)

