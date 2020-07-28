def cal_points(player):#defined function
    point=0
    if player["role"]=="Bat": # codition works if player is a batsman.

        point=(player["runs"]//2)*1

        #comaring runs
        if player["runs"]>=50:
            point=point+5
            if player["runs"]>=100:
                point=point+10

        #calculating strike rate.
        strike_rate = (player["runs"] / player["balls"]) * 100

        #comparing strike rate.
        if strike_rate >= 80 and strike_rate <= 100:
            point = point+2
        elif strike_rate > 100:
            point = point+4

        #calculating sises and fours.
        point = point+player["6"] * 2
        point = point+player["4"] * 1

        #printing output
        print({"name":player["name"],"Batscore":point})

#Bowler section
    if player["role"] == "Bowl":# condition works if player is bowler

        if player["wkts"] >= 0:#condition

            point = point + player["wkts"] * 10

            #sub condition
            if player["wkts"] >= 3:
                point = point + 5
                if player["wkts"] >= 5:
                    point = point + 10

                #calculating economy record.
                eco_rate = player["runs"] / player["overs"]

        #codition of economy rate.
                if eco_rate >= 3.5 and eco_rate <= 4.5:
                    point = point + 4

                elif eco_rate < 3.5:
                    point = point + 7

                elif eco_rate < 2:
                    point = point + 10

                print({"name": player["name"], "Bowlscore": point})
            else:
                eco_rate = player["runs"] / player["overs"]#calculating economy rate
                if eco_rate >= 3.5 and eco_rate <= 4.5:
                    point = point + 4

                elif eco_rate < 3.5:
                    point = point + 7

                elif eco_rate < 2:
                    point = point + 10

                #printing output
                print({"name": player["name"], "Bowlscore": point})
