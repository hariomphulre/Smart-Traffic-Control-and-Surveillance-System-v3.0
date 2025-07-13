import json
import time
import sys

FILE_PATH = "/home/pi/Desktop/Smart-Traffic-Control-and-Surveillance-System-v3.0/traffic_signal_simulation/traffic2.json"

# Load existing dictionary (if available)
def load_data():
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Default to empty dict if file doesn't exist or is corrupted

# Save dictionary to file
def save_data(data):
    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

traffic = load_data()

try:
    def start():
        traffic = load_data()
        traffic['R1'] = True
        traffic['R2'] = True
        traffic['R3'] = True
        traffic['R4'] = True

        traffic['G1'] = False
        traffic['G2'] = False
        traffic['G3'] = False
        traffic['G4'] = False

        traffic['Y1'] = False
        traffic['Y2'] = False
        traffic['Y3'] = False
        traffic['Y4'] = False

        save_data(traffic)

        def find_max():
            traffic = load_data()
            traffic_list = [traffic["T1"], traffic["T2"], traffic["T3"], traffic["T4"]]

            tmax1=0,tmax2=0,tmax3=0,tmax4=0
            tmax1lan=0,tmax2lan=0,tmax3lan=0,tmax4lan=0
            ############ new update #################
            for i in range(4):
                if(traffic_list[i]>=tmax1):
                    tmax4=tmax3
                    tmax3=tmax2
                    tmax2=tmax1
                    tmax1=traffic_list[i]
                    tmax4lan=tmax3lan
                    tmax3lan=tmax2lan
                    tmax2lan=tmax1lan
                    tmax1lan=i+1
                else if(traffic_list[i]>=tmax2):
                    tmax4=tmax3
                    tmax3=tmax2
                    tmax2=traffic_list[i]
                    tmax4lan=tmax3lan
                    tmax3lan=tmax2lan
                    tmax2lan=i+1
                else if(traffic_list[i]>=tmax3):
                    tmax4=tmax3
                    tmax3=traffic_list[i]
                    tmax4lan=tmax3lan
                    tmax3lan=i+1
                else:
                    tmax4=traffic_list[i]
                    tmax4lan=i+1
            #############################################

            # tmax = max(traffic_list)
            # tmaxlan = traffic_list.index(tmax) + 1
            # traffic_list.pop(tmaxlan - 1)
            # tmaxlan2 = (traffic_list.index(max(traffic_list))) + 1
            # if (tmaxlan2 >= tmaxlan):
                # tmaxlan2 += 1

            # if (tmax == 0):
            #     return [tmaxlan, 0, tmaxlan2, True]
            # elif (tmax <= 3):
            #     return [tmaxlan, 5, tmaxlan2, False]
            # elif (tmax <= 5):
            #     return [tmaxlan, 10, tmaxlan2, False]
            # elif (tmax <= 7):
            #     return [tmaxlan, 15, tmaxlan2, False]
            # return [tmaxlan, 20, tmaxlan2, False]


            ################ new update ##################
            c1=0,c2=0,c3=0,c4=0
            if(tmax1>0 and tmax1<=3):
                c1=5
            else if(tmax1>0 and tmax1<=5)
                c1=10
            else if(tmax1>0 and tmax1<=7)
                c1=15
            else if(tmax1>0 and tmax1<=10):
                c1=25
            else if(tmax1>0):
                c1=30
            
            c2=c1

            if(tmax3>0 and tmax3<=3):
                c3=5
            else if(tmax3>0 and tmax3<=5)
                c3=10
            else if(tmax3>0 and tmax3<=7)
                c3=15
            else if(tmax3>0 and tmax3<=10):
                c3=25
            else if(tmax3>0):
                c3=30

            if(tmax4>0 and tmax4<=3):
                c4=5
            else if(tmax4>0 and tmax4<=5)
                c4=10
            else if(tmax4>0 and tmax4<=7)
                c4=15
            else if(tmax4>0 and tmax4<=10):
                c4=25
            else if(tmax4>0):
                c4=30

            if(c3!=0):
                c3+=c2
            if(c4!=0):
                c4+=c3

            if (tmax1 == 0):
                # return [tmaxlan1, c1, tmaxlan2, c2, tmaxlan3, c3, tmaxlan4, c4, True]
                start()
            else:
                return [tmaxlan1, c1, tmaxlan2, c2, tmaxlan3, c3, tmaxlan4, c4, False]

        ###################### check any lane have traffic ##################
        def check():
            traffic = load_data()
            traffic['R1'] = True
            traffic['R2'] = True
            traffic['R3'] = True
            traffic['R4'] = True
            traffic['Y1'] = False
            traffic['Y2'] = False
            traffic['Y3'] = False
            traffic['Y4'] = False
            traffic['G1'] = False
            traffic['G2'] = False
            traffic['G3'] = False
            traffic['G4'] = False
            save_data(traffic)
            
            traffic = load_data()
            while (traffic["T1"] == 0 and traffic["T2"] == 0 and traffic["T3"] == 0 and traffic["T4"] == 0):
                time.sleep(1)
                traffic = load_data()
            return start()

        ##################### Ambulance ############################
        def emergency():
            traffic = load_data()
            lane = -1
            for i in range(4):
                if (traffic[f'A{(i + 1)}']):
                    lane = i + 1
                    break
            if (lane == -1): 
                return start()

            traffic['R1'] = True
            traffic['R2'] = True
            traffic['R3'] = True
            traffic['R4'] = True
            traffic['Y1'] = False
            traffic['Y2'] = False
            traffic['Y3'] = False
            traffic['Y4'] = False
            traffic['G1'] = False
            traffic['G2'] = False
            traffic['G3'] = False
            traffic['G4'] = False

            traffic[f'R{lane}'] = False
            traffic[f'G{lane}'] = True
            save_data(traffic)
            
            i = 20
            if (traffic[f'T{lane}'] <= 3):
                i = 5
            elif (traffic[f'T{lane}'] <= 5):
                i = 10
            elif (traffic[f'T{lane}'] <= 7):
                i = 15
                
            traffic = load_data()
            traffic["C"] = i
            save_data(traffic)
            
            while (i >= 0):
                print(f"Emergency Lane {lane}: {i}")
                traffic = load_data()
                traffic["C"] = i  # Update timer in JSON every second
                save_data(traffic)
                i -= 1
                time.sleep(1)
                
            traffic = load_data()
            if (traffic["A1"] or traffic["A2"] or traffic["A3"] or traffic["A4"]): 
                return emergency()
            return start()

        ##############################################################

        if (traffic["A1"] or traffic["A2"] or traffic["A3"] or traffic["A4"]): 
            return emergency()

        max_data = find_max()
        # if (max_data[3]):
        #     check()
            
        i = max_data[1] #max traffic countdown
        traffic = load_data()

        tmax1lane=max_data[0]
        tmax2lane=max_data[2]
        tmax3lane=max_data[4]
        tmax4lane=max_data[6]

        tmax1c=max_data[1]
        tmax2c=max_data[3]
        tmax3c=max_data[5]
        tmax4c=max_data[7]

        traffic[f"C{tmax1lane}"] = tmax1c
        traffic[f"C{tmax2lane}"] = tmax2c
        traffic[f"C{tmax3lane}"] = tmax3c
        traffic[f"C{tmax4lane}"] = tmax4c

        save_data(traffic)
        
        j = max_data[0] #max traffic lane

        max_traffics_cnt=[tmax1c,tmax2c,tmax3c,tmax4c]

        for(cntdwn in max_traffics_cnt):
            if(cntdwn==0):
                start()
            
            i=cntdwn
            while(i>=0):
                
        # j1 = 0
        # j2 = 0
        # i1 = 0
        # repeat = 0

        # traffic[f'R{j}'] = False
        # traffic[f'G{j}'] = True
        # save_data(traffic)
        
        # while (i >= 0):
        #     data = load_data()
        #     print(f"Lane {j}: {i}")
            
        #     # Update timer in JSON every second
        #     data["C"] = i
        #     save_data(data)
            
        #     if (data["A1"] or data["A2"] or data["A3"] or data["A4"]): 
        #         return emergency()

        #     if (i == 3):
        #         max_data = find_max()
        #         i1 = max_data[1]
        #         j1 = max_data[0]
        #         j2 = max_data[2]
        #         data[f'Y{j}'] = True
        #         data[f'G{j}'] = False
        #         if (repeat != 0 and j1 == repeat and j1 == j and j2 != 0):
        #             data[f'Y{(j2)}'] = True
        #             data[f'R{(j2)}'] = False
        #         else:
        #             data[f'Y{(j1)}'] = True
        #             data[f'R{(j1)}'] = False
        #         save_data(data)
                
        #     if (i == 0):
        #         max_data = find_max()
        #         if (max_data[3]):
        #             check()
                    
        #         if (repeat != 0 and j1 == repeat and j1 == j and j2 != 0):
        #             data[f'R{j}'] = True
        #             data[f'Y{j}'] = False
        #             j1 = j2
        #             j = j1
        #             data[f'G{j}'] = True
        #             data[f'Y{j}'] = False
        #         elif (repeat != j and j1 == j):
        #             data[f'Y{j}'] = False
        #             repeat = j
        #             data[f'G{j}'] = True
        #         else:
        #             data[f'R{j}'] = True
        #             data[f'Y{j}'] = False
        #             repeat = j
        #             j = j1
        #             data[f'G{j}'] = True
        #             data[f'Y{j}'] = False

        #         i = i1
        #         data["C"] = i
        #         save_data(data)
        #     else:
        #         i -= 1
        #     time.sleep(1)
        start()    
    start()
except KeyboardInterrupt:
    print("Simulation stopped")