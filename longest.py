
from collections import defaultdict

##def dec( msg, seqs):
##    mess = msg
##    g =[]
##    for i in range(len(mess)):
##        print ord(mess[i])
##        print seqs[i%len(seqs)]
##        #g.append(chr(((ord(mess[i])+26)%26) - seqs[i%len(seqs)]))
##        if mess[]
##    print g

def DecrementCharacter(character, amount):
    upper = character.isupper()

    a = ord('a')
    value = ord(character.lower()) - int(amount)
    if (value < a):
        value = value + 26

    if (upper):
        return chr(value).upper()
            
    return chr(value)
def DecryptMessage(message, key):
    messageEnd = len(message) - 1
    keyEnd = len(key) - 1

    mi = messageEnd
    ki = keyEnd

    adj = ''
    while (mi > - 1):
        if (message[mi].isalpha()):
            adj = DecrementCharacter(message[mi], key[ki]) + adj
            ki = ki - 1
            if (ki < 0):
                ki = keyEnd
        else:
            adj = message[mi] + adj

        mi = mi - 1

    return adj    

    
    

def pattern(seq):
    n = len(seq)
    sequences = []
    length = []
    c = defaultdict(int) # Counts of each subsequence
    for i in xrange(n):
        for j in xrange(i + 1, min(n, n / 2 + i)+1): 
            c[tuple(seq[i:j])] += 1
            sequences.append(seq[i:j])
            length.append(len(seq[i:j]))
            
    maxim = max(length)
    
    for i in sequences:
        if len(i) == maxim:
            seqs =  i
            #break
            print seqs
   # dec("atvthrqgsecnikg",seqs)
    print DecryptMessage("atvthrqgsecnikg",seqs)
    
    
a="Otjfvknou kskgnl, K mbxg iurtsvcnb ksgq hoz atv. Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez. -Atvt hrqgse, Cnikg"
b=a[-19:]
b=b.lower()
key =[]
temp="-Your friend, Alice"
temp=temp.lower()
for i in range(len(b)):
	if (ord(b[i])>=97 and ord(b[i]) <=122 ):
		key.append((ord(b[i])-ord(temp[i]))%26)
p=pattern(key)
print(p)
