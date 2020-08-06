str = "oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wh nfhdccmibh.r"
length = len(str)
res = ""

for i in range(0, length, 2):
    res += str[i+1]
    res += str[i]

print(res)
