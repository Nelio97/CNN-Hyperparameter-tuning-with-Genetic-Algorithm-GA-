#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:37:50 2019
#!/usr/bin/env python2
# -*- coding: utf-8 -*-

Created on Fri Jul 26 09:53:56 2019
@author: njcandelaria

Genetic Algorithm (módulo)

BASEADO EM:
https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6    
    

FUNÇÕES:
    
    create_population           >   criar a 1ª geração (valores alatórios)
    calc_fitness                >   calculo do fitness (para cada gene)
    mating_pool                 >   seleção dos parents de cada geração, com base no fitness
    crossover                   >   crossover dos parents
    mutation                    >   mutações aleatórias
    
"""
import numpy as np
import random
from automatic_create_and_train_data2_mnist import *




#list_param = [[10,200], [2,3], [1,2], [10,200], [50,200]]
#"""              0        1      2       3         4      """


def initial_population(population_size, list_param, img_height, img_width):
    
    
    print('Initial dimensions:  (' + str(img_height) + ',' + str(img_width) + ')')
    
    """
    These are the hyperparameters that can have any value within a range.
    """
    # CONV 1
    low_num_filters_conv1 = list_param[0][0]    #    Number of filters (range)
    high_num_filters_conv1 = list_param[0][1]
    
    
    # CONV 2
    low_num_filters_conv2 = list_param[3][0]    #    Number of filters (range)
    high_num_filters_conv2 = list_param[3][1]

    
    # FULLY CONECTED LAYER
    low_num_full = list_param[4][0]
    high_num_full = list_param[4][1]
    
    
    
    
    """
    The remaining hyperparameters depend on other variables, such as:
        - other hyperparameters (the stride depends on the kernel size)
        - image dimensions (both the kernel size and stride depend on it)
        
    The purpose of the following functions is to get the latter hyperparameters.
    """
    def get_rand_kernel(height,width,list_param): # Cria varios kernels possiveis, com base no tamanho da imagem 
        import random
        if (int(height) == int(width)):  # Imagens quadradas!
            
            i_k = int(list_param[1][0])
            print('i_k'); print(i_k)
            kernel_candidates = []
            
            while int(i_k) <= int(list_param[1][1]):
                
                if int(i_k) <= int(height):
                    kernel_candidates.append(int(i_k))
                print('kernel_candidates'); print(kernel_candidates)
                i_k += 1
            print 'abs(len(kernel_candidates))'
            print abs(len(kernel_candidates))
            rand_kernel = random.randrange(0,abs(len(kernel_candidates)),1)
            print('rand_kernel'); print(rand_kernel)
            return(int(kernel_candidates[rand_kernel]))
            
            
            
    def get_rand_stride(height,width,kernel,list_param): # Cria varios possiveis strides
        import random
        if (int(height) == int(width)): # Imagens quadradas!
            
            i_s = int(list_param[2][0])
            stride_candidates = []
            
            while int(i_s) <= int(list_param[2][1]):
                
                if ((int(height)-int(kernel)) % i_s == 0):
                    stride_candidates.append(int(i_s))
                i_s += 1
                
            print abs(len(stride_candidates))
            rand_stride = random.randrange(0,abs(len(stride_candidates)),1)
            return(int(stride_candidates[rand_stride]))
    
    
    
    def next_dimensions(height,width,kernel,stride):
        """
         This function defines the dimensions of an image that
        is the product of either a CONV layer or a POOL layer.
        """
        if (int(height) == int(width)):  # Imagens quadradas!
            next_dim = (((int(height)-int(kernel))/(int(stride))) + 1)
            return int(next_dim)


    
    
    """
    Assining all hyperparameters in it's respective gene position
    (with a random selection) 
    """
    if (int(img_height) == int(img_width)):  # Imagens quadradas!
        
        generation = []
        for k in range(population_size):        # Ao longo de todos os n genes da populacao
            gene1 = [0,0,0,0,0,0,0,0,0,0,0]
        
            # --------------------- CONV LAYER 1 ------------------------------------------
#            gene1.append(int(random.randint(low_num_filters_conv1,high_num_filters_conv1)))
            gene1[0] = int(random.randint(low_num_filters_conv1,high_num_filters_conv1))
            
#            kernel_c1 = get_rand_kernel(img_height, img_width, list_param)
#            gene1.append(kernel_c1)
            gene1[1] = get_rand_kernel(img_height, img_width, list_param)
            
#            stride_c1 = get_rand_stride(img_height, img_width, kernel_c1, list_param)
#            gene1.append(stride_c1)
            gene1[2] = get_rand_stride(img_height, img_width, gene1[1], list_param)
            
#            conv1_height = next_dimensions(img_height, img_width, kernel_c1, stride_c1)
            conv1_height = next_dimensions(img_height, img_width, gene1[1], gene1[2])
            print('CONV 1 dimensions:  (' + str(conv1_height) + ',' + str(conv1_height) + ')')
            # -----------------------------------------------------------------------------
            
            
            
            # --------------------- POOL LAYER 1 ------------------------------------------
#            kernel_p1 = get_rand_kernel(conv1_height, conv1_height, list_param)
#            gene1.append(kernel_p1)
            gene1[3] = get_rand_kernel(conv1_height, conv1_height, list_param)
            
#            stride_p1 = get_rand_stride(conv1_height, conv1_height, kernel_p1, list_param)
#            gene1.append(stride_p1)
            gene1[4] = get_rand_stride(conv1_height, conv1_height, gene1[3], list_param)
            
#            pool1_height = next_dimensions(conv1_height, conv1_height, kernel_p1, stride_p1)
            pool1_height = next_dimensions(conv1_height, conv1_height, gene1[3], gene1[4])

            print('POOL 1 dimensions:  (' + str(pool1_height) + ',' + str(pool1_height) + ')')
            # -----------------------------------------------------------------------------
            
            
            
            # --------------------- CONV LAYER 2 ------------------------------------------
#            gene1.append(int(random.randint(low_num_filters_conv2,high_num_filters_conv2)))
            gene1[5] = int(random.randint(low_num_filters_conv2,high_num_filters_conv2))
            print 'gene1[5] -> num_filters_conv2'
            print gene1[5]
#            kernel_c2 = get_rand_kernel(pool1_height, pool1_height, list_param)
#            gene1.append(kernel_c2)
            gene1[6] = get_rand_kernel(pool1_height, pool1_height, list_param)
            print 'gene1[6] -> kernel_conv2'
            print gene1[6]
            
#            stride_c2 = get_rand_stride(pool1_height, pool1_height, kernel_c2, list_param)
#            gene1.append(stride_c2)
            gene1[7] = get_rand_stride(pool1_height, pool1_height, gene1[6], list_param)
            print 'gene1[7] -> stride'
            print gene1[7]
            
#            conv2_height = next_dimensions(pool1_height, pool1_height, kernel_c2, stride_c2)
            conv2_height = next_dimensions(pool1_height, pool1_height, gene1[6], gene1[7])
            print('CONV 2 dimensions:  (' + str(conv2_height) + ',' + str(conv2_height) + ')')
            # -----------------------------------------------------------------------------
            
            
            
            # --------------------- POOL LAYER 2 ------------------------------------------
#            kernel_p2 = get_rand_kernel(conv2_height, conv2_height, list_param)
#            gene1.append(kernel_p2)
            gene1[8] = get_rand_kernel(conv2_height, conv2_height, list_param)
            
#            stride_p2 = get_rand_stride(conv2_height, conv2_height, kernel_p2, list_param)
#            gene1.append(stride_p2)
            gene1[9] = get_rand_stride(conv2_height, conv2_height, gene1[8], list_param)
            
#            pool2_height = next_dimensions(conv2_height, conv2_height, kernel_p2, stride_p2)
            pool2_height = next_dimensions(conv2_height, conv2_height, gene1[8], gene1[9])
            print('POOL 2 dimensions:  (' + str(pool2_height) + ',' + str(pool2_height) + ')')
            # -----------------------------------------------------------------------------
            
            
        
            # ------------------- FULLY CONECTED LAYER ------------------------------------
#            gene1.append(int(random.randint(low_num_full,high_num_full)))
            gene1[10] = int(random.randint(low_num_full,high_num_full))
            # -----------------------------------------------------------------------------
            
            
            

            gene = np.array(gene1)      #       Uncomment this if you want each gene to be a numpy array
            generation.append(gene)     #       Uncomment this if you want each gene to be a numpy array
            
#            generation.append(gene1)    #       Uncomment this if you want each gene to be a list
        
        
        return generation 
    

 

        
    
def mating_pool(pop, fitness, num_best, num_random):  
    """
    pop         - Geração inicial (numpy array com population_size linhas e Num_param colunas)
    fitness     - Accuracy (numpy array: population_size linhas e 1 coluna)
    perc_best   - número de genes "bons" escolhidos     [0.0 - 1.0[
    perc_random - número máximo de genes random  escolhidos[0.0 - 1.0[     
    """
#    Defined by percentages:
#    num_best_parents = int(perc_best*len(pop))
#    max_num_random_parents = int(perc_random*len(pop))
    
#    Defined by numbers:
    num_best_parents = int(num_best)
    max_num_random_parents = int(num_random)
    
    chosen_parents1 = []
    new_parent = 0
  
    copied_pop = pop
    copied_fitness = fitness
    
    for parent_num in range(num_best_parents):

        i = np.where(copied_fitness == np.max(copied_fitness))  # Output: (array([...]),)
        ind = int(i[0][0])                                      # ... (as a number)

        new_parent = copied_pop[ind]
        chosen_parents1.append(new_parent)       
        
        # Creating a new population and fitness lists, each with 1 element shorter
        # I came up with this because np.array does not allow simply removing 1 element.
        new_copied_pop = []
        new_copied_fitness = []
        
        for index in range(int(len(copied_pop))):
            if int(index) != int(ind):
                new_copied_pop.append(copied_pop[int(index)])
                new_copied_fitness.append(copied_fitness[int(index)])
                
        copied_pop = new_copied_pop
        copied_fitness = new_copied_fitness


    """ Escolha aleatória dos restantes ("bad")     [lista pop]
    """
    
    for bad_parents in range(max_num_random_parents):
        """
        1. Escolher aleatóriamente um elemento de copied_pop (já sem os pais)
        2. Decidir, aleatóriamente, se é adicionado ou não
        """
        rand_index = int(random.randrange(0,abs(int(len(copied_pop))),1)) # -1 por causa do índice!
        rand_num1 = random.random()
        rand_num2 = random.random()
        
        if rand_num1 > rand_num2:
            chosen_parents1.append(copied_pop[rand_index])

    return chosen_parents1



def crossover(parents,length_pop):
    
    copied_parents = parents
    crossed_parents1 = []


    children_num = int(int(length_pop)-int(len(copied_parents)))
    print children_num
    max_new_children = int((children_num + 1)/2)
    print max_new_children
    new_children = []
    
    
    # Crossver
    for cross in range(max_new_children):
        
        print('creating_children_iteration' + str(cross))
        
        child1 = []
        child2 = []

        rand1 = random.randrange(0,abs(len(copied_parents)),1) # -1 por causa do índice!
        rand2 = random.randrange(0,abs(len(copied_parents)),1) # -1 por causa do índice! 
        while rand1 == rand2: # Para impedir que os nºs sejam iguais.
            rand1 = random.randrange(0,abs(len(copied_parents)),1) # -1 por causa do índice!
            rand2 = random.randrange(0,abs(len(copied_parents)),1) # -1 por causa do índice!

        mother = copied_parents[int(rand1)]
        father = copied_parents[int(rand2)]
            
        mother_array = np.array(mother)
        father_array = np.array(father)
                        
        # 2.2
        crossing_point = int(random.randrange(0, abs(int(len(mother))), 1))        
        mother = np.hsplit(mother_array, [crossing_point])
        father = np.hsplit(father_array, [crossing_point])            
            
        # 2.3
        child1 = np.append(mother[0],father[1])
        print child1
        new_children.append(child1)
        
        child2 = np.append(father[0],mother[1])
        print child2
        new_children.append(child2)
    
    print 'new_children'
    print new_children    
    
    for ind in range(len(copied_parents)):
        crossed_parents1.append(copied_parents[ind])
    
    
    for put in range(len(new_children)):
        
        print('putting new_children elements in crossed_over1')
        print put
        
#        if (len(crossed_over1) < int(length_pop)):
#            crossed_over1.append(new_children[int(put)])
#            print crossed_over1
            
        if (len(crossed_parents1) < int(length_pop)):
            crossed_parents1.append(new_children[put])
    return crossed_parents1

#def crossover(parents,pop):
#    
##    parents ----> INALTERADO
#    parents1 = parents
#    
#    """
#    1. Crio uma lista vazia, à qual irei adicionar os novos genes (filhos)
#    2. Ciclo for em que para cada iteração:
#        2.1 - Pego em 2 genes da lista parents, aleatóriamente
#        2.2 - Separo ambos em 2 np.array's
#              (o crossing-over point é aleatório e o mesmo para os 2)
#        2.3 - Crossing over (só com 1 ponto)
#        2.4 - Adiciono-os a new_generation
#    NOTA:
#        Caso parents tenha um nº ímpar de elementos, no final do ciclo retiro 
#        aleatóriamente um elemento
#    """
#    crossed_over1 = []
#    remaining_children = int(int(len(pop))-int(len(parents)))
#    print 'remaining_children'
#    print remaining_children
##    print("Remaining children: " + str(remaining_children))
#    
#    if (int(len(parents)) % 2 == 0):
##        print("par")
#        """  O vetor parents tem um Nº PAR de elementos  """
#        
#        for counter in range(int((remaining_children/2))):
#            print 'len(parents1)'
#            print(int(len(parents1)))
#            child1 = []
#            child2 = []
#            
#            # 2.1
#            rand1 = random.randrange(0,abs(len(parents1)),1) # -1 por causa do índice!
#            rand2 = random.randrange(0,abs(len(parents1)),1) # -1 por causa do índice! 
#            while rand1 == rand2: # Para impedir que os nºs sejam iguais.
#                rand1 = random.randrange(0,abs(len(parents1)),1) # -1 por causa do índice!
#                rand2 = random.randrange(0,abs(len(parents1)),1) # -1 por causa do índice!
#                
#            mother = parents1[int(rand1)]
#            father = parents1[int(rand2)]
#            
#            mother_array = np.array(mother)
#            father_array = np.array(father)
#                        
#            # 2.2
#            crossing_point = int(random.randrange(0, int(len(mother))))        
#            mother = np.hsplit(mother_array, [crossing_point])
#            father = np.hsplit(father_array, [crossing_point])            
#            
#            # 2.3
#            child1 = np.append(mother[0],father[1])
#            child2 = np.append(father[0],mother[1])
#
#            # 2.4
#            crossed_over1.append(child1)
#            crossed_over1.append(child2)
#            
##            print("Length of crossed_over1 " + str(len(crossed_over1)))
#            
#            if counter == int((remaining_children/2)-1):
#                
##                print("Got to last element") 
#                
#                for index1 in range(len(parents1)):
#                    crossed_over1.append(parents1[int(index1)])
##                    print(len(crossed_over1))
#                
#                return crossed_over1
#
#            
#            
#                
#    else:
##        print("ímpar")
#        """ O vetor parents tem um Nº ÍMPAR de elementos """
#        
#        for counter in range(int((remaining_children/2)+1)):
#            print 'len(parents1)'
#            print(int(len(parents1)))
#            child1 = []
#            child2 = []
#            
#            # 2.1
#            rand1 = random.randrange(0,abs(len(parents1)),1) # -1 por causa do índice!
#            rand2 = random.randrange(0,abs(len(parents1)),1) # -1 por causa do índice! 
#            while rand1 == rand2: # Para impedir que os nºs sejam iguais.
#                rand1 = random.randrange(0,abs(len(parents1)),1) # -1 por causa do índice!
#                rand2 = random.randrange(0,abs(len(parents1)),1) # -1 por causa do índice!           
#                
#            mother = parents1[int(rand1)]
#            father = parents1[int(rand2)]
#            
#            mother_array = np.array(mother)
#            father_array = np.array(father)
#            
#            # 2.2
#            crossing_point = int(random.randrange(0, int(len(mother))))
#            mother = np.hsplit(mother_array, [crossing_point])
#            father = np.hsplit(father_array, [crossing_point])
#            
#            # 2.3
#            child1 = np.append(mother[0],father[1])
#            child2 = np.append(father[0],mother[1])
#
#            # 2.4
#            crossed_over1.append(child1)
#            crossed_over1.append(child2)
#        
#            if counter == int(remaining_children/2): # Removing the last element made.
##                print("Got to last element")
##                random_index = int(random.randrange(0, int(len(crossed_over1)))) # -1 por causa do índice!
#                copied_crossed_over1 = []
#                
#                for index in range(len(crossed_over1)):
#                    if index != int(len(crossed_over1)):
#                        copied_crossed_over1.append(crossed_over1[int(index)])
#
#                crossed_over1 = copied_crossed_over1
#                
#                for index1 in range(len(parents1)):
#                    crossed_over1.append(parents1[int(index1)])
##                    print(len(crossed_over1))
#
#                return crossed_over1
#                


def mutation(pop, mutated_genes, genome_mutated, list_param, img_height, img_width):
    
#        Remember!
#        list_param = [[10,200], [2,3], [1,2], [10,200], [50,200]]
#"""                      0        1      2       3         4      """
    
    # Independent hyperparameters
    low_num_filters_conv = list_param[0][0]    #    Number of filters (range)
    high_num_filters_conv = list_param[0][1]
    low_num_full = list_param[4][0]
    high_num_full = list_param[4][1]
    
    # Dependent hyperparameters
    def get_rand_kernel(height,width,list_param): # Cria varios kernels possiveis, com base no tamanho da imagem 
        import random
        if (int(height) == int(width)):  # Imagens quadradas!
            
            i_k = int(list_param[1][0])
            print('i_k'); print(i_k)
            kernel_candidates = []
            
            while int(i_k) <= int(list_param[1][1]):
                
                if int(i_k) <= int(height):
                    kernel_candidates.append(int(i_k))
                print('kernel_candidates'); print(kernel_candidates)
                i_k += 1
            print 'abs(len(kernel_candidates))'
            print abs(len(kernel_candidates))
            rand_kernel = random.randrange(0,abs(len(kernel_candidates)),1)
            print('rand_kernel'); print(rand_kernel)
            return(int(kernel_candidates[rand_kernel]))
            
    def get_rand_stride(height,width,kernel,list_param): # Cria varios possiveis strides
        import random
        if (int(height) == int(width)): # Imagens quadradas!
            
            i_s = int(list_param[2][0])
            stride_candidates = []
            
            while int(i_s) <= int(list_param[2][1]):
                
                if ((int(height)-int(kernel)) % i_s == 0):
                    stride_candidates.append(int(i_s))
                i_s += 1
                
            print abs(len(stride_candidates))
            rand_stride = random.randrange(0,abs(len(stride_candidates)),1)
            return(int(stride_candidates[rand_stride]))

    def next_dimensions(height,width,kernel,stride):
        """
         This function defines the dimensions of an image that
        is the product of either a CONV layer or a POOL layer.
        """
        if (int(height) == int(width)):  # Imagens quadradas!
            next_dim = (((int(height)-int(kernel))/(int(stride))) + 1)
            return int(next_dim)
    """
      Now, the function creates a new list of genes taking into consideration 
    how many it should mutate.
    """
    
    mutation_genes = int(mutated_genes)
    gene_part_mutated = int(genome_mutated) # Assuming that all gene lenghts are the same!
    
    copied_pop = pop
    offspring1 = []
    
    
    """
        Creating a list of indexes that will be used in the mutation.
        The corresponding genes inside the population will suffer mutation(s)
    """
    rand_gene_history = []
    for idx in range(mutation_genes):
        
        rand_gene = int(random.randrange(0,int(len(copied_pop)),1))
        
        # Checking if random number was chosen before:
        check_rand_gene = rand_gene in rand_gene_history
        
        while check_rand_gene == True:                       # This idx was already chosen
            rand_gene = int(random.randrange(0,int(len(copied_pop)),1))
            check_rand_gene = rand_gene in rand_gene_history
                
        rand_gene_history.append(rand_gene)
    
    """
        Creating a new list of arrays, where the indexes chosen before will
    trigger the mutation for the corresponding gene.
    
        The remaining genes will remain untouched.
    """
        
    for idx0 in range(len(copied_pop)):
        
        gene = copied_pop[idx0]
        check_mut_gene = idx0 in rand_gene_history
        
        if (check_mut_gene == True):

            rand_gene_part_history = []
            for idx1 in range(gene_part_mutated):
                
                if (int(img_height) == int(img_width)):  # Imagens quadradas!
                
                    # Random element of chosen gene
                    rand_element = int(random.randrange(0,abs(len(copied_pop[0])),1)) # Assuming that all genes have the same dimensions!
                    # Checking if this idx was chosen before
                    check_part = rand_element in rand_gene_part_history
                    while check_part == True:
                        rand_element = int(random.randrange(0,len(copied_pop[0])))
                        check_part = rand_element in rand_gene_part_history
                        # When this idx is a new one:
                    rand_gene_part_history.append(rand_element)
                    
                    
                    kernel_c1 = get_rand_kernel(img_height, img_width, list_param)
                    stride_c1 = get_rand_stride(img_height, img_width, kernel_c1, list_param)
                    conv1_height = next_dimensions(img_height, img_width, kernel_c1, stride_c1)
                    
                    
                    kernel_p1 = get_rand_kernel(conv1_height, conv1_height, list_param)
                    stride_p1 = get_rand_stride(conv1_height, conv1_height, kernel_p1, list_param)
                    pool1_height = next_dimensions(conv1_height, conv1_height, kernel_p1, stride_p1)
                    
                    
                    kernel_c2 = get_rand_kernel(pool1_height, pool1_height, list_param)
                    stride_c2 = get_rand_stride(pool1_height, pool1_height, kernel_c2, list_param)
                    conv2_height = next_dimensions(pool1_height, pool1_height, kernel_c2, stride_c2)
                    
                    
                    kernel_p2 = get_rand_kernel(conv2_height, conv2_height, list_param)
                    stride_p2 = get_rand_stride(conv2_height, conv2_height, kernel_p2, list_param)
                    
                    
                
                    if any ( [rand_element == 0, rand_element == 5] ):
                        # Number of filters for CONV 1 or 2
                        gene[rand_element] = int(random.randint(low_num_filters_conv,high_num_filters_conv))
        
                    elif (rand_element == 10):
                        # Number of Fully Conected Layers
                        gene[rand_element] = int(random.randint(low_num_full,high_num_full))
                    
                    elif (rand_element == 1):
                        # Kernel size for CONV 1
                        gene[rand_element] = kernel_c1
                        
                    elif (rand_element == 2):
                        # Stride for CONV 1
                        gene[rand_element] = stride_c1
                        
                    elif (rand_element == 3):
                        # Kernel size for POOL 1
                        gene[rand_element] = kernel_p1
                        
                    elif (rand_element == 4):
                        # Stride for POOL 1
                        gene[rand_element] = stride_p1
                        
                    elif (rand_element == 6):
                        # Kernel size for CONV 2
                        gene[rand_element] = kernel_c2
                        
                    elif (rand_element == 7):
                        # Stride for CONV 2
                        gene[rand_element] = stride_c2
                        
                    elif (rand_element == 8):
                        # Kernel size for POOL 2
                        gene[rand_element] = kernel_p2
                    
                    elif (rand_element == 9):
                        # Stride for POOL 2
                        gene[rand_element] = stride_p2
                        
        offspring1.append(gene)  
        
    return pop


















#def mutation(pop, mutated_genes, genome_mutated, list_param):
#    
#    copied_pop = pop
#    offspring1 = []
#    
#    for element in range(len(copied_pop)):
#        offspring1.append(copied_pop[element])
#    
#    
#    
##    print ' ############################### '
##    print 'Inicial population'
#    
#    #list_param = [[10,200], [2,3], [1,2], [10,200], [50,200]]
##"""                  0        1      2       3         4      """
#
#    low_num_filters_conv = list_param[0][0]    #    Number of filters (range)
#    high_num_filters_conv = list_param[0][1]
#
#    low_kernel_size_conv = list_param[1][0]    #    Kernel size (range):
#    high_kernel_size_conv = list_param[1][1]
#
#    low_stride_conv = list_param[2][0]         #    Stride (range):
#    high_stride_conv = list_param[2][1]
#
##    low_pool1 = list_param[3][0]
##    high_pool1 = list_param[3][1]
#
##    low_num_filters_conv2 = list_param[3][0]    #    Number of filters (range)
##    high_num_filters_conv2 = list_param[3][1]
#
#
#    low_num_full = list_param[4][0]
#    high_num_full = list_param[4][1]
#
#
#
##    mutation_genes = int(p1*len(offspring1))
#    mutation_genes = int(mutated_genes)
#    gene_part_mutated = int(genome_mutated)                 # Assuming that all gene lenghts are the same!
#
#    rand_gene_history = []
#    
#    for idx0 in range(mutation_genes):
#
#        # Random gene inside population
#        rand_gene = random.randrange(0,int(len(offspring1)),1)
#        
#        # Checking if random number was chosen before:
#        check_gene = int(rand_gene) in rand_gene_history
#        
#        while check_gene == True:                       # This idx was already chosen
#            rand_gene = random.randrange(0,int(len(offspring1)),1)
#            check_gene = int(rand_gene) in rand_gene_history
#            
#        # When the idx generated is a new one
#        
#        rand_gene_history.append(rand_gene)
##        print 'random gene chosen '
##        print rand_gene
##        print ' ----------------------------- '
#        
#        rand_gene_part_history = []
#        for idx1 in range(gene_part_mutated):
#            
#            # Random element of chosen gene
#            rand_element = int(random.randrange(0,abs(len(offspring1[0])),1))
#            
#            # Checking if this idx was chosen before
#            check_part = rand_element in rand_gene_part_history
#            
#            while check_part == True:
#                rand_element = int(random.randrange(0,len(offspring1[0])))
#                check_part = rand_element in rand_gene_part_history
#                
#            # When this idx is a new one:
#            rand_gene_part_history.append(rand_element)
##            print 'random element chosen'
##            print rand_element
##            print 'random element history:'
##            print rand_gene_part_history
#            """
#            Mutação à parte do gene em questão, mas que depende do parametro
#            """
#            if any ( [rand_element == 0, rand_element == 5] ):
#                # Number of filters for CONV 1 or 2
#                offspring1[rand_gene][rand_element] = int(random.randint(low_num_filters_conv,high_num_filters_conv))
#                
#            elif any ( [[rand_element == 1, rand_element == 3, rand_element == 6, rand_element == 8]] ):
#                # Kernel size for CONV 1/2 or POOL 1/2
#                offspring1[rand_gene][rand_element] = int(random.randint(low_kernel_size_conv,high_kernel_size_conv))
#                
#            elif any ( [rand_element == 2, rand_element == 4, rand_element == 7, rand_element == 9] ):
#                # Stride for CONV 1/2 or POOL 1/2
#                offspring1[rand_gene][rand_element] = int(random.randint(low_stride_conv,high_stride_conv))
#        
#            else:
#                # Number of Fully Conected Layers
#                offspring1[rand_gene][rand_element] = int(random.randint(low_num_full,high_num_full))
#                
#    return offspring1




