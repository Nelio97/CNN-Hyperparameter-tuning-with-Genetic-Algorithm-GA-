#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:19:39 2019
@author: njcandelaria

                        -----------------------------------
                                  MNIST DATABASE
                        -----------------------------------
        The following code is being used to save Training Images, Training Images,
    Testing Images and Testting Labels from MNIST Database into a direcotry I
    have created.

        The images on this database consist of handwritten digits (0-9) saved as 
    elements of a numpy array (28x28).
    
        For all images there's a correspondent label.
        I got the files at: http://yann.lecun.com/exdb/mnist/
        
        I am using this code to first test my Genetic Algorithm.


        On this code, I'm:
            
            1. Importing training images and labels from previously downoaded .gz files
            
            2. Saving all training images and labels in np.array's
            
            3. Saving them in a specific directory, as a PNG file

"""

def import_images_mnist(num_images):

    import idx2numpy
    import matplotlib.pyplot as plt
    import random
    
    print("With this code, you can have a database with up to 10.000 images")
    print("Based on MNIST database, testing images")
    print(' ... ')
    file_testing_images = '/home/FC/njcandelaria/caffemaster/Nelio/scripts/database_mnist_teste/t10k-images.idx3-ubyte'
    file_testing_labels = '/home/FC/njcandelaria/caffemaster/Nelio/scripts/database_mnist_teste/t10k-labels.idx1-ubyte'

    arr_test_img = idx2numpy.convert_from_file(file_testing_images)
    arr_test_lab = idx2numpy.convert_from_file(file_testing_labels)

    num_test_images = int(arr_test_img.shape[0]) 

    

    # Diretoria anterior
#    s = '/home/FC/njcandelaria/caffemaster/interface/mnist_database_images/img_'
#    s = '/home/FC/njcandelaria/caffemaster/interface/my_trained_nets_mnist_database/mnist_database_images_1000/img_'
    s = '/home/FC/njcandelaria/Documents/mnist_database/less/img_'
    # Diretoria atual
#    s = '/home/FC/njcandelaria/Documents/mnist_database_trained_nets/'
    rand_idx_history = []

    for index in range(num_images):
        
        # Random gene inside population
        # Random image chosen
        rand_idx = int(random.randrange(0,num_images))

        # Checking if random number was chosen before (making sure that ALL images are different)
        check_idx = rand_idx in rand_idx_history
            
        while check_idx == True:                       # This idx was already chosen
            rand_idx = int(random.randrange(0,num_images))
            check_idx = rand_idx in rand_idx_history
        
        rand_idx_history.append(rand_idx)
        
        image = arr_test_img[index]
        label = arr_test_lab[index]
        
        # ALTERAR CONDIÇÕES CONSOANTE O Nº IMAGENS A IMPORTAR
        
        if 0 <= index <= 8:
            fname = s + '00' + str(int(index)) + '_' + str(int(label)) + 'class' + '.png'
        elif 9 <= index <= 98:
            fname = s + '0' + str(int(index)) + '_' + str(int(label)) + 'class' + '.png'
        elif 99 <= index <= 999:
            fname = s + str(int(index)) + '_' + str(int(label)) + 'class' + '.png'

        plt.imsave(fname,arr=image)
    
    print(str(num_images) + ' succesfully imported from MNIST Database (Training)')
    
