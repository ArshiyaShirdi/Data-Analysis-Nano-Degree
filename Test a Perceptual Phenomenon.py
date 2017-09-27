import datetime
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

fil = pd.read_csv("stroopdata.csv")
#print(fil)

fil1 = pd.DataFrame(fil)
cong = fil1['Congruent']
incong = fil1['Incongruent']

#print(cong,incong)

congo_b = incong - cong 
print(congo_b)

########Calculating mean#######
cong_m = np.mean(cong)
incong_m = np.mean(incong)
print(cong_m,incong_m)



########Calculating median ########
c = (len(cong))/2
cs = np.sort(cong)
median = cs[12]

c1 = (len(incong))/2
cs1 = np.sort(incong)
median1 = cs1[12]

print(median,median1)

##### Calculating range####

cmx = max(cong)
cmn = min(cong)
cmr = cmx - cmn
print(cmr)

cmxi = max(incong)
cmni = min(incong)
cmri = cmxi - cmni
print(cmri)

#########plotting congruent,incongruent,difference between congruent and incongruent####
plt.plot(cong,label='linear')
plt.plot(incong,label='linear')
#plt.plot(congo_b,label='linear')
         

plt.show()


########

x = ttest_ind(cong, incong)
print(x)

