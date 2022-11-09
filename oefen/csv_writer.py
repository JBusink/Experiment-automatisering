import os
import csv
import datetime, time

def save_csv(name,df,colnames):
    
    if os.path.isfile(f"{name}.csv") == True:
        print('File excists')
        return
    else:
        with open(f"{name}.csv",'w') as file:
            wr=csv.writer(file)
            Tbegin = time.time()
            seconds = time.time()
            local_time = time.ctime(seconds)

            wr.writerow([str(local_time),"Experiment LED arduino 33IoT"])
            wr.writerow(colnames)
            for i in range(len(data[0])):
                wr.writerow([round(time.time()-Tbegin,6), df[0][i],df[1][i]])
    return print("Files saved")

data = [[0,1,2,3,4],[0,2,4,6,8]]

colnames = ('time', 'col1','col2')
save_csv('test',data,colnames = colnames)
    