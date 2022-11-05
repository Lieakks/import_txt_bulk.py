import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

os.getcwd()  # get current working directory
os.chdir('C:/Users/Daipei/Nutstore/1/Experiment_Data/muscle2/damping')  # change working directory
path = 'C:/Users/Daipei/Nutstore/1/Experiment_Data/muscle2/damping'  # set path
os.listdir(path)  # list files in the path

datalist = []  # create an empty list
for i in os.listdir(path):  # loop through all files in the path
    if i.endswith('.txt'):  # only import txt files
        datalist.append(i)  # append the file name to the list
datalist  # check the list

save_list = []  # create an empty list
df = pd.DataFrame()  # create an empty dataframe
t = 1
#name = []
#for t in range(1, len(datalist)):
#    name.append('muscle2_damping_' + str(t))

for txt in datalist:  # loop all files in the list
    name = 'muscle2_damping_' + str(t)
    data_path = os.path.join(path, txt)  # set the path for each file
    df_txt = pd.read_table(data_path, index_col= False)  # read the file
    df_txt = df_txt[['角度(°', ')转数(']].values  # convert the dataframe to array
    df_txt = np.c_[df_txt, np.zeros(len(df_txt))]  # add a column of zeros
    df_txt[:,2] = df_txt[:,1]*360 + df_txt[:,0]  # convert the angle to degree
#    plt.plot(df_txt[:,2])  # plot the data
#    plt.show()  # show the plot
    for i in range(1, len(df_txt)-1):
        if abs(df_txt[i,2]-df_txt[i-1,2]) >= 100 :
            # delete the data with large difference
            df_txt[i,2] = df_txt[i-1,2]
    plt.plot(df_txt[:,2])
    plt.show()
    exec ('muscle2_damping_' + str(t) + '=' + 'df_txt')  # create a variable for each file
    t += 1

for i in range(1, len(datalist)):
    np.savetxt('C:/Users/Daipei/Desktop/Test Data/artificial_muscle_2/Damping/muscle2_damping_' + str(i) + '.csv', eval('muscle2_damping_' + str(i)), delimiter = ',')

