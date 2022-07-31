# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:58:11 2022

@author: abrunaud
"""

import random as r
import numpy as np
import scipy.stats as stats


#################### simulation over several days with replicates  #####################


simulation_days = 400      # duration of each replicate
replicates = 100            # number of replicates

# output variable to retrieve at the end of each replicate
ha_evolution_list_sp1 = []   # stores all replicates of "evolution of mean patrolling window position of sp1"
ha_evolution_list_sp2 = []   # stores all replicates of "evolution of mean patrolling window position of sp2"
wa_evolution_list_sp1 = []   # stores all replicates of "evolution of mean patrolling window width of sp1"
wa_evolution_list_sp2 = []   # stores all replicates of "evolution of mean patrolling window width of sp2"

ha_final_sp1 = []            # stores patrolling window position of all males of sp1
ha_final_sp2 = []            # stores patrolling window position of all males of sp2
wa_final_sp1 = []            # stores patrolling window width of all males of sp1
wa_final_sp2 = []            # stores patrolling window width of all males of sp2
final_sex_ratio_sp1 = []     # stores final sex ratio (sex ratio of the population at the end of simulation) of sp1
final_sex_ratio_sp2 = []     # stores final sex ratio of sp2

pop_sp1_size_replica = []    # stores sp 1 population size evolution for all replica
pop_sp2_size_replica = []    # stores sp 2 population size evolution for all replica

for z in range(replicates):              # repeat for desired replicate number
    mean_ha_evolution_sp1 = []           # used to track the evolution of mean patrolling window position of sp1
    mean_ha_evolution_sp2 = []           # used to track the evolution of mean patrolling window position of sp2
    mean_wa_evolution_sp1 = []           # used to track the evolution of mean patrolling window width of sp 1
    mean_wa_evolution_sp2 = []           # used to track the evolution of mean patrolling window width of sp 2
    pop_size_sp1 = []                    # used to track the evolution of population size of sp 1
    pop_size_sp2 = []                    # used to track the evolution of population size of sp 2
    
    # initialisation of the population
    population = []                                               # list of all individuals
    initial_abund_1 = 100                                         # initial effective of sp 1
    initial_abund_2 = 100                                         # initial effective of sp 2
    
    for j in range(initial_abund_1):                              # creation of sp 1 
        initial_ha1 = np.random.uniform(0,1)                      # initial patrolling window position is random for each individual
        population.append(individuals(r.sample(["M","F"],1)[0],
                                stats.truncnorm.rvs((lower - initial_ha1)/mu,(upper-initial_ha1)/mu, initial_ha1, mu), 
                                stats.truncnorm.rvs((lower - initial_wa1)/mu,(upper-initial_wa1)/mu, initial_wa1, mu), 
                                0,
                                1))
    for k in range(initial_abund_2):                              # creation of sp 2
        initial_ha2 = np.random.uniform(0,1)                      # initial patrolling window position is random for each individual
        population.append(individuals(r.sample(["M","F"],1)[0],
                                stats.truncnorm.rvs((lower - initial_ha2)/mu,(upper-initial_ha2)/mu, initial_ha2, mu), 
                                stats.truncnorm.rvs((lower - initial_wa2)/mu,(upper-initial_wa2)/mu, initial_wa2, mu), 
                                0,
                                2))
        
    for k in range(simulation_days): # for desired duration of replicates
        
        t = 0 # reset initial time to 0, corresponds to the start of the day
        
        emergences_today = emergences_and_schedule(population)                        # retrieves emergence list and emergence schedule of the day
        known_events = patrolling_schedule_males(population) | emergences_today[1]    # creates a dictionary of events (emergences and patrol shifts) supposedly happening on this day 
        known_events[1] = "end day"                                                   # adding the end of the day event to known_events
        chronological_events = sorted(known_events.keys())                            # sort events of the day chronologically
        
        for i in range(len(chronological_events)):                          
            while t < chronological_events[i]:                                        # until the next "known" event happens
                t = event(population,t,chronological_events[i])                       # determine if an event happens and which event, or if no event happens between ti and T
            if known_events.get(chronological_events[i])[2] == "e":                   # determines if "known" event is an emergence
                if known_events.get(chronological_events[i])[-1] == "M":              # for emergent males
                    emergences_today[0][int(known_events.get(chronological_events[i])[19:-1])].ha = - emergences_today[0][int(known_events.get(chronological_events[i])[19:-1])].ha
                    emergences_today[0][int(known_events.get(chronological_events[i])[19:-1])].wa = - emergences_today[0][int(known_events.get(chronological_events[i])[19:-1])].wa
                    # ha and wa of male newborns are made negative to make them non-patrolling on their first day    
                population.append(emergences_today[0][int(known_events.get(chronological_events[i])[19:-1])]) # emerging individual is added to the population

        for j in range(len(population)):                                              # allows males who emerged on previous day to patrol
            if population[j].ha < 0 and population[j].wa < 0:
                population[j].ha = - population[j].ha                                 # turn back the ha to positive
                population[j].wa = - population[j].wa                                 # turn back the wa to positive
        
        mean_ha_evolution_sp1.append(np.mean(list_ha_of_males_sp1(population)))       # registers the mean patrolling window position of males of sp 1 at the end of the day
        mean_ha_evolution_sp2.append(np.mean(list_ha_of_males_sp2(population)))       # registers the mean patrolling window position of males of sp 2 at the end of the day
        mean_wa_evolution_sp1.append(np.mean(list_wa_of_males_sp1(population)))       # registers the mean patrolling window width of males of sp 1 at the end of the day
        mean_wa_evolution_sp2.append(np.mean(list_wa_of_males_sp2(population)))       # registers the mean patrolling window width of males of sp 1 at the end of the day
        pop_size_sp1.append(size_sp1_sp2(population)[0])                                          # registers the population size at the end of the day
        pop_size_sp2.append(size_sp1_sp2(population)[1])
        
    # end of replicates : registering output variables
    
    ha_evolution_list_sp1.append(mean_ha_evolution_sp1)                               # registers the evolution of mean patrolling window position of males of sp 1 at the end of the replica
    ha_evolution_list_sp2.append(mean_ha_evolution_sp2)                               # registers the evolution of mean patrolling window position of males of sp 2 at the end of the replica
    wa_evolution_list_sp1.append(mean_wa_evolution_sp1)                               # registers the evolution of patrolling window width of males of sp 1 at the end of the replica
    wa_evolution_list_sp2.append(mean_wa_evolution_sp2)                               # registers the evolution of patrolling window width of males of sp 2 at the end of the replica
    
    ha_final_sp1.append(list_ha_of_males_sp1(population))                             # registers final patrolling window position of all males of sp 1 at the end of the replica
    ha_final_sp2.append(list_ha_of_males_sp2(population))                             # registers final patrolling window position of all males of sp 2 at the end of the replica
    wa_final_sp1.append(list_wa_of_males_sp1(population))                             # registers final patrolling window width of all males of sp 1 at the end of the replica
    wa_final_sp2.append(list_wa_of_males_sp2(population))                             # registers final patrolling window width of all males of sp 2 at the end of the replica
    final_sex_ratio_sp1.append(sex_ratio_sp1(population))                             # registers final sex-ratio of sp 1 at the end of the replica
    final_sex_ratio_sp2.append(sex_ratio_sp2(population))                             # registers final sex-ratio of sp 1 at the end of the replica
    pop_sp1_size_replica.append(pop_size_sp1)                                         # registers the evolution of sp 1 population size at the end of the replica
    pop_sp2_size_replica.append(pop_size_sp2)                                         # registers the evolution of sp 2 population size at the end of the replica


















"""
ha_evolution_matrix_delta_e_delta_c = {}           # arrays used to retrieve data
wa_evolution_matrix_delta_e_delta_c = {}
ha_final_matrix_delta_e_delta_c = {}
wa_final_matrix_delta_e_delta_c = {}
final_sex_ratio_matrix_delta_e_delta_c = {}

for delta_e_range in np.linspace(0,0.1,11):
    for delta_c_range in np.linspace(0,0.1,11):
        
        parameter_set_key = "de = ",str(delta_e_range)," and dc = ", str(delta_c_range)
        
        dlt_e = delta_e_range
        dlt_c = delta_c_range

                 
        #ha_evolution_matrix_delta_e_delta_c[parameter_set_key] = ha_evolution_list
        #wa_evolution_matrix_delta_e_delta_c[parameter_set_key] = wa_evolution_list
        #ha_final_matrix_delta_e_delta_c[parameter_set_key] = ha_final
        wa_final_matrix_delta_e_delta_c[parameter_set_key] = wa_final
        final_sex_ratio_matrix_delta_e_delta_c[parameter_set_key] = final_sex_ratio
"""





########################## testing simulation over 1 day ##############################


"""
population = []
for j in range(100):        # appending of all offsprings in emer
    initial_ha1 = np.random.uniform(0,1)
    population.append(individuals(r.sample(["M","F"],1)[0],
                            stats.truncnorm.rvs((lower - initial_ha1)/mu,(upper-initial_ha1)/mu, initial_ha1, mu), 
                            stats.truncnorm.rvs((lower - initial_wa1)/mu,(upper-initial_wa1)/mu, initial_wa1, mu), 
                            0,
                            1))
for k in range(100):
    initial_ha2 = np.random.uniform(0,1)
    population.append(individuals(r.sample(["M","F"],1)[0],
                            stats.truncnorm.rvs((lower - initial_ha2)/mu,(upper-initial_ha2)/mu, initial_ha2, mu), 
                            stats.truncnorm.rvs((lower - initial_wa2)/mu,(upper-initial_wa2)/mu, initial_wa2, mu), 
                            0,
                            2))

t = 0

emergences_today = emergences_and_schedule(population)
known_events = patrolling_schedule_males(population) | emergences_today[1] # dict of events (emergences and patrol shifts) supposedly happening on this day 
known_events[1] = "end day"                   # adding the end of the day event to known_events
chronological_events = sorted(known_events.keys())        # sort events of the day chronologically

for i in range(len(chronological_events)):   
    while t < chronological_events[i]:                      # until the next "known" event happens
        t = event(population,t,chronological_events[i])                # determine if an event happens and which event, or nothing 
    if known_events.get(chronological_events[i])[2] == "e":       # if "known" event is an emergence
        if known_events.get(chronological_events[i])[-1] == "M":
            emergences_today[0][int(known_events.get(chronological_events[i])[19:-1])].ha = - emergences_today[0][int(known_events.get(chronological_events[i])[19:-1])].ha
            emergences_today[0][int(known_events.get(chronological_events[i])[19:-1])].wa = - emergences_today[0][int(known_events.get(chronological_events[i])[19:-1])].wa
            # ha and wa of male newborns are made negative to make them non-patrolling on their first day
        population.append(emergences_today[0][int(known_events.get(chronological_events[i])[19:-1])])
    # elif known_events.get(chronological_events[i])[2] == "t":     # if "known" event is an entry (in patrol)
    #     pass
    # elif known_events.get(chronological_events[i])[2] == "i":     # if "known" event is an exit of patrol
    #     pass

for j in range(len(population)):             # allows males who emerged on previous day to patrol
    if population[j].ha < 0 and population[j].wa < 0:
        population[j].ha = - population[j].ha     # turn back the ha to positive
        population[j].wa = - population[j].wa     # turn back the wa to positive



"""


