#by AlephSquirrel
from pygame import*
from random import*
init()
C=time.Clock()
D=display.set_mode((640,)*2)
F=font.SysFont(0,24)
R=randrange
U=display.update
display.set_caption('Sna1Ke')
while 1:
 x=y=d=3;s=0;l=[];f=R(32);g=R(32)
 while C.tick(15):
  for e in event.get():
   e.type==QUIT>exit()
   if e.type==KEYDOWN!=104<e.key<109:k=e.key%5;d=k^2*(k==d^2)
  x=x+d*d//2-d&31;y=y+~(7%~d)&31
  if(x-f|y-g)==0:s+=1;f=R(32);g=R(32)
  else:l=l[len(l)>2:]
  if(x,y)in l:break
  l+=(x,y),;D.fill((0,)*3)
  for i in range(32):draw.line(D,(60,)*3,(0,i*20),(640,i*20));draw.line(D,(60,)*3,(i*20,0),(i*20,640))
  [draw.rect(D,(0,180+15*i,0),Rect(X*20+i,Y*20+i,20-2*i,20-2*i))for X,Y in l for i in(0,4)];draw.circle(D,(255,0,0),(f*20+11,g*20+11),9);draw.line(D,(0,240,0),(f*20+10,g*20+3),(f*20+18,g*20+2),3);t=F.render(f"Score: {s}",1,(255,)*3);D.blit(t,t.get_rect());U()
 t=F.render(f"Game over! Score: {s}",1,(255,)*3);r=t.get_rect();r.center=D.get_rect().center;D.blit(t,r);U();C.tick(.4)