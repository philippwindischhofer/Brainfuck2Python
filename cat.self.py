from MemoryTape import MemoryTape
import putget as pg
ptr=0
mem=MemoryTape()
ptr+=1
ptr+=1
ptr+=1
ptr+=1
ptr+=1
ptr+=1
while mem[ptr]:
	mem[ptr]-=1

mem[ptr]+=1
mem[ptr]+=1
mem[ptr]+=1
mem[ptr]+=1
ptr-=1
mem[ptr]=ord(pg.getch())
ptr-=1
ptr-=1
ptr-=1
while mem[ptr]:
	mem[ptr]-=1

ptr+=1
ptr+=1
ptr+=1
ptr+=1
ptr+=1
ptr+=1
ptr+=1
ptr+=1
ptr+=1
ptr+=1
ptr+=1
while mem[ptr]:
	mem[ptr]-=1

ptr-=1
ptr-=1
ptr-=1
ptr-=1
ptr-=1
ptr-=1
ptr-=1
ptr-=1
while mem[ptr]:
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	mem[ptr]+=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	mem[ptr]+=1
	ptr+=1
	ptr+=1
	ptr+=1
	mem[ptr]-=1

ptr-=1
ptr-=1
ptr-=1
while mem[ptr]:
	ptr+=1
	ptr+=1
	ptr+=1
	mem[ptr]+=1
	ptr-=1
	ptr-=1
	ptr-=1
	mem[ptr]-=1

while mem[ptr]:
	mem[ptr]-=1

ptr+=1
ptr+=1
ptr+=1
ptr+=1
while mem[ptr]:
	ptr-=1
	mem[ptr]-=1
	ptr-=1
	ptr-=1
	ptr-=1
	mem[ptr]+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	mem[ptr]-=1

ptr-=1
ptr-=1
ptr-=1
ptr-=1
while mem[ptr]:
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	mem[ptr]+=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	mem[ptr]-=1

ptr+=1
ptr+=1
ptr+=1
while mem[ptr]:
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	pg.putch(chr(mem[ptr]))
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	mem[ptr]=ord(pg.getch())
	ptr-=1
	ptr-=1
	ptr-=1
	while mem[ptr]:
		mem[ptr]-=1

	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	while mem[ptr]:
		mem[ptr]-=1

	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	while mem[ptr]:
		ptr+=1
		ptr+=1
		ptr+=1
		ptr+=1
		ptr+=1
		ptr+=1
		ptr+=1
		ptr+=1
		mem[ptr]+=1
		ptr-=1
		ptr-=1
		ptr-=1
		ptr-=1
		ptr-=1
		ptr-=1
		ptr-=1
		ptr-=1
		ptr-=1
		ptr-=1
		ptr-=1
		mem[ptr]+=1
		ptr+=1
		ptr+=1
		ptr+=1
		mem[ptr]-=1

	ptr-=1
	ptr-=1
	ptr-=1
	while mem[ptr]:
		ptr+=1
		ptr+=1
		ptr+=1
		mem[ptr]+=1
		ptr-=1
		ptr-=1
		ptr-=1
		mem[ptr]-=1

	while mem[ptr]:
		mem[ptr]-=1

	ptr+=1
	ptr+=1
	ptr+=1
	ptr+=1
	while mem[ptr]:
		ptr-=1
		mem[ptr]-=1
		ptr-=1
		ptr-=1
		ptr-=1
		mem[ptr]+=1
		ptr+=1
		ptr+=1
		ptr+=1
		ptr+=1
		mem[ptr]-=1

	ptr-=1
	ptr-=1
	ptr-=1
	ptr-=1
	while mem[ptr]:
		ptr+=1
		ptr+=1
		ptr+=1
		ptr+=1
		mem[ptr]+=1
		ptr-=1
		ptr-=1
		ptr-=1
		ptr-=1
		mem[ptr]-=1

	ptr+=1
	ptr+=1
	ptr+=1

