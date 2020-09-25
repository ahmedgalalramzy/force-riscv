
p1 = '<physical_register index="0xb'

p2 = '" name="mhpmcounter'

p3 = 'h" size="32" type="SysReg"/>'

for i in range(3, 32):
    x = p1 + str(hex(131 + i - 3))[2:] + p2 + str(i) + p3
    print(x)
    