C, P, R = map(int, input().split())
C_i, P_i, R_i = 2.5*C, 2.0*P, 0.5*R
All_i = C_i+ P_i + R_i
if (All_i*2)//10 ==0:
    amperes = All_i*2
else:
    amperes = ((All_i*2)//10)*10 +10
print('{} amperes'.format(int(amperes)))