#Add the text files to the same folder as this project is in
#A proper compiler such as VS Code is must to run the code

import time
import customtkinter
from tkinter import *
import CTkTable
import numpy as np
import customtkinter as ctk
from customtkinter import CTk, CTkProgressBar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt



customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("green") 

calorie, Total_water, water, water_need, calorieneed=0, 0, 0, 1, 1

class App(customtkinter.CTk):
    def __init__(self):
        global water
        global data
        global daily_data
        global water_data
        global timestamp
        global calorieneed
        global water_need
        global Total_water
        data = []
        daily_data = []
        water_data = []
        
        timestamp = time.strftime('%H:%M:%S')


        with open('food.txt', 'r') as file: 
             food = file.readlines() 
        for item in food: 
            data.append(item.strip().split(',')) 


        with open('dailyreport.txt', 'r') as file: 
             report = file.readlines() 
        for line in report: 
            daily_data.append(line.strip().split(',')) 
        
        with open('water_data.txt', 'r') as file: 
             water_report = file.readlines() 
        for line in water_report: 
            water_data.append(line.strip().split(',')) 
        

        super().__init__()

        
        self.title("EE_Project")
        self.geometry(f"{1100}x{580}")

        
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1) 
        
        
        
       
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        
        label = ctk.CTkLabel(self, text="Water Goal", font=customtkinter.CTkFont(size=20, weight="bold"))
        label.grid(row=2, column=3, padx=(20,0), pady=(20,0), sticky="nsew")
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        
        label = ctk.CTkLabel(self, text="Calorie Goal", font=customtkinter.CTkFont(size=20, weight="bold"))
        label.grid(row=2, column=2, padx=(20,0), pady=(20,0), sticky="nsew")
        createPieChart(PieV,colV)
        
        createPieChart(PieV,colV)
        
        

        
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Health Companion", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="BMI", command=self.open_input_dialog_event2, font=customtkinter.CTkFont(size=15, weight="bold"), width=250, corner_radius=0, height=40)
        #self.sidebar_button_1.configure(fg_color="Orchid3")
        self.sidebar_button_1.grid(row=1, column=0, padx=0, pady=5)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Add/Edit Profile", command=self.open_input_dialog_event3, font=customtkinter.CTkFont(size=15, weight="bold"), width=250, corner_radius=0, height=40)
        self.sidebar_button_2.grid(row=2, column=0, padx=0, pady=5)
        
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Check Your Goals", command=self.report, font=customtkinter.CTkFont(size=15, weight="bold"), width=250, corner_radius=0, height=40)
        self.sidebar_button_4.grid(row=3, column=0, padx=0, pady=5)
        #self.sidebar_button_5 = customtkinter.CTkButton(self.sidebar_frame, text="Calories Burnt", command=self.burnt)
        #self.sidebar_button_5.grid(row=4, column=0, padx=20, pady=(10,250))
        self.optionmenu_5 = customtkinter.CTkOptionMenu(self.sidebar_frame, dynamic_resizing=False,
                                                        values=["Walking", "Running", "Swimming", "Add Manually"], command=self.exercise_call, font=customtkinter.CTkFont(size=15, weight="bold"), width=250, corner_radius=0, height=40)
        
        self.optionmenu_5.grid(row=4, column=0, padx=0, pady=(10, 350))
        self.optionmenu_5.set("Exercises")
        
       
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        

        
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter water in ml")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
       
        
        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="DodgerBlue4", text="Add Water", text_color=("gray10", "#DCE4EE"), command=self.water_, font=customtkinter.CTkFont(size=15, weight="bold"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        
        self.textbox1 = customtkinter.CTkTextbox(self, width=200)
        self.textbox1.grid(row=1, column=0, padx=(5, 5), pady=(10, 35), sticky="nsew")


        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=3, padx=(10, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Raw Food")
        self.tabview.add("Breakfast")
        self.tabview.add("Fast Food")
        self.tabview.tab("Raw Food").grid_columnconfigure(0, weight=1) 

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("Raw Food"), dynamic_resizing=False,
                                                        values=[data[0][3],data[1][3],data[2][3],data[3][3],data[4][3],data[5][3],data[6][3],data[7][3],data[8][3],data[9][3],data[10][3],data[11][3],data[12][3],data[13][3]] ,command=self.optionmenue_callback,  font=customtkinter.CTkFont(size=15, weight="bold"))
        
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        

        self.optionmenu_2 = customtkinter.CTkOptionMenu(self.tabview.tab("Raw Food"), dynamic_resizing=False,
                                                    values=[data[14][3],data[15][3],data[16][3],data[17][3],data[18][3],data[19][3],data[20][3],data[21][3],data[22][3],data[23][3],data[24][3],data[25][3],data[26][3],data[27][3],data[28][3],data[29][3],data[30][3],data[31][3],data[32][3],data[33][3],data[34][3],data[35][3]], command=self.optionmenue_callback, font=customtkinter.CTkFont(size=15, weight="bold"))
        
        self.optionmenu_3 = customtkinter.CTkOptionMenu(self.tabview.tab("Breakfast"), dynamic_resizing=False,
                                                    values=[data[36][3],data[37][3],data[38][3],data[39][3],data[40][3],data[41][3]],command=self.optionmenue_callback, font=customtkinter.CTkFont(size=15, weight="bold"))
        self.optionmenu_3.grid(row=0, column=0, padx=50, pady=(20, 10))
        
        self.optionmenu_2.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        
        self.optionmenu_4 = customtkinter.CTkOptionMenu(self.tabview.tab("Breakfast"), dynamic_resizing=False,
                                                    values=[data[42][3],data[43][3],data[44][3],data[45][3],data[46][3],data[47][3],data[48][3],data[49][3]], command=self.optionmenue_callback, font=customtkinter.CTkFont(size=15, weight="bold"))
        
        self.optionmenu_4.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.optionmenu_5 = customtkinter.CTkOptionMenu(self.tabview.tab("Fast Food"), dynamic_resizing=False,
                                                        values=[data[50][3],data[51][3],data[52][3],data[53][3],data[54][3],data[55][3],data[56][3],data[57][3]] ,command=self.optionmenue_callback,  font=customtkinter.CTkFont(size=15, weight="bold"))
        
        self.optionmenu_5.grid(row=0, column=0, padx=50, pady=(20, 10))
        
        self.optionmenu_6 = customtkinter.CTkOptionMenu(self.tabview.tab("Fast Food"), dynamic_resizing=False,
                                                    values=[data[58][3],data[59][3],data[60][3],data[61][3],data[62][3],data[63][3],data[64][3],data[65][3]], command=self.optionmenue_callback, font=customtkinter.CTkFont(size=15, weight="bold"))
        
        self.optionmenu_6.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("Raw Food"), text="New Meal",
                                                           command=self.open_input_dialog_event1,  font=customtkinter.CTkFont(size=15, weight="bold"))
        
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        

        self.appearance_mode_optionemenu.set("Dark")
        
        self.optionmenu_1.set("Fruits")
        self.optionmenu_2.set("Vegetables")
        self.optionmenu_3.set("Breakfast")
        self.optionmenu_4.set("Beverages")
        self.optionmenu_5.set("Indian snacks")
        self.optionmenu_6.set("Non-Veg")


        
        value = [["Meal","Calories","Protiens","Time"]]+daily_data[-1:-len(daily_data):-1]
        value1 = [["Water","Time"]]+water_data[-1:-len(water_data):-1]
        value2 = [["Exercise","Calories Burnt"]]
        
        table = CTkTable.CTkTable(master=self, row=8, column=4, values=value , header_color="Orchid4",hover_color="gray31",corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
        
        
        table.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        table1 = CTkTable.CTkTable(master=self, row=8, column=2, values=value1, header_color="DodgerBlue2", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table1.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        table2 = CTkTable.CTkTable(master=self, row=8, column=2, values=value2, header_color="tomato", hover_color="gray31",corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table2.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
       

    def open_input_dialog_event1(self):
        timestamp = time.strftime('%H:%M:%S')
        global Total_water
        global water
        global calorie
        global calorieneed
        dialog = customtkinter.CTkInputDialog(text="Enter new meal: ", title="Add a new meal")
        meal=dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Enter calories: ", title="Add a new meal")     
        calorie=dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Enter protien in grams: ", title="Add a new meal")       
        protien=dialog.get_input()
        
        with open("dailyreport.txt", "a") as f:
            f.write(meal+","+calorie+","+protien+","+timestamp+"\n")
                        
        
        daily_data = []
         
        with open('dailyreport.txt', 'r') as file: 
             report = file.readlines() 
        for line in report: 
            daily_data.append(line.strip().split(',')) 
                        
        calorie=calorie+int(data[meal][1])       
        value = [["Meal","Calories","Protiens","Time"]]+daily_data[-1:-100:-1]
        print(value)
        print(daily_data)
        table = CTkTable.CTkTable(master=self, row=8, column=4, values=value, header_color="Orchid3", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        label2 = customtkinter.CTkLabel(master=self, text=f"{calorie} / {calorieneed} calories")
        label2.grid(row=1, column=2, padx=20, pady=(10,10))

        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=2, padx=20, pady=(10,50))
        self.progress.set(int(calorie)/int(calorieneed))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        value = [["Meal","Calories","Protiens","Time"]]+daily_data[-1:-len(daily_data):-1]
        value1 = [["Water","Time"]]+water_data[-1:-len(water_data):-1]
    
        print(value)
        print(value1)
    
        table = CTkTable.CTkTable(master=self, row=8, column=4, values=value, header_color="Orchid3", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        table1 = CTkTable.CTkTable(master=self, row=8, column=2, values=value1, header_color="DodgerBlue2", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table1.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        label2 = customtkinter.CTkLabel(master=self, text=f"{calorie} / {calorieneed} calories")
        label2.grid(row=1, column=2, padx=20, pady=(10,10))

        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=2, padx=20, pady=(10,50))
        self.progress.set(int(calorie)/int(calorieneed))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        createPieChart(PieV,colV)
        
        Total_water=Total_water+int(water)
        
        
        label1 = customtkinter.CTkLabel(master=self, text=f"{Total_water} / {water_need} ml")
        label1.grid(row=1, column=3, padx=20, pady=(10,10))
        
        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=3, padx=20, pady=(10,50))
        self.progress.set(int(Total_water)/int(water_need))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        createPieChart(PieV,colV)
               
    def open_input_dialog_event2(self):
        timestamp = time.strftime('%H:%M:%S')
        dialog = customtkinter.CTkInputDialog(text="Height (cm) ", title="BMI calculator")
        H=dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Weight (kg) ", title="BMI calculator")
        W=dialog.get_input()
        bmi = round(int(W)/((int(H)*int(H))/10000), 2)
        
        self.textbox1.insert("0.0", f"\n Your BMI is {bmi}\n")
       
        #self.label = customtkinter.CTkLabel(self, text=f"Your BMI is: {bmi} ")
        #self.label.grid(row=4, column=0, padx=20, pady=20)
                    
    def open_input_dialog_event3(self):
        timestamp = time.strftime('%H:%M:%S')
        global water_need
        global calorieneed
        global protienneed
        global Total_water
        
        dialog = customtkinter.CTkInputDialog(text="Enter Your Name: ", title="Add a new meal")
        name=dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Enter Your Age: ", title="Profile")
        age=dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Enter Your Gender (M for Male & F for Female): ", title="Profile")
        gender=dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Enter Your Height (cm): ", title="Profile")
        height=dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Enter Your Weight (kg): ", title="Profile")
        weight=dialog.get_input()
        dialog = customtkinter.CTkInputDialog(text="Enter Your Daily activity type (N for Normal & H for High): ", title="Profile")
        activity=dialog.get_input()
        
        with open('profile.txt', 'a') as file: 

         file.write("Name: "+name+"\n"+"Age: "+age+"\n"+"Gender: "+gender+"\n"+"Height: "+height+"\n"+"Weight: "+weight+"\n") 
        
        
        if(activity=="H"):
           activity=1.5
        if(activity=="N"):
           activity=1.2

        if gender=="M":         
           calorieneed = (66.5 + (13.8*int(weight)) + (5*int(height)) - (6.8*int(age)))*activity
           print("\nCalorie goal for the day is set to: ", round(calorieneed,2)," Calories")
        if gender=="F":
           calorieneed = (655.1 + (9.6*int(weight)) + (1.9*int(height)) - (4.7*int(age)))*activity
           print("\nCalorie goal for the day is set to: ", round(calorieneed,2)," Calories")
        protienneed = int(weight)*0.9
        print("Protien goal for the day is set to: ", protienneed," g")
       
        if gender=="M":
            water_need=3700
        if gender=="F":
            water_need=2700
            
            
        self.textbox1.insert("0.0", f"\nHi {name},\n\nYour Calorie goal for the day is set to: {calorieneed}\nProtien goal for the day is set to: {protienneed}\nWater goal is set to: {water_need}\n")
        
        value = [["Meal","Calories","Protiens","Time"]]+daily_data[-1:-len(daily_data):-1]
        value1 = [["Water","Time"]]+water_data[-1:-len(water_data):-1]
    
        print(value)
        print(value1)
    
        table = CTkTable.CTkTable(master=self, row=8, column=4, values=value, header_color="Orchid3", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        table1 = CTkTable.CTkTable(master=self, row=8, column=2, values=value1, header_color="DodgerBlue2", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table1.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        label2 = customtkinter.CTkLabel(master=self, text=f"{calorie} / {calorieneed} calories")
        label2.grid(row=1, column=2, padx=20, pady=(10,10))

        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=2, padx=20, pady=(10,50))
        self.progress.set(int(calorie)/int(calorieneed))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        createPieChart(PieV,colV)
        
        Total_water=Total_water+int(water)
        
        
        label1 = customtkinter.CTkLabel(master=self, text=f"{Total_water} / {water_need} ml")
        label1.grid(row=1, column=3, padx=20, pady=(10,10))
        
        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=3, padx=20, pady=(10,50))
        self.progress.set(int(Total_water)/int(water_need))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        createPieChart(PieV,colV)
                  
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
    
    def report(self):
        timestamp = time.strftime('%H:%M:%S')
        global calorie
        global calorieneed
        global Total_water
        global water
        calorieneed=2000
        water_need=3700
        
        daily_data = []
         
        with open('dailyreport.txt', 'r') as file: 
             report = file.readlines() 
        for line in report: 
            daily_data.append(line.strip().split(',')) 
                        
               
        value = [["Meal","Calories","Protiens","Time"]]+daily_data[-1:-100:-1]
        print(value)
        print(daily_data)
        print(daily_data[-1:-100:-1])
        table = CTkTable.CTkTable(master=self, row=8, column=4, values=value, header_color="Orchid3", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        label2 = customtkinter.CTkLabel(master=self, text=f"{calorie} / {calorieneed} calories")
        label2.grid(row=1, column=2, padx=20, pady=(10,10))

        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=2, padx=20, pady=(10,50))
        self.progress.set(int(calorie)/int(calorieneed))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        createPieChart(PieV,colV)
        
        Total_water=Total_water+int(water)
        
        
        label1 = customtkinter.CTkLabel(master=self, text=f"{Total_water} / {water_need} ml")
        label1.grid(row=1, column=3, padx=20, pady=(10,10))
        
        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=3, padx=20, pady=(10,50))
        self.progress.set(int(Total_water)/int(water_need))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        createPieChart(PieV,colV)

    def burnt(self):
         timestamp = time.strftime('%H:%M:%S')
         dialog = customtkinter.CTkInputDialog(text="Enter the no.of calories you have burnt ", title="Calories Burnt")
         c_burnt=int(dialog.get_input())
         
         calorie=int(calorie)-c_burnt

    def water_(self):
        timestamp = time.strftime('%H:%M:%S')
        global Total_water
        global water
        global calorie
        global calorieneed
        
        water=self.entry.get()
        int_value = int(water)
        with open("water_data.txt", "a") as f:
                    f.write(water+","+timestamp+"\n")
                    
        water_data = []
        with open('water_data.txt', 'r') as file: 
             water_report = file.readlines() 
        for line in water_report: 
            water_data.append(line.strip().split(',')) 
        
        value1 = [["Water","Time"]]+water_data[-1:-100:-1]
        
        table1 = CTkTable.CTkTable(master=self, row=8, column=2, values=value1, header_color="DodgerBlue2", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table1.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        Total_water=Total_water+int(water)
        
        label1 = customtkinter.CTkLabel(master=self, text=f"{Total_water} / {water_need} ml")
        label1.grid(row=1, column=3, padx=20, pady=(10,10))
        
        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=3, padx=20, pady=(10,50))
        self.progress.set(int(Total_water)/int(water_need))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        createPieChart(PieV,colV)

    def optionmenue_callback(self,choice):
        timestamp = time.strftime('%H:%M:%S')
        global calorie
        global Total_water
        global water
        global calorie
        global calorieneed
        print(choice)
        if choice=="Apple(100g)":
            meal=0
            self.textbox1.insert("0.0", "\n\t\tAPPLES\t\n\nThey’re rich in both soluble and insoluble fiber, such as pectin, hemicellulose, and cellulose. These help you manage your blood sugar levels, promote good digestion, and support gut and heart health\nIn addition, they’re a good source of vitamin C\n")
        if choice=="Banana(100g)":
            meal=1
            self.textbox1.insert("0.0", "\n\t\tBANANAS\t\n\nNote that green, unripe bananas are higher in resistant starch than ripe ones, and they’re a good source of the dietary fiber pectin\nVitamin B6: 27% of the DV\nVitamin C: 12% of the DV\nMagnesium: 8% of the DV\n")
        if choice=="Orange(100g)":
            meal=2
            self.textbox1.insert("0.0", "\n\t\tORANGES\t\n\nOranges are known for their high vitamin C content, providing 91% of the DV in a single fruit. They’re also high in potassium, folate, thiamine (vitamin B1), fiber, and plant polyphenols\nStudies have found that consuming whole oranges may lower levels of inflammation, blood pressure, cholesterol, and post-meal blood sugar\n")
        if choice=="Grapes(100g)":
            meal=3
            self.textbox1.insert("0.0", '''\n\t\tGrapes\t\n\nGrapes offer health benefits, primarily due to their high nutrient and antioxidant content. They may benefit the eye, heart, bones, and more. 
Grapes are high in several important nutrients. Just 1 cup (151 grams) of red or green grapes provides :

Calories: 104
Carbs: 27 grams
Protein: 1 gram
Fat: 0.2 grams
Fiber: 1.4 grams
Copper: 21% of the daily value (DV)
Vitamin K: 18% of the DV
Thiamine (vitamin B1): 9% of the DV
Riboflavin (vitamin B2): 8% of the DV
Vitamin B6: 8% of the DV
Potassium: 6% of the DV
Vitamin C: 5% of the DV
Manganese: 5% of the DV
Vitamin E: 2% of the DV''')
        if choice=="Mango(100g)":
            meal=4
            self.textbox1.insert("0.0", "")
        if choice=="Pomegranate(100g)":
            meal=5
            self.textbox1.insert("0.0", "")
        if choice=="Pear(100g)":
            meal=6
            self.textbox1.insert("0.0", "")
        if choice=="Dates(1 piece)":
            meal=7
            self.textbox1.insert("0.0", "")
        if choice=="Melon(100g)":
            meal=8
            self.textbox1.insert("0.0", "")
        if choice=="Plum(100g)":
            meal=9
            self.textbox1.insert("0.0", "")
        if choice=="Papaya(100g)":
            meal=10
            self.textbox1.insert("0.0", "")
        if choice=="Litchi(100g)":
            meal=11
            self.textbox1.insert("0.0", "")
        if choice=="Strawberries(100g)":
            meal=12
            self.textbox1.insert("0.0", "")
        if choice=="Apricot(100g)":
            meal=13
            self.textbox1.insert("0.0", "")
        if choice=="Bottle gourd(100g)":
            meal=14
            self.textbox1.insert("0.0", "")
        if choice=="Ridge gourd(100g)":
            meal=15
            self.textbox1.insert("0.0", "")
        if choice=="Bitter gourd(100g)":
            meal=16
            self.textbox1.insert("0.0", "")
        if choice=="Capsicum(100g)":
            meal=17
            self.textbox1.insert("0.0", "")
        if choice=="Fenugreek leaves(cooked)(100g)":
            meal=18
            self.textbox1.insert("0.0", "")
        if choice=="Radish leaves(100g)":
            meal=19
            self.textbox1.insert("0.0", "")
        if choice=="Spinach(25g)":
            meal=20
            self.textbox1.insert("0.0", "")
        if choice=="Pumpkin(100g)":
            meal=21
            self.textbox1.insert("0.0", "")
        if choice=="Zucchini(100g)":
            meal=22
            self.textbox1.insert("0.0", "")
        if choice=="Drumsticks(100g)":
            meal=23
            self.textbox1.insert("0.0", "")
        if choice=="Tomato(100g)":
            meal=24
            self.textbox1.insert("0.0", "")
        if choice=="Sprouts(100g)":
            meal=25
            self.textbox1.insert("0.0", "")
        if choice=="French beans(100g)":
            meal=26
            self.textbox1.insert("0.0", "")
        if choice=="Kidney beans(100g)":
            meal=27
            self.textbox1.insert("0.0", "")
        if choice=="Soya beans(100g)":
            meal=28
            self.textbox1.insert("0.0", "")
        if choice=="Beans (100g)":
            meal=29
            self.textbox1.insert("0.0", "")
        if choice=="Peas(100g)":
            meal=30
            self.textbox1.insert("0.0", "")
        if choice=="Lady finger(100g)	":
            meal=31
            self.textbox1.insert("0.0", "")
        if choice=="Cabbage(100g)":
            meal=32
            self.textbox1.insert("0.0", "")
        if choice=="Cauliflower(100g)":
            meal=33
            self.textbox1.insert("0.0", "")
        if choice=="Broccoli(100g)":
            meal=34
            self.textbox1.insert("0.0", "")
        if choice=="Brinjal(100g)":
            meal=35
            self.textbox1.insert("0.0", "")
        if choice=="Poha(100g)":
            meal=36
            self.textbox1.insert("0.0", "")
        if choice=="Upma(100g)":
            meal=37
            self.textbox1.insert("0.0", "")
        if choice=="Scrambled eggs(1)":
            meal=38
            self.textbox1.insert("0.0", "")
        if choice=="Aloo paratha":
            meal=39
            self.textbox1.insert("0.0", "")
        if choice=="Regular white bread toast":
            meal=40
            self.textbox1.insert("0.0", "")
        if choice=="Jam(1 Spoon)":
            meal=41
            self.textbox1.insert("0.0", "")
        if choice=="Green tea":
            meal=42
            self.textbox1.insert("0.0", "")
        if choice=="Black tea":
            meal=43
            self.textbox1.insert("0.0", "")
        if choice=="Milk tea":
            meal=44
            self.textbox1.insert("0.0", "")
        if choice=="Plain milk":
            meal=45
            self.textbox1.insert("0.0", "")
        if choice=="Coconut water":
            meal=46
            self.textbox1.insert("0.0", "")
        if choice=="Cold drink(500ml)":
            meal=47
            self.textbox1.insert("0.0", "")
        if choice=="Milkshake(500ml)":
            meal=48
            self.textbox1.insert("0.0", "")
        if choice=="Beer(500ml)":
            meal=49
            self.textbox1.insert("0.0", "")
        if choice=="Samosa(1 piece)":
            meal=50
            self.textbox1.insert("0.0", "")
        if choice=="Burger(1 piece)":
            meal=51
            self.textbox1.insert("0.0", "")
        if choice=="Sandwich(1 piece)":
            meal=52
            self.textbox1.insert("0.0", "")
        if choice=="Pizza(1 piece)":
            meal=53
            self.textbox1.insert("0.0", "")
        if choice=="Chips(1 Packet)":
            meal=54
            self.textbox1.insert("0.0", "")
        if choice=="Bhel or Pani-puri(1 Serving(6 pieces))":
            meal=55
            self.textbox1.insert("0.0", "")
        if choice=="Pav Bhaji(1 plate)":
            meal=56
            self.textbox1.insert("0.0", "")
        if choice=="Indian sweets(1 piece)":
            meal=57
            self.textbox1.insert("0.0", "")
        if choice=="Fried chicken(1 Serving)":
            meal=58
            self.textbox1.insert("0.0", "")
        if choice=="Tandoori chicken(1 Serving)":
            meal=59
            self.textbox1.insert("0.0", "")
        if choice=="Butter chicken(1 Serving)":
            meal=60
            self.textbox1.insert("0.0", "")
        if choice=="Fried fish(1 Serving)":
            meal=61
            self.textbox1.insert("0.0", "")
        if choice=="Crab(100gm)":
            meal=62
            self.textbox1.insert("0.0", "")
        if choice=="Prawn":
            meal=63
            self.textbox1.insert("0.0", "")
        if choice=="Cooked chicken(100gm)":
            meal=64
            self.textbox1.insert("0.0", "")
        if choice=="Cooked pork(100gm)":
            meal=65
            self.textbox1.insert("0.0", "")
            
            
        with open("dailyreport.txt", "a") as f:
            f.write(data[meal][3]+","+data[meal][1]+","+data[meal][2]+","+timestamp+"\n")
                        
        
        daily_data = []
         
        with open('dailyreport.txt', 'r') as file: 
             report = file.readlines() 
        for line in report: 
            daily_data.append(line.strip().split(',')) 
                        
        calorie=calorie+int(data[meal][1])       
        value = [["Meal","Calories","Protiens","Time"]]+daily_data[-1:-100:-1]
        print(value)
        print(daily_data)
        print(daily_data[-1:-100:-1])
        table = CTkTable.CTkTable(master=self, row=8, column=4, values=value, header_color="Orchid3", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        label2 = customtkinter.CTkLabel(master=self, text=f"{calorie} / {calorieneed} calories")
        label2.grid(row=1, column=2, padx=20, pady=(10,10))

        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=2, padx=20, pady=(10,50))
        self.progress.set(int(calorie)/int(calorieneed))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        value = [["Meal","Calories","Protiens","Time"]]+daily_data[-1:-len(daily_data):-1]
        value1 = [["Water","Time"]]+water_data[-1:-len(water_data):-1]
    
        print(value)
        print(value1)
    
        table = CTkTable.CTkTable(master=self, row=8, column=4, values=value, header_color="Orchid3", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        table1 = CTkTable.CTkTable(master=self, row=8, column=2, values=value1, header_color="DodgerBlue2", hover_color="gray31", corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
        table1.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        label2 = customtkinter.CTkLabel(master=self, text=f"{calorie} / {calorieneed} calories")
        label2.grid(row=1, column=2, padx=20, pady=(10,10))

        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=2, padx=20, pady=(10,50))
        self.progress.set(int(calorie)/int(calorieneed))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        createPieChart(PieV,colV)
        
        Total_water=Total_water+int(water)
        
        
        label1 = customtkinter.CTkLabel(master=self, text=f"{Total_water} / {water_need} ml")
        label1.grid(row=1, column=3, padx=20, pady=(10,10))
        
        self.progress = CTkProgressBar(self)
        self.progress.grid(row=1, column=3, padx=20, pady=(10,50))
        self.progress.set(int(Total_water)/int(water_need))
        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=3,  padx=(20, 0), pady=(20, 0), sticky="nsew")
        
        
        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        createPieChart(PieV,colV)
        
        
        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 220, 220
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        PieV=[(int(Total_water)/water_need)*100, ((water_need-int(Total_water))/water_need)*100]
        colV=["Dodgerblue2","white"]
        createPieChart(PieV,colV)   

        
        canvas = Canvas(self,width=230,height=230, background="gray15")
        canvas.grid(row=1,column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")

        def createPieChart(PieV,colV):
            st = 0
            coord = 30, 30, 240, 240
            for val,col in zip(PieV,colV):    
                canvas.create_arc(coord,start=st,extent = val*3.6,fill=col,outline=col)
                st = st + val*3.6 

        
        PieV=[(calorie/calorieneed)*100,(((calorieneed-calorie)/calorieneed)*100)]
        colV=["Orchid3","white"]
        createPieChart(PieV,colV)
        
    def exercise_call(self,choice):
            timestamp = time.strftime('%H:%M:%S')
            global calorie
            global exercise
            global Total_water
            global water
            global calorieneed
            print(choice)
            
            exercise=[]
            if choice=="Running":
                dialog = customtkinter.CTkInputDialog(text="Enter distance your ran : ", title="Exercise")
                Dist=dialog.get_input()
                
                dialog = customtkinter.CTkInputDialog(text="Enter Time you took : ", title="Exercise")
                T=dialog.get_input()
                
            if choice=="Add Manually":
                
                dialog = customtkinter.CTkInputDialog(text="Name of the Activity : ", title="Exercise")
                act=dialog.get_input()
                
                dialog = customtkinter.CTkInputDialog(text="Calories Burnt : ", title="Exercise")
                burnt=dialog.get_input()
                
                with open('exercise.txt', 'a') as file: 
                    file.write("Activity: "+act+"\t\t"+"Calories Burnt: "+burnt+"\t\t"+"Time: "+timestamp+"\n") 
                
                exercise.append([act,burnt])
                
                calorie=calorie-int(burnt)
                
                value2 = [["Exercise","Calories Burnt"]]+exercise
                
                table2 = CTkTable.CTkTable(master=self, row=8, column=2, values=value2, header_color="tomato", hover_color="gray31",corner_radius=0, font=customtkinter.CTkFont(size=15, weight="bold"))
       
                table2.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")         
                

if __name__ == "__main__":
    app = App()
    app.mainloop() 
    
