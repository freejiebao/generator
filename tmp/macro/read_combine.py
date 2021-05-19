import argparse
import numpy as np

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('-i','--input', help='input file', default='combine.log')
parser.add_argument('-t','--transfer', help='transfer the signal strength',action='store_true', default= False)

args = parser.parse_args()

def transfer(signal_strength,sample_type='',round_length=2):
    if args.transfer:
        if sample_type=='sswwjj_dim5':
            return np.round(246*246*np.sqrt(signal_strength)/200000.,round_length)
        else:
            return np.round(np.sqrt(signal_strength),round_length)
    else:
        return np.round(signal_strength,round_length)

combine={}
quantiles=[0,0,0,0,0]
nquantile=-1
with open(args.input,'r') as infile:
    for line in infile:
        stripped_line = line.strip()
        if 'The hmn mass:' in stripped_line:
            # print(stripped_line)
            combine[stripped_line.split()[3][:-1]]=quantiles
        if nquantile==0:
            nquantile+=1
        if '-- AsymptoticLimits ( CLs ) --' in stripped_line:
            quantiles=[0,0,0,0,0]
            nquantile+=1
        if nquantile>0 and nquantile<=5:
            quantiles[nquantile-1]=float(stripped_line.split("r < ")[1])
            nquantile+=1
        if nquantile>5:
            nquantile=-1
            # print(quantiles)
print(combine)
sort=['hmn_m50','hmn_m150','hmn_m300','hmn_m450','hmn_m600','hmn_m750','hmn_m900','hmn_m1000','hmn_m1250','hmn_m1500','hmn_m1750','hmn_m2000','hmn_m2500','hmn_m5000','hmn_m7500','hmn_m10000','hmn_m15000','hmn_m20000','sswwjj_dim5']
tmp_combine={}
for i in sort:
    tmp_combine[i]=combine[i]
combine=tmp_combine
# latex style
for i in combine:
    quantile0=transfer(combine[i][0],i,3)
    quantile1=transfer(combine[i][1],i,3)
    quantile2=transfer(combine[i][2],i,3)
    quantile3=transfer(combine[i][3],i,3)
    quantile4=transfer(combine[i][4],i,3)
    line="{0} & {1} & [{2},{3}] & [{4},{5}] \\\\".format(i,quantile2,quantile1,quantile3,quantile0,quantile4)
    print(line)
# xlsx style
for i in range(0,5):
    line=''
    for j in combine:
        val=transfer(combine[j][i],i,4)
        line+=str(val)
        line+='\t'
    print(line)
