from beeply import notes

# To create an object of the class, pass the duration of the beep sound as parameter
# Default is 900
s = notes.beeps()
s.hear('C',500)
s.hear('D',500)
s.hear('E',3500)
s.hear('D',500)
s.hear('E',500)
s.hear('F',500)
sleep(2)
s.hear('E',1400)
s.hear('D',1400)
s.hear('_B',500)
s.hear('D',600)
s.hear('C')
sleep(2)