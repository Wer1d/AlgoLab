import time
def BruteForce(text_string,k):
    print("Start BruteForcing......")
    example = list(text_string)

    G_index_with_range = []
    for i in range(len(example)):
        if example[i] == "G":
            for j in range(len(example)):
                if example[j] == "P":
                    G_index_with_range.append((i,j,abs(i-j))) #(ตำแหน่งของG,ตำแหน่งของP,ระยะห่าง)

    print("Brute Force Calculating all posiibillity...")
    for i in range(len(G_index_with_range)):
        print("Grab car at position : "+str(G_index_with_range[i][0]),"Passenger at position : "+str(G_index_with_range[i][1]),"distance : "+str(G_index_with_range[i][2]))

    filterwithk = []
    for i in range(len(G_index_with_range)):
        if G_index_with_range[i][2] <= k:
            filterwithk.append(G_index_with_range[i])


    print("Distance filtering process at k =",k,"......")
    for i in range(len(filterwithk)):
        print("Grab car at position : "+str(filterwithk[i][0]),"Passenger at position : "+str(filterwithk[i][1]),"distance : "+str(filterwithk[i][2]))
    print("result =",len(filterwithk))

    output_G = []
    output_P = []
    for i in range(len(filterwithk)):
        if filterwithk[i][0] not in output_G and filterwithk[i][1] not in output_P:
            output_G.append(filterwithk[i][0])
            output_P.append(filterwithk[i][1])

    print("BruteForce_Output :",len(output_G))

def Greedy(text_string,k):
    print("Start Greedying......")
    example = list(text_string)
    
    filtered = []
    for i in range(len(example)):
        if(i<len(example)):    
            if i not in filtered:
                if example[i]=="P":
                    counter=0
                    for j in range(i+1,len(example)):
                        counter+=1
                        if counter > k:
                            break
                        if j not in filtered :
                            if example[j]=="G":
                                filtered.append(j)
                                print("Found G at index:",j,",Pick a P at",i)
                                break
                if example[i]=="G":
                    counter=0
                    for j in range(i+1,len(example)):
                        counter+=1
                        if counter > k:
                            break
                        if j not in filtered :
                            if example[j]=="P":
                                filtered.append(j)
                                print("Found G at index:",i,",Pick a P at",j)
                                break
    print("Greedy_Output: ",len(filtered))

def Greedy_Start_Form_Fartest(text_string,k):
    print("Start Greedying From Fartest......")
    example = list(text_string)
    
    filtered = []
    for i in range(len(example)):
        if(i<len(example)):    
            if i not in filtered:
                if example[i]=="P":
                    counter=0
                    for j in range(i+k,i,-1):
                        if j < len(example):
                            counter+=1
                            if counter > k:
                                break
                            if j not in filtered :
                                if example[j]=="G":
                                    filtered.append(j)
                                    print("Found G at index:",j,",Pick a P at",i)
                                    break
                if example[i]=="G":
                    counter=0
                    for j in range(i+k,i,-1):
                        if j < len(example):
                            counter+=1
                            if counter > k:
                                break
                            if j not in filtered :
                                if example[j]=="P":
                                    filtered.append(j)
                                    print("Found G at index:",i,",Pick a P at",j)
                                    break
    print("Greedy_from_fartest_Output: ",len(filtered))


qtext = "GPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPPPPPPPPPPPPPPPPPPPPPPPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPPPPPPPPPPPPPPPPPPPPPPPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGPGP"
inpk = 2
start_time1 = time.perf_counter()
BruteForce(qtext,inpk)
end_time1 = time.perf_counter()

start_time2 = time.perf_counter()
Greedy(qtext,inpk)
end_time2 = time.perf_counter()

start_time3 = time.perf_counter()
Greedy_Start_Form_Fartest(qtext,inpk)
end_time3 = time.perf_counter()

print("time taken for BruteForce =",(end_time1-start_time1)*1000,"milliseconds")
print("time taken for Greedy =",(end_time2-start_time2)*1000,"milliseconds")
print("time taken for Greedy From Fartest =",(end_time3-start_time3)*1000,"milliseconds")