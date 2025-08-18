#by AlephSquirrel
from pygame import*
from random import*
init()
C=time.Clock().tick
D=display.set_mode((640,)*2)
F=font.SysFont(0,24).render
L=draw.line
R=randrange
U=display.update
display.set_caption('Sna1Ke')
while 1:
 x=y=d=3;s=0;l=[];b=[];f=R(32);g=R(32)
 while C(15):
  for e in event.get():
   T=e.type;T==QUIT>exit()
   if T==KEYDOWN!=104<e.key<109:b+=e.key%5,
  if b:k,*b=b;d=k^2*(k==d^2)
  x=x+d*d//2-d&31;y=y+~(7%~d)&31
  if x-f|y-g:l=l[len(l)>2:]
  else:
   s+=1;f=R(32);g=R(32)
   while(f,g)in l:f=R(32);g=R(32)
  if(x,y)in l:break
  l+=(x,y),;D.fill((0,)*3)
  for i in range(32):L(D,(60,)*3,(0,i*20),(640,i*20));L(D,(60,)*3,(i*20,0),(i*20,640))
  [draw.rect(D,(0,180+15*i,0),Rect(X*20+i,Y*20+i,20-2*i,20-2*i))for X,Y in l for i in(0,4)];draw.circle(D,(255,0,0),(f*20+11,g*20+11),9);L(D,(0,240,0),(f*20+10,g*20+3),(f*20+18,g*20+2),3);t=F(f"Score: {s}",1,(255,)*3);D.blit(t,t.get_rect());U()
 t=F(f"Game over! Score: {s}",1,(255,)*3);r=t.get_rect();r.center=320,320;D.blit(t,r);U();C(.4)