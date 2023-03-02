                
class Health:
    bmi1=[]
    bmr=[]
    daily_bmr_level=[]
    print("----------------*** calculate of your body mass index(BMI) enter the detai***---------------")
    
    def __init__(self,gender,age,height,weight):
        self.gender=gender
        self.age=age
        self.height=height
        self.weight=weight
        

    def body_bmi(self):
  
        m=self.height/3.28
        bmi=self.weight/m**2
        self.bmi1.append(bmi)
        print("BMI adults:",bmi)

    def health_status(self):
        print("\n----------------***check your health status as per BMI***----------------")
        for i in self.bmi1:
            if i<16:
                print("severe thinness (cause):\nmalnutrition \nosteoporosis \ndecreased muscle strength \nhypothemia \nlowered immunity ")

            elif i>16 and i<17:
                print("moderate thinness (cause):\ndecrease in body fluid \nmuscal mass \nfat ")

            elif i>17 and i<18.5:
                print("mild thinness risk (cause):\nfactor in eating disorders \nmetabolic and hereditary factor \npsychological and emotional stress \naddiction to alcohol and street drugs ")

            elif i>18.5 and i<25:
                print("normal range:\nnormal and healthy ")

            elif i>25 and i<30:
                print("over weight (casue and risk):\neating too much and moving too little \n(risk) \nhigh blood pressure(hypertension) \ntype-2 diabetes \ncoronary heart disease \nstroke \ngallbladder disease \nosteoarthritis \nlow quality of life ")

            elif i>30 and i<35:
                print("obesity class 1 (casue and risk):\neating too much and moving too little \n(risk) \nhigh blood pressure(hypertension) \ntype-2 diabetes \ncoronary heart disease \nstroke \ngallbladder disease \nosteoarthritis \nlow quality of life ")

            elif i>35 and i<40:
                print("obesity class 2 (casue and risk):\neating too much and moving too little \n(risk) \nhigh blood pressure(hypertension) \ntype-2 diabetes \ncoronary heart disease \nstroke \ngallbladder disease \nosteoarthritis \nlow quality of life ")

            else:
                print("obesity class 3 (casue and risk):\neating too much and moving too little \n(risk) \nhigh blood pressure(hypertension) \ntype-2 diabetes \ncoronary heart disease \nstroke \ngallbladder disease \nosteoarthritis \nlow quality of life ")


    def body_bmr(self):
        print("\n----------------***(BMR)basal etabolic rate,the amount of energy(calaorie) your body needs to maintain daily bsis***----------------") 
       
        if self.gender=="male":
            a=(4.563*self.weight*2.20)+(15.88*self.height*12)-(5*self.age)+5
            self.bmr.append(a)
            print(a,"daily calories requrment")

        elif self.gender=="female":
            b=(4.563*self.weight*2.20)+(15.88*self.height*12)-(5*self.age)-161
            self.bmr.append(b)
            print(b,"daily calories requrment")

        else:
            print("enter valid detail")


             
    def daily_req_calorie_level(self):
        print("\n----------------***please choose the option from as per your daily exercise activity***----------------")
        c=float(input("\n1.little or no exercies\n2.light exercise or sports 1-3 days/week \n3.moderately exercise 3-5 days/week \n4.hard exercise 6-7 days/week \n5.very hard exercise and physical job \n enter "))
        if c==1:
                
                for i in self.bmr:
                    a=i*1.2
                    self.daily_bmr_level.append(a)
                    print(a,"daily calories requrment")
                 
        elif c==2:
            for i in self.bmr:
                b=i*1.375
                self.daily_bmr_level.append(b)
                print(b,"daily calories requrment")
                 
        elif c==3:
            for i in self.bmr:
                c=i*1.55
                self.daily_bmr_level.append(c)
                print(c,"daily calories requrment")
                 
             
        elif c==4:
            for i in self.bmr:
                d=i*1.725
                self.daily_bmr_level.append(d)
                print(d,"daily calories requrment")
                     

        elif c==5:
             for i in self.bmr:
                 e=i*1.9
                 self.daily_bmr_level.append(e)
                 print(e,"daily calories requrment")
                      
             
                 
    def micro_and_macro(self):#1gm protine=4calorie,1gm carb=4 calorie,1gm fat=9 calorie
        for i in self.daily_bmr_level:
            a=30/100*i
            b=20/100*i
            c=50/100*i
            print("\n----------------***calories from protine ,carbs and fat***----------------")
            print("calories from protines:",a,"fats:",b,"carbohydrates:",c)
            print("protines in gm:",a/4,"fats in gm:",b/9,"carbohydrates in gm:",c/4)
            
    def water_intake(self):
        print("\n----------------***Daily water requirements for body***----------------")
        if self.gender=="male":
            print("daily water intake is 3.7 liters per day--")
        else:
            print("daily water intake is 2.7 liters per day--")

    def calories_burn(self):
        a=input("\n----------------***want to burn your calories yes/no***----------------")
        if a=="yes":
            print("\nplease choose your activity for calculate burning calories ")
            print("7.5  bicycling, general") 
            print("14.0 bicycling, mountain, uphill, vigorous") 
            print("8.0  exercise calisthenics (e.g., push ups, sit ups, pull-ups, jumping jacks), vigorous effort") 
            print("5.0  exercise health club exercise classes, general, gym/weight training combined in one visit") 
            print("3.8  exercise home exercise, general") 
            print("9.0  exercise stair-treadmill ergometer, general") 
            print("4.0  exercise yoga, Power") 
            print("3.3  exercise yoga, Surya Namaskar") 
            print("7.3  dancing aerobic, general") 
            print("3.5  multiple household tasks all at once, moderate effort") 
            print("3.0  walk/stand combination, for volunteer purposes") 
            print("7.0  jogging, general") 
            print("6.0  Running, 4 mph (13 min/mile)") 
            print("8.3  running, 5 mph (12 min/mile)") 
            print("9.0  running, 5.2 mph (11.5 min/mile)") 
            print("9.8  running, 6 mph (10 min/mile)") 
            print("10.5 running, 6.7 mph (9 min/mile)") 
            print("6.3  climbing hills, no load") 
            print("5.3  snow shoeing, moderate effort") 
            print("10.0 snow shoeing, vigorous effor") 
            print("13.3 skiing, cross-country, skating") 
            print("7.0  skating, ice, general") 
            print("5.5  water aerobics, water calisthenics") 
            print("10.0 water polo") 
            print("3.0  water volleyball") 
            print("9.8  water jogging") 
            print("13.8 swimming, butterfly, general") 
            print("4.0  paddle boat") 
            print("4.0  volleyball") 
            print("7.3  tennis, general") 
            print("10.0 soccer, competitive") 
            print("7.0  soccer, casual, general") 
            print("7.8  hockey, field") 
            print("4.8  golf, general") 
            print("4.8  cricket, batting, bowling, fielding") 
            print("6.5  basketball, general")
            mets=float(input("enter the mets "))
            time=float(input("enter the duration hours"))
            for i in self.bmr:
                a=i*mets/24*time
                print(a,"calories burn in",time,"hours","\n Thank you")
                            
        else:
            print("thank you")



gender=input("enter your gender male/female____")

try:
    
    age=float(input("enter your age____"))
    height=float(input("enter your height in foot____"))
    weight=float(input("enter your weight in kg____"))
    
except ValueError:
    print("enter the numbers only")   


    

a=Health(gender,age,height,weight)

a.body_bmi()

a.health_status()

a.body_bmr()

a.daily_req_calorie_level()

a.micro_and_macro()

a.water_intake()

a.calories_burn()

























