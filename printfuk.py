import sys
import random
import subprocess
import time
from sys import platform
global chars
chars = [chr(x) for x in range(32,592)]+[chr(x) for x in range(647,670)]+[chr(x) for x in range(688,767)]+[chr(x) for x in range(880,1024)]+[chr(x) for x in range(7936,8191)]
def getRandomChar():
	global chars
	x= random.randint(0,int(len(chars)*1.02))
	if x>=len(chars) or x=='\r' or x=='\n':
		return ""
	c= chars[x]
	return c
def __break(S,color=88,cmod=0.5,useColor=True,startAfter=0,onlyAfter=False):
	i=random.randint(0,100)
	n = 0;
	N=(int)(len(S)*cmod)
	while i>=5 and n<=N:
		
		if len(S)>startAfter and onlyAfter:
			i = random.randint(startAfter,len(S)-1)
		else:
			i = random.randint(0,len(S)-1)
		if len(S)<startAfter:
			c = S[i]
		else:
			c = getRandomChar()
			
		S=S[:i]+c+S[i+1:]
		n+=1
		i=random.randint(0,100)
	if useColor:
		strEffect = u"\u001b[38;5;"+color+"m\033[5m"
		reset = "\u001b[0m"
		return strEffect+S+reset
	return S
def __isWindows():
	return platform.lower().startswith("win")
def __printHelper(S):
	subprocess.run(["echo", "-ne",S])
def print(*args,**kwargs):
	_string = args[0]
	sep = " "
	if "sep" in kwargs:
		sep = str(kwargs['sep'])
	if len(args)>1:
		for s in args[1:]:
			_string+=sep+s
	delay=.1
	end="\n"
	color=88
	startAfter=0
	maxCharMod=.5
	useAnsi=True
	onlyAfter=False

	if "delay" in kwargs:
		delay = kwargs['delay']
	if "color" in kwargs:
		color = kwargs['color']
	color=str(color)
	if "startAfter" in kwargs:
		startAfter = kwargs['startAfter']
	if startAfter>=len(_string):
		startAfter=0
	if "maxCharMod" in kwargs:
		maxCharMod = kwargs['maxCharMod']
	if "end" in kwargs:
		end = kwargs['end']
	if "useAnsi" in kwargs:
		useAnsi = kwargs['useAnsi']
	elif __isWindows():
			useAnsi=False
	if "onlyAfter" in kwargs:
		onlyAfter = kwargs['onlyAfter']
	if delay<0:
		delay=0.1	
	if maxCharMod>1:
		maxCharMod=1
	if maxCharMod<=0:
		maxCharMod=0.5
	if maxCharMod<0.05:
		maxCharMod=0.05

	if len(end)>1:
		end=__break(end,color,maxCharMod)

	
	S = ""
	i=0
	st=""
	if delay>0:
		j=0
		for x in _string:
			j+=1
			S+=x
			st=__break(S,color,maxCharMod,useAnsi,startAfter, onlyAfter)
			if j>=len(_string):
				subprocess.run(["echo", "-ne",st])
			else:
				subprocess.run(["echo", "-ne",st+'\r'])
				#sys.stdout.write(st+'\r')
			#sys.stdout.flush()
		
			time.sleep(delay)
			
		subprocess.run(["echo", "-ne",end])
		#sys.stdout.write(end)
	else:
		st=__break(_string,color,maxCharMod)
		subprocess.run(["echo", "-ne",st])
		subprocess.run(["echo", "-ne",end])
if __name__ == "__main__":
	ver = "0.0.2"
	m1="printfuk version "+ver+" written by"
	print(m1," ",color=32,sep=":",startAfter=len(m1),delay=.2,onlyAfter=True,end="\b")
	print("Holden Milne 2021"," "*len(m1),color=166,startAfter=0,delay=.08,end=" ")

