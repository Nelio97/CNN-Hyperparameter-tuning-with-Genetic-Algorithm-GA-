#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 17:10:34 2019

@author: njcandelaria
"""

#!/usr/bin/env python2
# -*- coding: utf-8 -*-


import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.insert(1, '/opt/anaconda/lib/python2.7/site-packages/IPython/core/ultratb.py')
#import ultratb.py
#sys.excepthook = ultratb.ColorTB()

import ga
import random
import numpy as np
import datetime
import time
import matplotlib.pyplot as plt
from automatic_create_and_train_data2_mnist import *
#from sending_email import send_me_an_email

#global classId
#global nBatches
#global nChannels
#global resultsDir
#global imgResizeHeight
#global imgResizeWidth 
#global dataDir 
#global filename

""" 
        Created on Thu Aug  1 11:55:17 2019
        @author: njcandelaria

        Hyperparameter Tuning Script for CNN.
        
        The following code generates a population of CNN parameters and then runs
    a Genetic Algorithm (GA).
    
        This was a first attempt to make this task, and the code is set so that each
    gene has N elements in it, N being the total number of weights in the CNN (all of 
    these values belong to [0,1[).
    
        THIS IMPLIES THAT THE ACTUAL CNN CODE DOES NOT INCLUDE BACKPROPAGATION.
    
        The GA operators come from module ga_v1.py.
    
        The code for the CNN was developed by Helena Pereira (PhD student, IBEB).


    INPUT ARGUMENTS:
        gen_size            :           num of genes in each generation
        max_gen             :           max. num of generations
        N                   :           number of parameters inside a gene
        stop_delta          :           min. variation of max. accuracy values
        stop_gen            :           max. value of generations for which the accuracy value
                                    is allowed to increase less than delta
        
    OTHER ARGUMENTS:
        accuracy            :           nup.array where accuracy values for each gene are stored
        performance         :           list where the highest accuracy values for each generation are stored
        performer           :           list where the genes corresponding to the values in performance are stored
        means               :           list of the mean accuracy value for each generation
        stdandart           :           list of the stadart variations of accuracy for each generarion
        convergence         :           list where variations of performance values are stored
        t                   :           list where all counters are saved (just for plotting purposes)
        
        
    STOPPING CRITERIA:
        max_gen                 :       reached the max. value of generations
        stop_gen & stop_delta   :       reached a point where, even if there are more generations,
                                    there's no significant variation of accuracy value  
"""
# Starting timer
timer = [float(time.time())]

# Current time
datetime.datetime.now()

gen_size = 10
max_gen = 10
stop_delta = float(0.00001)
stop_gen = 3

# Hyperparameters
hyperparam_range = [[10,200], [2,7], [0,2], [2,7], [0,2], [10,200], [2,7], [0,2], [2,7], [0,2], [50,200]]
N = int(len(hyperparam_range))

performance = []                                    
performer = []  
                        
mean_values = []
standart_deviation = []

convergence = []
t = []

def test_convergence(l, n):    
    if n > len(l): return False
    step = 0
    for i in l:
        if i <= stop_delta:
            step += 1
            if step == n: return True
    return False    

def send_me_an_email():
    
    import smtplib

    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    
    from_add = '...'
    to_add = "..."
    
    msg =  MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    
    msg['Subject'] = "Ping: Code ready"
    body = 'I believe your code is ready, sir.'
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_add, '...password...')
    text = msg.as_string()
    server.sendmail(from_add, to_add, text)
    server.quit()


# Criar a 1ª geração (genes com parâmetros aleatórios)
gen = ga.initial_population(gen_size,hyperparam_range)
                                  
for counter in range(max_gen): # Ao longo das várias gerações
    
    means_row = []
    std_row = []
    
#    accuracy_row = []
#    accuracy = []
    t.append(counter)
    print('----- Generation ' + str(counter) + ' -----')
    for k in range(gen_size):  # Ao longo dos genes da mesma geração
        
        # ---------------------------------------------------------------------
        """
        PSEUDOCÓDIGO
                
        1. Correr a CNN para o gene generation(k) """
        # Para simplificar, o output do CNN será:   accuracy(generation(k))
        
        
#        classIds = '_0class,_1class,_2class,_3class,_4class,_5class,_6class,_7class,_8class,_9class'
#        values = [1,0.1]
        
        
        values = run(gen[k])
        print 'values'
        print values
#        nBatches = 5
#        nChannels = 1
#        imgResizeHeight = 28
#        imgResizeWidth = 28
#        classIds = '_0class,_1class,_2class,_3class,_4class,_5class,_6class,_7class,_8class,_9class'
#        classId = ['_0class', '_1class', '_2class', '_3class', '_4class', '_5class', '_6class', '_7class', '_8class', '_9class']
##        resultsDir = '/home/FC/njcandelaria/caffemaster/interface/my_trained_nets_mnist_database/results_1000_v1'
#        resultsDir = '/home/FC/njcandelaria/Documents/mnist_results_1000_v'
#        
#        createNets(resultsDir, resultsDir, classId, nBatches, nChannels, imgResizeHeight,imgResizeWidth, "1",gen[k])
#        runBatches(resultsDir, resultsDir, classId, nBatches, "1")
#        readBatches(resultsDir, resultsDir, classId, nBatches, nChannels, "1")
#        print dataDir
#        
        

        
        """
        2. Colocar o fitness de generation(k) na coluna k da matriz ouput_matrix
        """   
        
        # Preciso de correr os ficheiros de forma a obter a média dos batches e o seu desvio padrão
        # Quanto maior for a média da accuracy e menor o seu std, melhor é a arquitetura...
        
#        this_mean = float(np.mean(values[0]))      # Média das médias
#        this_std = float(np.mean(values[1]))       # Standart Deviation médio
#        
#        means_row.append(this_mean)
#        std_row.append(this_std)
        
        means_row.append(float(np.mean(values[0])))
        std_row.append(float(np.mean(values[1])))
        

        # ---------------------------------------------------------------------
    
    # Updating timer
    timer.append(float(time.time()))
    delta_t = float(timer[int(counter)])-float(timer[int(counter-1)])
      
    
    
    
    
    # Finding the max value for accuracy mean (for this generation)
    gen_means = np.array(means_row)
    gen_std = np.array(std_row)
    
    find = np.where(gen_means == np.max(gen_means))
    find1 = int(find[0][0])
    best_performer = [gen_means[find1],gen_std[find1]]
    performance.append(best_performer)
    performer.append(gen[find1])
    
    
    # Finding the mean values (and standart deviation) for accuracy, for this generation
    
    
    
    gen_means_mean = float(np.mean(gen_means))  # A média dos valores médios
    mean_values.append(gen_means_mean)
    
    gen_std_mean = float(np.mean(gen_std))
    standart_deviation.append(gen_std_mean)     # A média dos desvios padrões
    
    
    
    print("Generation: " + str(counter))
    print(datetime.datetime.now())
    print("Time spent: " + str(datetime.timedelta(seconds=delta_t)))
    print("Max. accuracy value (and respective std): " + str(performance[int(counter)]))
    print("Mean accuracy value: " + str(gen_means_mean))
    print("Standart deviation: " + str(gen_std_mean))
    print(" ----------------------------------------------------------------- ")

    
#    if test_convergence(performance,int(stop_gen)) == True: 
#        break
    
    # Defining this generation's mating pool
    chosen_parents = ga.mating_pool(gen,gen_means_mean,0.20,0.10)
    
    
    # Crossover
    crossed_over = ga.crossover(chosen_parents,gen)
    
    
    # Mutation
    offspring = ga.mutation(crossed_over,0.10,0.10,hyperparam_range)
    
    
    # Checking for convergence
    if counter > 1:
        acc_variation = (float(performance[int(counter)])-float(performance[int(counter-1)]))/(float(performance[int(counter-1)]))
        convergence.append(acc_variation)
        
        if test_convergence(performance,int(stop_gen)) == False:
            
            # The mutated generation becomes generation (for the next iteration)
            gen = offspring
            
        else:
            
            # Plotting information
            
            print("Cycle stopped at generation " + str(counter))
            timer.append(float(time.time()))
            print(datetime.datetime.now())
            final_delta_t = float(timer[int(counter)])-float(timer[0])
            print("Time spent: " + str(datetime.timedelta(seconds=final_delta_t)))
                
            # Plotting results
            
            plt.figure(1)
            plt.title("Max. fitness values (for " + str(counter) + " generations)")
            plt.scatter(t,performance)
            plt.ylim(0.0, 1.0)
            plt.grid(True)
            plt.xticks(t)
            plt.show()
            plt.savefig('Max_fitness_values.png')
            
            plt.figure(2)
            plt.title("Mean_fitness_values (for " + str(counter) + " generations)")
            plt.scatter(t,means)
            plt.ylim(0.0, 1.0)
            plt.grid(True)
            plt.xticks(t)
            plt.savefig('Mean_fitness_values.png')
                
            plt.figure(3)
            plt.title("Std deviation fitness values (for " + str(counter+1) + " generations)")
            plt.scatter(t,means)
            plt.ylim(0.0, 1.0)
            plt.grid(True)
            plt.xticks(t)
            plt.savefig('Std_dev_fitness_values.png')
                
            send_me_an_email()
            
            break
        
    
"""
Plot resultados
"""
plt.figure(1)
plt.title("Max. fitness values (for " + str(counter+1) + " generations)")
plt.scatter(t,performance)
plt.ylim(0.0, 1.0)
plt.grid(True)
plt.xticks(t)
#plt.show()
plt.savefig('Max_fitness_values.png')

plt.figure(2)
plt.title("Mean fitness values (for " + str(counter+1) + " generations)")
plt.scatter(t,means)
plt.ylim(0.0, 1.0)
plt.grid(True)
plt.xticks(t)
#plt.show()
plt.savefig('Mean_fitness_values.png')

#plt.figure(3)
#plt.title("Std deviation fitness values (for " + str(counter+1) + " generations)")
#plt.scatter(t,means)
#plt.ylim(0.0, 1.0)
#plt.grid(True)
#plt.xticks(t)
#plt.savefig('Std_dev_fitness values.png')

send_me_an_email()

