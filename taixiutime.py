from random import randint

def comp():
    c1=randint(1,6)
    c2=randint(1,6)
    c3=randint(1,6)
    computer=c1+c2+c3
    if computer<=10:
        computer='Xiu'
    else:
        computer='Tai'
    return computer

def nguoichoi():
    so_luong=int(input('Nhap so luong nguoi dat cuoc: '))
    ten=list()
    tien=list()
    tx=list()
    for i in range(so_luong):
        t=input('Nhap ten nguoi choi '+str(i+1)+':')
        ten.append(t)
        ti=input('Nhap tien dat cuoc cua nguoi choi'+str(i+1)+':')
        tien.append(ti)
        p=input('Nhap ben ban dat(Tai/Xiu):')
        tx.append(p)
    return ten,tien,tx

ketqua=comp()
tmp=nguoichoi()
name=tmp[0]
money=tmp[1]
bet=tmp[2]
win=0
print('Ket qua:',ketqua)
for i in range(len(bet)):
    if bet[i]==ketqua:
        bet[i]=1
        win+=1
    else:
        bet[i]=0
tong=0
for i in range(len(money)):
    tong+=int(money[i])
tien_thuong=tong//win
for i in range(len(bet)):
    if bet[i]==1:
        bet[i]=tien_thuong
for i in range(len(name)):
    print('Ten: '+name[i])
    print('Tong tien con lai:',bet[i])

