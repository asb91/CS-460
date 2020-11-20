import os
import parser
import geometry

def database(dirs,path):

    # ITERATING OVER FILES 

    database_ = []

    for file in dirs:
        
        files = []
        dfNH=[]
        dfSEG=[]

        # PARSING DATA FILES
        
        data = parser.parse_data(os.path.join(path,file))
        files.append(file)
        
        for i in range(len(data)):
            if data[i][0] == 'N':
                res_id = data[i][2]
                for j in range(len(data)):
                    if data[j][0] == 'H' and data[j][2] == res_id : 
                        dfNH.append(data[j] + data[i]) 
                        break
                        
        for j in range(len(data)):
            if data[j][0] == 'SD': 
                dfSEG.append(files+data[j])

        # REMOVING IRRELEVANT DATA ENTRIES

        for i in range(len(dfSEG)):
            for j in range(len(dfNH)):
                dist= geometry.distance(dfSEG[i][4],dfSEG[i][5],dfSEG[i][6],dfNH[j][3],dfNH[j][4],dfNH[j][5])
                if dist < 4.2: 
                    database_.append(dfSEG[i]+dfNH[j])


    fve = f_vector(database_,1)
    rv = [database_,fve]
    return rv
            

def f_vector(database,choice):
    
    # CONSTRUCTING FEATURE VECTORS 

    if choice == 0:
    
        vector = []

        for i in range(len(database)):
        
            temp = []

            dist_d = geometry.distance(database[i][10],database[i][11],database[i][12],database[i][16],database[i][17],database[i][18])
            temp.append(dist_d)
            dist_D = geometry.distance(database[i][4],database[i][5],database[i][6],database[i][16],database[i][17],database[i][18])
            temp.append(dist_D)
            ang_th = geometry.angle(database[i][4]-database[i][10],database[i][5]-database[i][11],database[i][6]-database[i][12],database[i][16]-database[i][10],database[i][17]-database[i][11],database[i][18]-database[i][12])
            temp.append(ang_th) 
            
            if database[i][19] == 'YES':
                temp.append('YES')
                vector.append(temp)                    

            elif database[i][19] == 'NO':
                temp.append('NO')
                vector.append(temp)
            
        return vector     

    elif choice == 1:

        vector = []

        for i in range(len(database)):
            
            temp = []

            dist_d = geometry.distance(database[i][10],database[i][11],database[i][12],database[i][16],database[i][17],database[i][18])
            temp.append(dist_d)
            dist_D = geometry.distance(database[i][4],database[i][5],database[i][6],database[i][16],database[i][17],database[i][18])
            temp.append(dist_D)
            ang_th = geometry.angle(database[i][4]-database[i][10],database[i][5]-database[i][11],database[i][6]-database[i][12],database[i][16]-database[i][10],database[i][17]-database[i][11],database[i][18]-database[i][12])
            temp.append(ang_th)
            vector.append(temp)                   
             
        return vector
