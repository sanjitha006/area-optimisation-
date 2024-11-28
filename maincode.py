#bounding block height maximum of max height of blocks and the average height when  2 blocks are kept one over the other
import time
startime=time.time()
input_file=open("input.txt","r")
output_file=open("output.txt","w")

gates={}

gwh=[]

totalarea=0
totalh=0
totalw=0
maxh=0

while(True):
    y=input_file.readline().split()

    if len(y)==0:
        break
    x=[y[0],int(y[1]),int(y[2])]
    gwh.append(x)
    maxh=max(maxh,int(y[2]))
    totalh+=int(y[2])
    totalw+=int(y[1])
    totalarea+=(int(y[1])*int(y[2]))
   

gwh=sorted(gwh, key=lambda x: x[1],reverse=True)


def compute(avght,gwh):
    gates2={}
    fg=[]

    visited=[0]*(len(gwh))
    i=0
    bbheight2=avght
    
    while(i<len(gwh)):
        if (visited[i]==1):
            i+=1
            continue

        x=list([gwh[i]])
   
        visited[i]=1
      
        for j in range(i+1,len(gwh)):
            if((gwh[j][2]+gwh[i][2])<=avght and visited[j]!=1):
    
                x=list([gwh[j]+["t"]])+x
            
                visited[j]=1
             
                present_th=x[1][2]+x[0][2]
                present_rh=x[1][2]
                l=1
                lb=0
                p=1
                for h in range(j+1,len(gwh)):
                    if(lb>=0 and ((x[l][1]-x[lb][1])>=gwh[h][1]) and ((gwh[h][2]+present_rh)<=avght) and p!=0 and visited[h]!=1):
                        present_rh+=x[l][2]
                        x.append(gwh[h]+["r"])
                
                        l-=1
                        lb-=1
                        visited[h]=1
                        p-=1
                    elif((gwh[h][2]+present_th)<=avght and visited[h]==0 ):
                        x=list([gwh[h]+["t"]])+x
                      
                        p+=1
                        l+=1
                        lb+=1
                        present_th+=gwh[h][2]
                        visited[h]=1
                break
            
        fg.append(x)

    k=0
    
    for i in fg:
        if(len(i)>=2):
            for d in range(len(i)):
                if(len(i[d])==3):
                    break
            gates2[i[d][0]]=(k,0)
            p=1
     
            while((d-p)>=0 or (d+p)<len(i) ):
                if  (d-p)>=0:
                    gates2[i[d-p][0]]=(k,gates2[i[d-p+1][0]][1]+i[d-p+1][2])
                if((d+p)<len(i)):
                    gates2[i[d+p][0]]=(gates2[i[d-p][0]][0]+i[d-p][1],gates2[i[d-p][0]][1])
                p+=1
            k+=i[d][1]
            
        elif(len(i)==2):
            gates2[i[1][0]]=(k,0)
            gates2[i[0][0]]=(k,i[1][2])
            k+=i[1][1]
        else:
            gates2[i[0][0]]=(k,0)
            k+=i[0][1]

    bbwidth2=k
    bbarea=bbwidth2*bbheight2

    
    res=[bbarea,bbwidth2,bbheight2,gates2]
    print(res)
    print()
    
    return(res)
    
bbarea_min=1000000000000000000000

for f in range(1,len(gwh)+1):
    avght=max((totalh*f)//len(gwh),maxh)
    print(gwh,maxh)
    v=compute(avght,gwh)

    
    if(v[0]<bbarea_min):
        bbarea_min=v[0]
        bbwidth=v[1]
        bbheight=v[2]
        gates=v[3]
    
packing_percent=(totalarea*100/(bbwidth*bbheight))
output_file.write("bounding_box"+" "+str(bbwidth)+" "+str(bbheight)+"\n")
    
for i in gates:
    output_file.write(i+" "+str(gates[i][0])+" "+str(gates[i][1])+"\n")
output_file.close()
    

print(packing_percent)
endtime=time.time()
print(endtime-startime,"seconds")







