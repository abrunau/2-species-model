"""
Created on Wed Jun  8 09:40:55 2022
Updated for github

@author: abrunaud
"""

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd






plt.hist(ha_final_sp1[1],color="r",edgecolor='0',alpha=0.3,label="patrolling window position sp 1")
plt.hist(ha_final_sp2[1],color="b",edgecolor="0",alpha=0.3,label="patrolling window position sp 2")
#plt.axvline(x=np.mean(ha_final_sp1[0]),linewidth=2,color="#BE3F3F",label="mean patrolling window position sp1")
#plt.axvline(x=np.mean(ha_final_sp2[0]),linewidth=2,color="#3F54BE",label="mean patrolling window position sp2")
plt.xlim(0,1)
plt.ylim(0,70)
#plt.axvline(e1,c="red",label = "peak emergence sp 1")
#plt.axvline(e2,c="blue", label = "peak emergence sp 2")
plt.ylabel("Number of males")
plt.xlabel("Daily time")
xe = np.linspace(0,1,1000)
ye1 = (1 / (np.sqrt(2 * np.pi * np.power(ve1,2)))) * (np.power(np.e, -(np.power((xe-e1),2)/(2*np.power(ve1,2)))))
ye2 = (1 / (np.sqrt(2 * np.pi * np.power(ve2,2)))) * (np.power(np.e, -(np.power((xe-e2),2)/(2*np.power(ve2,2)))))
plt.plot(xe,ye1,c="r",label="emergence distrib sp 1",alpha=0.5)
plt.plot(xe,ye2,c="b",label="emergence distrib sp 2",alpha=0.5)
plt.legend()
plt.title("Distribution of patrolling window positions of males at the end of simulations")

############################# graphics #######################################

# peak patrol time and patrol time range evolution plot
for i in range(replicates):
    plt.ylim(0,1)
    plt.plot(range(simulation_days),ha_evolution_list_sp1[i],c="r")
    plt.plot(range(simulation_days),ha_evolution_list_sp2[i],c="b")
plt.legend(["sp 1", "sp 2"])
plt.ylabel("Daily time")
plt.xlabel("Number of days")
plt.axhline(e1,c="#B40000",linewidth = 4,label="emergence peak sp 1")
plt.axhline(e2,c="#0013B4",linewidth = 4,label="emergence peak sp 2")
plt.title("Mean patrolling window position evolution")
plt.figtext(0.5,0.03, ["d = ",d, "dc = ",dlt_c,"de = ",dlt_e,"e1 = ",e1,"e2 = ",e2,"ve1 = ve2 = ",ve1 ,"K = ",K,"alpha12 = alpha21 = ",alpha12,"Beta = ",beta],ha="center",va="center",fontsize=12,)



for i in range(replicates):
    plt.ylim(0,1)
    plt.plot(range(simulation_days),wa_evolution_list_sp1[i],c="r")
    plt.plot(range(simulation_days),wa_evolution_list_sp2[i],c="b")
plt.legend(["sp 1", "sp 2"])
plt.ylabel("Daily time")
plt.xlabel("Number of days")
plt.title("Mean patrolling window duration evolution")
plt.figtext(0.5,0.03, ["d = ",d, "dc = ",dlt_c,"de = ",dlt_e,"e1 = ",e1,"e2 = ",e2,"ve1 = ve2 = ",ve1 ,"K = ",K,"alpha12 = alpha21 = ",alpha12,"Beta = ",beta],ha="center",va="center",fontsize=12,)



# mean_ha - e
for i in range(replicates):
    plt.plot(range(simulation_days),[x-e1 for x in ha_evolution_list_sp1[i]],c="r")
    plt.plot(range(simulation_days),[x-e2 for x in ha_evolution_list_sp2[i]],c="b")
plt.legend(["sp 1", "sp 2"])
plt.ylabel("Daily time")
plt.xlabel("Number of days")
plt.title("Mean patrolling window position evolution")



















plt.subplot(211)
plt.subplot(212)
plt.ylabel("Daily time")
plt.xlabel("Number of days")
plt.legend()
plt.title("Mean peak patrolling time (top) and mean patrolling range (bottom) evolution over " + str(simulation_days) + " days with baseline parameters \n and peak emergence time = 0.75")



plt.figure(0)
for i in range(replicates):
    plt.plot(range(simulation_days),wa_evolution_list[i],label="replicate n°" + str(i))
plt.ylim(0,1)
plt.ylabel("Daily time")
plt.xlabel("Number of days")
plt.axhline(ve,color="red",label="emergence time range")
plt.legend()
plt.title("Mean patrolling time range evolution over " + str(simulation_days) + " days")








# male presence barplot
"""
initial_patrolling_presence = []
for i in np.arange(0,1,0.01):
    initial_patrolling_presence.append(len(list_patrolling_males(i)))
# barplot male presence

plt.figure(3)
plt.bar(np.arange(0,1,0.01),patrolling_presence_list[0],width=0.008,label="final patrolling presence")
plt.bar(np.arange(0,1,0.01),initial_patrolling_presence,width=0.008,label="initial patrolling presence",alpha=0.6)
plt.ylabel("Number of patrolling males")
plt.xlabel("Daily time")
plt.title("Patrolling males presence after " + str(simulation_days) + " days for baseline parameters \n replicat n°" + str(0))
plt.axvline(e,label = "peak emergence time",c="red")
plt.legend()
"""


list_ha_initial = []
for i in range(100):
    list_ha_initial.append(stats.truncnorm.rvs((lower - initial_ha)/mu,(upper - initial_ha)/mu, initial_ha, mu))


# histogram of peak patrolling
plt.figure(3)
plt.hist(per_ha_final[0],bins=10,label="final peak patrolling time",color='0',edgecolor='1')
plt.hist(list_ha_initial,bins=5,label='initial peak patrolling time',color="0.9",edgecolor='0')
plt.xlim(0,1)
plt.ylabel("peak patrolling time of males")
plt.xlabel("Daily time")
plt.title("Peak patrolling time of all males after " + str(simulation_days) + " days \n replicat n°" + str(1))
plt.axvline(e,label = "peak emergence time",c="red")
plt.legend()


list_wa_initial = []
for i in range(100):
    list_wa_initial.append(stats.truncnorm.rvs((lower - initial_wa)/mu,(upper - initial_wa)/mu, initial_wa, mu))


ve = 0.05
# histogram of patrolling range
plt.figure(4)
plt.hist(wa_final[0],bins=10,label="final patrolling time range of males",color='0',edgecolor='1',alpha=0.6)
plt.hist(list_wa_initial,bins=10,label='initial patrolling time range of males',color="0.9",edgecolor='0',alpha=0.5)
plt.xlim(0,0.5)
plt.ylabel("Patrolling time range of males")
plt.xlabel("Daily time")
plt.title("Patrolling time range of males after " + str(simulation_days) + " days for baseline parameters \n replicat n°" + str(0))
plt.axvline(ve,label = "emergence time range",c="red")
plt.legend()




np.mean(ha_final[0]) - e
np.std(ha_final[0])
np.mean(wa_final[0]) - ve
np.std(wa_final[0])
final_sex_ratio[0]



















# heatmap with deltac and deltae
axis_deltac = [0,0.01,0.1]
axis_deltae = [0,0.01,0.1]

data_heatmap = [[0.05,0.03,0.02],[0.06,0.07,0.05],[0.08,0.09,0.1]]

plt.tricontour(axis_deltac,axis_deltae,Z=data_heatmap)

matplotlib.cmaps("viridis")









fig, ax = plt.subplots()
im = ax.imshow(data_heatmap)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(axis_deltac)))
ax.set_xtickslabels(axis_deltac)
ax.set_yticks(np.arange(len(axis_deltae)))
ax.set_ytickslabels(axis_deltae)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(axis_deltac)):
    for j in range(len(axis_deltae)):
        text = ax.text(j, i, data_heatmap[i, j],
                       ha="center", va="center", color="w")
        
ax.set_title("Effect of delta_c and delta_e on mean patrolling range")
fig.tight_layout()
plt.show()








import pandas as pd


e1_e2_1 = pd.DataFrame(
    {
     "wa_sp1" : pd.Series(wa_final_sp1[0]),
     "wa_sp2" : pd.Series(wa_final_sp2[0]),
     "e1" : e1,
     "e2" : e2,
     "replica" : 1
     }
    )

e1_e2_2 = pd.DataFrame(
    {
     "wa_sp1" : pd.Series(wa_final_sp1[1]),
     "wa_sp2" : pd.Series(wa_final_sp2[1]),
     "e1" : e1,
     "e2" : e2,
     "replica" : 2
     }
    )

e1_e2_3 = pd.DataFrame(
    {
     "wa_sp1" : pd.Series(wa_final_sp1[2]),
     "wa_sp2" : pd.Series(wa_final_sp2[2]),
     "e1" : e1,
     "e2" : e2,
     "replica" : 3
     }
    )

e1_e2_4 = pd.DataFrame(
    {
     "wa_sp1" : pd.Series(wa_final_sp1[3]),
     "wa_sp2" : pd.Series(wa_final_sp2[3]),
     "e1" : e1,
     "e2" : e2,
     "replica" : 4
     }
    )

e1_e2_5 = pd.DataFrame(
    {
     "wa_sp1" : pd.Series(wa_final_sp1[4]),
     "wa_sp2" : pd.Series(wa_final_sp2[4]),
     "e1" : e1,
     "e2" : e2,
     "replica" : 5
     }
    )

e1_e2_6 = pd.DataFrame(
    {
     "wa_sp1" : pd.Series(wa_final_sp1[5]),
     "wa_sp2" : pd.Series(wa_final_sp2[5]),
     "e1" : e1,
     "e2" : e2,
     "replica" : 6
     }
    )

e1_e2_7 = pd.DataFrame(
    {
     "wa_sp1" : pd.Series(wa_final_sp1[6]),
     "wa_sp2" : pd.Series(wa_final_sp2[6]),
     "e1" : e1,
     "e2" : e2,
     "replica" : 7
     }
    )

e1_e2_8 = pd.DataFrame(
    {
     "wa_sp1" : pd.Series(wa_final_sp1[7]),
     "wa_sp2" : pd.Series(wa_final_sp2[7]),
     "e1" : e1,
     "e2" : e2,
     "replica" : 8
     }
    )

e1_e2_9 = pd.DataFrame(
    {
     "wa_sp1" : pd.Series(wa_final_sp1[8]),
     "wa_sp2" : pd.Series(wa_final_sp2[8]),
     "e1" : e1,
     "e2" : e2,
     "replica" : 9
     }
    )

e1_e2_10 = pd.DataFrame(
    {
     "wa_sp1" : pd.Series(wa_final_sp1[9]),
     "wa_sp2" : pd.Series(wa_final_sp2[9]),
     "e1" : e1,
     "e2" : e2,
     "replica" : 10
     }
    )




e1_e2_50 = pd.concat([e1_e2_1,e1_e2_2,e1_e2_3,e1_e2_4,e1_e2_5,e1_e2_6,e1_e2_7,e1_e2_8,e1_e2_9,e1_e2_10],axis=0)

wa_table_e1_e2 = pd.concat([e1_e2_50,e1_e2_45,e1_e2_40,e1_e2_35,e1_e2_30,e1_e2_25],axis=0)


# importing the dataframe from text
ha_table_e1_e2 = ha_table_e1_e2txt.drop("Unnamed: 0",axis=1)
# don't forget to import as DataFrame

x_axis = ha_table_e1_e2["e2"] - ha_table_e1_e2["e1"]
y_axis = ha_table_e1_e2["ha_sp2"] - ha_table_e1_e2["ha_sp1"]

plt.plot(x_axis,y_axis)
plt.xlabel("e2 - e1")
plt.ylabel("ha2 - ha1")


# boxplot sur les 10 valeurs de moyenne de réplicat
ha_mean_tab = ha_table_e1_e2.groupby(["e1","e2","replica"]).mean()
y_axis = ha_mean_tab["ha_sp2"] - ha_mean_tab["ha_sp1"]

y_axis1 = y_axis[(0.25,0.25,)]
#y_axis2 = y_axis[(0.25,0.275,)]
y_axis3 = y_axis[(0.25,0.3,)]
y_axis4 = y_axis[(0.25,0.35,)]
y_axis5 = y_axis[(0.25,0.4,)]
y_axis6 = y_axis[(0.25,0.45,)]
y_axis7 = y_axis[(0.25,0.5,)]
y_axis8 = y_axis[(0.25,0.75,)]

plt.boxplot(x=[y_axis1,y_axis3,y_axis4,y_axis5,y_axis6,y_axis7],labels = [0,0.05,0.1,0.15,0.2,0.25])
plt.xlabel("e2 - e1",fontsize=22)
plt.ylabel("ha2 - ha1",fontsize=22)
plt.figtext(0.5,0.02, s=["d = ",d, "dc = ",dlt_c,"de = ",dlt_e,"ve1 = ve2 = ",ve1 ,"K ",K,"alpha12 = alpha21 = ",alpha12,"Beta = ",beta],ha="center",va="center",fontsize=22)
plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)



# ha1 - e1
ha1_minus_e1_0 = (ha_mean_tab["ha_sp1"] - 0.25)[(0.25,0.25,)]
ha1_minus_e1_5 = (ha_mean_tab["ha_sp1"] - 0.25)[(0.25,0.3,)]
ha1_minus_e1_10 = (ha_mean_tab["ha_sp1"] - 0.25)[(0.25,0.35,)]
ha1_minus_e1_15 = (ha_mean_tab["ha_sp1"] - 0.25)[(0.25,0.4,)]
ha1_minus_e1_20 = (ha_mean_tab["ha_sp1"] - 0.25)[(0.25,0.45,)]
ha1_minus_e1_25 = (ha_mean_tab["ha_sp1"] - 0.25)[(0.25,0.5,)]
ha1_minus_e1_50 = (ha_mean_tab["ha_sp1"] - 0.25)[(0.25,0.75,)]

plt.boxplot(x=[ha1_minus_e1_0,ha1_minus_e1_5,ha1_minus_e1_10,ha1_minus_e1_15,ha1_minus_e1_20,ha1_minus_e1_25],labels = [0,0.05,0.1,0.15,0.2,0.25])
plt.xlabel("e2 - e1",fontsize=22)
plt.ylabel("ha1 - e1",fontsize=22)
plt.figtext(0.5,0.02, s=["d = ",d, "dc = ",dlt_c,"de = ",dlt_e,"ve1 = ve2 = ",ve1 ,"K ",K,"alpha12 = alpha21 = ",alpha12,"Beta = ",beta],ha="center",va="center",fontsize=22)
plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)

# ha2 - e2
ha2_minus_e2_0 = (ha_mean_tab["ha_sp2"] - 0.25)[(0.25,0.25,)]
ha2_minus_e2_5 = (ha_mean_tab["ha_sp2"] - 0.3)[(0.25,0.3,)]
ha2_minus_e2_10 = (ha_mean_tab["ha_sp2"] - 0.35)[(0.25,0.35,)]
ha2_minus_e2_15 = (ha_mean_tab["ha_sp2"] - 0.4)[(0.25,0.4,)]
ha2_minus_e2_20 = (ha_mean_tab["ha_sp2"] - 0.45)[(0.25,0.45,)]
ha2_minus_e2_25 = (ha_mean_tab["ha_sp2"] - 0.5)[(0.25,0.5,)]
ha2_minus_e2_50 = (ha_mean_tab["ha_sp2"] - 0.75)[(0.25,0.75,)]

plt.boxplot(x=[ha2_minus_e2_0,ha2_minus_e2_5,ha2_minus_e2_10,ha2_minus_e2_15,ha2_minus_e2_20,ha2_minus_e2_25],labels = [0,0.05,0.1,0.15,0.2,0.25])
plt.xlabel("e2 - e1",fontsize=22)
plt.ylabel("ha2 - e2",fontsize=22)
plt.figtext(0.5,0.02, s=["d = ",d, "dc = ",dlt_c,"de = ",dlt_e,"ve1 = ve2 = ",ve1 ,"K ",K,"alpha12 = alpha21 = ",alpha12,"Beta = ",beta],ha="center",va="center",fontsize=22)
plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)




# tentative de representer ha2_ha1, ha1 - e1 et ha2 - e2 sur le même plot

x_axis = [0,0,0,0,0,0,0,0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,]

plt.scatter(x_axis,y=[y_axis1,y_axis3,y_axis4,y_axis5,y_axis6,y_axis7,y_axis8],label = "ha2 - ha1",alpha=0.5)
plt.scatter(x_axis,y=[ha1_minus_e1_0,ha1_minus_e1_5,ha1_minus_e1_10,ha1_minus_e1_15,ha1_minus_e1_20,ha1_minus_e1_25,ha1_minus_e1_50],label = "ha1 - e1",alpha=0.5)
plt.scatter(x_axis,y=[ha2_minus_e2_0,ha2_minus_e2_5,ha2_minus_e2_10,ha2_minus_e2_15,ha2_minus_e2_20,ha2_minus_e2_25,ha2_minus_e2_50],label = "ha2 - e2",alpha=0.5)
plt.xlabel("e2 - e1 value",fontsize=22)
plt.ylabel("",fontsize=22)
plt.legend()
plt.figtext(0.5,0.02, s=["d = ",d, "dc = ",dlt_c,"de = ",dlt_e,"ve1 = ve2 = ",ve1 ,"K = ",K1,"alpha12 = alpha21 = ",alpha12,"Beta = ",beta],ha="center",va="center",fontsize=22)
plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)


# wa2 - wa1 en fct de e2 - e1
wa_mean_tab = wa_table_e1_e2.groupby(["e1","e2","replica"]).mean()
y_axis = wa_mean_tab["wa_sp2"] - wa_mean_tab["wa_sp1"]
wa_mean_sp2 = wa_mean_tab["wa_sp2"]
wa_mean_sp1 = wa_mean_tab["wa_sp1"]

wa_mean_sp2_0 = wa_mean_sp2[(0.25,0.25,)]
wa_mean_sp2_5 = wa_mean_sp2[(0.25,0.3,)]
wa_mean_sp2_10 = wa_mean_sp2[(0.25,0.35,)]
wa_mean_sp2_15 = wa_mean_sp2[(0.25,0.4,)]
wa_mean_sp2_20 =wa_mean_sp2[(0.25,0.45,)]
wa_mean_sp2_25 =wa_mean_sp2[(0.25,0.5,)]

wa_mean_sp1_0 = wa_mean_sp1[(0.25,0.25,)]
wa_mean_sp1_5 = wa_mean_sp1[(0.25,0.3,)]
wa_mean_sp1_10 = wa_mean_sp1[(0.25,0.35,)]
wa_mean_sp1_15 = wa_mean_sp1[(0.25,0.4,)]
wa_mean_sp1_20 =wa_mean_sp1[(0.25,0.45,)]
wa_mean_sp1_25 =wa_mean_sp1[(0.25,0.5,)]






y_axis1 = y_axis[(0.25,0.25,)]
y_axis3 = y_axis[(0.25,0.3,)]
y_axis4 = y_axis[(0.25,0.35,)]
y_axis5 = y_axis[(0.25,0.4,)]
y_axis6 = y_axis[(0.25,0.45,)]
y_axis7 = y_axis[(0.25,0.5,)]

plt.boxplot(x=[y_axis1,y_axis3,y_axis4,y_axis5,y_axis6,y_axis7],labels = [0,0.05,0.1,0.15,0.2,0.25])
plt.xlabel("e2 - e1",fontsize=22)
plt.ylabel("wa2 - wa1",fontsize=22)
plt.figtext(0.5,0.02, s=["d = ",d, "dc = ",dlt_c,"de = ",dlt_e,"ve1 = ve2 = ",ve1 ,"K ",K1,"alpha12 = alpha21 = ",alpha12,"Beta = ",beta],ha="center",va="center",fontsize=22)
plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)



x_axis = [0,0,0,0,0,0,0,0,0,0,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.15,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25,0.25]

plt.scatter(x_axis,y=[wa_mean_sp1_0,wa_mean_sp1_5,wa_mean_sp1_10,wa_mean_sp1_15,wa_mean_sp1_20,wa_mean_sp1_25],label = "wa1")
plt.scatter(x_axis,y=[wa_mean_sp2_0,wa_mean_sp2_5,wa_mean_sp2_10,wa_mean_sp2_15,wa_mean_sp2_20,wa_mean_sp2_25],label = "wa2")
plt.xlabel("e2 - e1 value",fontsize=22)
plt.ylim(0,0.5)
plt.ylabel("",fontsize=22)
plt.legend()
plt.figtext(0.5,0.02, s=["d = ",d, "dc = ",dlt_c,"de = ",dlt_e,"ve1 = ve2 = ",ve1 ,"K = ",K1,"alpha12 = alpha21 = ",alpha12,"Beta = ",beta],ha="center",va="center",fontsize=22)
plt.rc('xtick',labelsize=16)
plt.rc('ytick',labelsize=16)










"""
plt.scatter(x_axis,y_axis)
plt.xlabel("e2 - e1")
plt.ylabel("ha2 - ha1")
plt.figtext(0.5,0.03, ["d = ",d, "dc = ",dlt_c,"de = ",dlt_e,"ve1 = ve2 = ",ve1 ,"\n" "K1 = K2 = ",K1,"alpha12 = alpha21 = ",alpha12,"Beta = ",beta],ha="center",va="center",fontsize=12)

# boxplot on all values 
ha_table_e1_e2["ha_sp2 - ha_sp1"] = ha_table_e1_e2["ha_sp2"] - ha_table_e1_e2["ha_sp1"]

y_axis1 = ha_table_e1_e2[ha_table_e1_e2.e2 == 0.25]["ha_sp2 - ha_sp1"].dropna()
y_axis2 = ha_table_e1_e2[ha_table_e1_e2.e2 == 0.275]["ha_sp2 - ha_sp1"].dropna()
y_axis3 = ha_table_e1_e2[ha_table_e1_e2.e2 == 0.3]["ha_sp2 - ha_sp1"].dropna()
y_axis4 = ha_table_e1_e2[ha_table_e1_e2.e2 == 0.35]["ha_sp2 - ha_sp1"].dropna()
y_axis5 = ha_table_e1_e2[ha_table_e1_e2.e2 == 0.4]["ha_sp2 - ha_sp1"].dropna()
y_axis6 = ha_table_e1_e2[ha_table_e1_e2.e2 == 0.45]["ha_sp2 - ha_sp1"].dropna()
y_axis7 = ha_table_e1_e2[ha_table_e1_e2.e2 == 0.5]["ha_sp2 - ha_sp1"].dropna()
y_axis8 = ha_table_e1_e2[ha_table_e1_e2.e2 == 0.75]["ha_sp2 - ha_sp1"].dropna()


plt.boxplot(x=[y_axis1,y_axis2,y_axis3,y_axis4,y_axis5,y_axis6,y_axis7,y_axis8],labels = [0,2.5,5,10,15,20,25,50])
plt.xlabel("e2 - e1")
plt.ylabel("ha2 - ha1")
plt.title("")
"""




