f=open("covid_19_india.csv","r")
covidlist={}
for lines in f:
    no,date,time,state,confirmed_i,confirmed_f,cured,deaths,confirmed=lines.rstrip("\n").split(",")
    if no not in covidlist:
        covidlist[no]={"no":no,"date":date,"time":time,"state":state,"confirmed_i":confirmed_i,"confirmed_f":confirmed_f,"cured":cured,"deaths":deaths,"confirmed":confirmed}
print(covidlist)
def print_covid_data(**kwargs):
    no=kwargs["no"]
    if no in covidlist:
        print(covidlist[no]["date"])
        if "prop" in kwargs:
            prop=kwargs["prop"]
            print(covidlist[no][prop])
        else:
            pass
    else:
        print("no not exist")
print_covid_data(no="3",prop="cured")