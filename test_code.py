def read():
    f = open("job_data.csv",'r')
    dataArchAvg = 0
    c1 = 0 # counter for average
    srBusAvg = 0
    c2 = 0
    dataSciAvg = 0
    c3 = 0
    mlAvg = 0
    c4 = 0
    for line in f:
        column = line.split(',')
        if(column[2]=="Data Architect"):
            dataArchAvg += int(column[7])
            c1 += 1
        elif(column[2]=="Senior Business Analyst"):
            srBusAvg += int(column[7])
            c2 += 1
        elif(column[2]=="Data Scientist"):
            dataSciAvg += int(column[7])
            c3 += 1
        elif(column[2]=="Machine Learning Engineer"):
            mlAvg += int(column[7])
            c4 += 1
    
    dataArchAvg /= c1
    srBusAvg /= c2
    dataSciAvg /= c3
    mlAvg /= c4

    print("These are the average number of salaries for the following job titles: ")
    print("i. Data Architect: " + str(dataArchAvg))
    print("ii. Senior Business Analyst: " + str(srBusAvg))
    print("iii. Data Scientist: " + str(dataSciAvg))
    print("iv. Machine Learning Engineer: "+ str(mlAvg))
    f.close()


read()

