metros=float(input('Metros: '))
#print(f'{metros} metros sao {metros*100} centimetros e {metros*1000} milimetros')
km= metros/1000
hm= metros/100
dam= metros/10
dm= metros*10
cm= metros*100
mm= metros*1000

print(f'{metros} Metros sao: \n{km} Km\n{hm} hm\n{dam} dam\n{dm:.0f} dm\n{cm:.0f} cm\n{mm:.0f} mm')
