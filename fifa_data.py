import numpy as np
import pandas as pd

data=pd.read_csv('C:/Users/user/Downloads/data.csv',index_col=0)
data.rename({'Release Clause': 'Release_Clause', 
             'Preferred Foot': 'Preferred_Foot',
             'International Reputation':'International_Reputation',
             'Weak Foot':'Weak_Foot',
             'Skill Moves':'Skill_Moves',
             'Work Rate':'Work_Rate',
             'Body Type':'Body_Type',
             'Real Face':'Real_Face',
             'Jersey Number':'Jersey_Number',
             'Loaned From':'Loaned_From',
             'Contract Valid Until':'Contract_Valid_Until'}, axis=1, inplace=True)

#--------- To change the format of Value, Wage, Release_Clause values --------
xa=data.Value.values.tolist()
for i in range(len(xa)):
    xb=xa[i].split('€')
    xc=xb[1].split('M')
    try:
        #xa[i]=float(xc[0])*(10**6)
        xa[i]=float(xc[0])
    except ValueError:
        xd=xc[0].split('K')
        xa[i]=float(xd[0])*(10**(-3))
        
data['Value']=xa

#-----------------------------------
count=0
float_prob=[]
float_val=[]
ya=data.Release_Clause.values.tolist()
for i in range(len(ya)):
    try:
        yb=ya[i].split('€')
    except AttributeError:
        #float_prob.append(i)
        #float_val.append(ya[i])
        #count+=1
        ya[i]=0
    else: 
        yc=yb[1].split('M')
        try:
            #ya[i]=float(yc[0])*(10**6)
            ya[i]=float(yc[0])
        except ValueError:
            yd=yc[0].split('K')
            ya[i]=float(yd[0])*(10**(-3))
        
    
data['Release_Clause']=ya

#----------------------------------

za=data.Wage.values.tolist()
for i in range(len(za)):
    zb=za[i].split('€')
    zc=zb[1].split('K')
    za[i]=float(zc[0])
    '''
    try:
        #xa[i]=float(xc[0])*(10**6)
        za[i]=float(zc[0])
    except ValueError:
        zd=zc[0].split('K')
        za[i]=float(zd[0])*(10**(-3))
        '''
        
data['Wage']=za
 

#----------------Changing Weight and Height data format---------------
height=data.Height.values.tolist()
for i in range(len(height)):
    try:
        foot=height[i].split("'")
    except AttributeError:
        height[i]=0
    else:
        hcm=float(foot[0])*30.48 + float(foot[1])*2.54
        height[i]= hcm*0.01
    
data['Height']=height   
#------------------------------
weight=data.Weight.values.tolist()
for i in range(len(weight)):
    try:
        lbs=weight[i].split("lbs")
    except AttributeError:
        weight[i]=0
    else:
        weight[i]= float(lbs[0])*0.45
    
data['Weight']=weight 
   
# Calculate BMI of players        
data['BMI']=((data['Weight'])/(data['Height']**2)).values

data['Overall_by_Wage']=(data['Overall']/data['Wage']).values

#Export the formatted data frame to a new .csv file
data.to_csv(r'C:/Users/user/Downloads/data1.csv',header=True, index=None)

