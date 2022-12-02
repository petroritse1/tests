#A random password generator
import random
aplha = "A",'B','C','D','E',"F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
sma = 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
num = '1','2','3','4','5','6','7','8','9','0'
ch = "!","@","#","$","%",'^',"&",'*','(',')','_','+',';','|','/','~'

# chi = input("How long do you want your password to be in characters but it must be higher than 5:/n  ")
d = []
for x in range(1,5):
    ran_chi = random.choice(aplha)
    ran_chi1 = random.choice(sma)
    ran_chi2 = random.choice(num)
    ran_chi3 = random.choice(ch)
    d.append(ran_chi)
    d.append(ran_chi1)
    d.append(ran_chi2)
    d.append(ran_chi3)
  
  
    
d = str(d)
d = d.replace(",","")
d = d.join
print(d)