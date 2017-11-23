import winsound
from time import sleep

class beeps:
	# Duration of the note beep
	duration = 0 # in milliseconds
	
	# Scale #-1 Notes
	_B = 247

	# Scale #0 Notes
	C = 261
	D = 293
	E = 329
	F = 349
	G = 391
	A = 440
	B = 494
	
	# Scale #1 Notes
	C_ = 523
	D_ = 587
	E_ = 659
	F_ = 698
	G_ = 784
	A_ = 880
	B_ = 988
	
	# Scale #2 Notes
	C__ = 1047
	
	def __init__(self, d=None):
		if d is None:
			self.duration = 900
		else:
			self.duration = int(d)
	
	def hear(self, val, d=None):
		if d is None:
			if val=='' or val==' ':
				raise Exception('UnidentifiedMusicalNoteException: Unidentified note \'\' or \' \'')
			elif val=='C':
				winsound.Beep(self.C,self.duration)
			elif val=='D':
				winsound.Beep(self.D,self.duration)
			elif val=='E':
				winsound.Beep(self.E,self.duration)
			elif val=='F':
				winsound.Beep(self.F,self.duration)
			elif val=='G':
				winsound.Beep(self.G,self.duration)
			elif val=='A':
				winsound.Beep(self.A,self.duration)
			elif val=='B':
				winsound.Beep(self.B,self.duration)
			elif val=='C_':
				winsound.Beep(self.C_,self.duration)
			elif val=='D_':
				winsound.Beep(self.D_,self.duration)
			elif val=='E_':
				winsound.Beep(self.E_,self.duration)
			elif val=='F_':
				winsound.Beep(self.F_,self.duration)
			elif val=='G_':
				winsound.Beep(self.G_,self.duration)
			elif val=='A_':
				winsound.Beep(self.A_,self.duration)
			elif val=='B_':
				winsound.Beep(self.B_,self.duration)
			elif val=='C__':
				winsound.Beep(self.C__,self.duration)
			elif val=='_B':
				winsound.Beep(self._B,self.duration)
		else:
			if val=='' or val==' ':
				raise Exception('UnidentifiedMusicalNoteException: Unidentified note \'\' or \' \'')
			elif val=='C':
				winsound.Beep(self.C,d)
			elif val=='D':
				winsound.Beep(self.D,d)
			elif val=='E':
				winsound.Beep(self.E,d)
			elif val=='F':
				winsound.Beep(self.F,d)
			elif val=='G':
				winsound.Beep(self.G,d)
			elif val=='A':
				winsound.Beep(self.A,d)
			elif val=='B':
				winsound.Beep(self.B,d)
			elif val=='C_':
				winsound.Beep(self.C_,d)
			elif val=='D_':
				winsound.Beep(self.D_,d)
			elif val=='E_':
				winsound.Beep(self.E_,d)
			elif val=='F_':
				winsound.Beep(self.F_,d)
			elif val=='G_':
				winsound.Beep(self.G_,d)
			elif val=='A_':
				winsound.Beep(self.A_,d)
			elif val=='B_':
				winsound.Beep(self.B_,d)
			elif val=='C__':
				winsound.Beep(self.C__,d)
			elif val=='_B':
				winsound.Beep(self._B,d)