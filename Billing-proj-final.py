from tkinter import*
from tkinter import messagebox
import random
import pymysql
from datetime import datetime
import time;

class Billing:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Super Market Billing")
        title=Label(self.root,text="Super Market Billing",bd=12,relief=GROOVE,bg="#074463",fg="White",
                    font=("times new roman",30,"bold"),pady=2).pack(fill=X)

       
#=============Variables==================
        #===Cosmetics===
        self.bath_soap=IntVar()
        self.Face_cream=IntVar()
        self.Face_wash=IntVar()
        self.Tooth_paste=IntVar()
        self.Tooth_brush=IntVar()
        self.Hair_wash=IntVar()
        #====Grocery====
        self.Rice=IntVar()
        self.salt=IntVar()
        self.sugar=IntVar()
        self.wheat=IntVar()
        self.oil=IntVar()
        self.dhaal=IntVar()
        #====Drinks======
        self.frooti=IntVar()
        self.Maaza=IntVar()
        self.limca=IntVar()
        self.up=IntVar()
        self.sprite=IntVar()
        self.cola=IntVar()
        #====Total price and Tax====
        self.cosmetic_price=StringVar()
        self.grocery_price=StringVar()
        self.drinks_price=StringVar()

        self.cosmetic_tax=StringVar()
        self.grocery_tax=StringVar()
        self.drinks_tax=StringVar()
        #======Customer=====
        self.Customer_name=StringVar()
        self.Customer_phone=StringVar()
        x=random.randint(1000,9999)
        self.Bill_no=StringVar()
        self.Bill_no.set(str(x))
        self.txtarea=StringVar()
        
        self.date=StringVar()
       

    
        
  #======Total Button=====
        self.total=IntVar()
    
#=====================Customer Detail Frame=================================
        
        F1=LabelFrame(self.root,bd=10,relief=GROOVE,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F1.place(x=0,y=80,relwidth=1)
        
        customername_lbl=Label(F1,text="Customer Name",bg="#074463",fg="White",
                               font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)  
        customername_text=Entry(F1,width=15,textvariable=self.Customer_name,font="arial,15",
                               bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)

        customerphone_lbl=Label(F1,text="Phone Number",bg="#074463",fg="White",
                               font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)  
        customerphone_text=Entry(F1,width=15,textvariable=self.Customer_phone,font="arial,15",
                               bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

        customerbill_lbl=Label(F1,text="Bill Number",bg="#074463",fg="White",
                               font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)  
        customerbill_text=Entry(F1,width=15,textvariable=self.Bill_no,font="arial,15",
                               bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=10)
        
        self.date.set(time.strftime("%d/%m/%y"))
        
        
        Date_lbl=Label(F1,text="Date",bg="#074463",fg="White",
                           font=("times new roman",15,"bold")).grid(row=0,column=6,padx=10,pady=5)
        Date_text=Entry(F1,width=7,textvariable=self.date,font="arial,15",
                               bd=7,relief=SUNKEN).grid(row=0,column=7,pady=5,padx=10)

        
#===============Cosmetics Frame=======
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Cosmetics",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F2.place(x=5,y=180,width=325,height=380)

        bath_lbl=Label(F2,text="Bath Soap",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")

        bath_text=Entry(F2,width=10,textvariable=self.bath_soap,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
                               
        FaceCream_lbl=Label(F2,text="Face Cream",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")

        FaceCream_text=Entry(F2,width=10,textvariable=self.Face_cream,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
                               
        FaceWash_lbl=Label(F2,text="Face Wash",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")

        FaceWash_text=Entry(F2,width=10,textvariable=self.Face_wash,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
            
        ToothPaste_lbl=Label(F2,text="Tooth Paste",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")

        ToothPaste_text=Entry(F2,width=10,textvariable=self.Tooth_paste,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)

        ToothBrush_lbl=Label(F2,text="Tooth Brush",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")

        ToothBrush_text=Entry(F2,width=10,textvariable=self.Tooth_brush,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)

        HairWash_lbl=Label(F2,text="Hair Wash",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")

        HairWash_text=Entry(F2,width=10,textvariable=self.Hair_wash,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)

        #===============Groceries=======
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Grocery",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F3.place(x=340,y=180,width=325,height=380)

        g1_lbl=Label(F3,text="Rice",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")

        g1_text=Entry(F3,width=10,textvariable=self.Rice,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
                               
        g2_lbl=Label(F3,text="Food Oil",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")

        g2_text=Entry(F3,width=10,textvariable=self.oil,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
                               
        g3_lbl=Label(F3,text="Wheat",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")

        g3_text=Entry(F3,width=10,textvariable=self.wheat,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
            
        g4_lbl=Label(F3,text="Dhaal",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")

        g4_text=Entry(F3,width=10,textvariable=self.dhaal,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)

        g5_lbl=Label(F3,text="Sugar",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")

        g5_text=Entry(F3,width=10,textvariable=self.sugar,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)

        g6_lbl=Label(F3,text="Salt",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")

        g6_text=Entry(F3,width=10,textvariable=self.salt,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)

         #==============Drinks======
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Drinks",font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F4.place(x=670,y=180,width=325,height=380)

        c1_lbl=Label(F4,text="Frooti",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")

        c1_text=Entry(F4,width=10,textvariable=self.frooti,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
                               
        c2_lbl=Label(F4,text="Maaza",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")

        c2_text=Entry(F4,width=10,textvariable=self.Maaza,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=1,column=1,pady=5,padx=10)
                               
        c3_lbl=Label(F4,text="Limca",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")

        c3_text=Entry(F4,width=10,textvariable=self.limca,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=2,column=1,pady=5,padx=10)
            
        c4_lbl=Label(F4,text="Sprite",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")

        c4_text=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=3,column=1,pady=5,padx=10)

        c5_lbl=Label(F4,text="Cola",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")

        c5_text=Entry(F4,width=10,textvariable=self.cola,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=4,column=1,pady=5,padx=10)

        c6_lbl=Label(F4,text="7UP",bg="#074463",fg="Light Green",
                               font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")

        c6_text=Entry(F4,width=10,textvariable=self.up,font=("times new roman",16,"bold"),
                               bd=5,relief=SUNKEN).grid(row=5,column=1,pady=5,padx=10)

         #==============Billing======
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=1000,y=180,width=350,height=380)
        bill_title=Label(F5,text="CASH BILL",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)
        
        #====Button frame=====

        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",
                      font=("times new roman",15,"bold"),fg="gold",bg="#074463")
        F6.place(x=0,y=560,relwidth=1,height=140)
        
        m1_lbl=Label(F6,text="Total Cosmetic price",bg="#074463",fg="white",
                 font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_text=Entry(F6,width=18,font=("ariel",10,"bold"),textvariable=self.cosmetic_price,
                      bd=5,relief=SUNKEN).grid(row=0,column=1,pady=1,padx=10)

        m2=Label(F6,text="Total Grocery price",bg="#074463",fg="white",
                 font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_text=Entry(F6,width=18,textvariable=self.grocery_price,font=("ariel",10,"bold"),
                               bd=5,relief=SUNKEN).grid(row=1,column=1,pady=1,padx=10)

        m3=Label(F6,text="Total Drinks price",bg="#074463",fg="white",
                 font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_text=Entry(F6,width=18,textvariable=self.drinks_price,font=("ariel",10,"bold"),
                               bd=5,relief=SUNKEN).grid(row=2,column=1,pady=1,padx=10)

        c1_lbl=Label(F6,text="Cosmetic Tax",bg="#074463",fg="white",
                 font=("times new roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky="w")
        c1_text=Entry(F6,width=18,textvariable=self.cosmetic_tax,font=("ariel",10,"bold"),
                               bd=5,relief=SUNKEN).grid(row=0,column=3,pady=1,padx=10)

        c2=Label(F6,text="Grocery Tax",bg="#074463",fg="white",
                 font=("times new roman",14,"bold")).grid(row=1,column=2,padx=20,pady=1,sticky="w")
        c2_text=Entry(F6,width=18,textvariable=self.grocery_tax,font=("ariel",10,"bold"),
                               bd=5,relief=SUNKEN).grid(row=1,column=3,pady=1,padx=10)

        c3=Label(F6,text="Drinks Tax",bg="#074463",fg="white",
                 font=("times new roman",14,"bold")).grid(row=2,column=2,padx=20,pady=1,sticky="w")
        c3_text=Entry(F6,width=18,textvariable=self.drinks_tax,font=("ariel",10,"bold"),
                               bd=5,relief=SUNKEN).grid(row=2,column=3,pady=1,padx=10)

        def total():
             self.a1= self.bath_soap.get()*40
             self.a2=self.Face_cream.get()*150
             self.a3=(self.Face_wash.get()*120)
             self.a4=(self.Tooth_paste.get()*50)
             self.a5=(self.Tooth_brush.get()*60)
             self.a6=(self.Hair_wash.get()*100)
             self.total_cosmetic_price=(self.a1+self.a2+self.a3+self.a4+self.a5+self.a6)
            
             self.cosmetic_price.set("Rs."+str(self.total_cosmetic_price))
             self.c_tax=round((self.total_cosmetic_price*0.02),2)
             self.cosmetic_tax.set("Rs."+str(self.c_tax))

             self.Grocery1=(self.Rice.get()*200)
             self.Grocery2=(self.sugar.get()*100)
             self.Grocery3=(self.salt.get()*120)
             self.Grocery4=(self.dhaal.get()*150)
             self.Grocery5=(self.wheat.get()*160)
             self.Grocery6=(self.oil.get()*300)
             self.total_Grocery_price=(self.Grocery1+self.Grocery2+self.Grocery3+self.Grocery4+self.Grocery5+self.Grocery6)
            
             self.grocery_price.set("Rs."+str(self.total_Grocery_price))
             self.g_tax=round((self.total_Grocery_price*0.02),2)
             self.grocery_tax.set("Rs."+str(self.g_tax))

             self.Drink1=(self.Maaza.get()*50)
             self.Drink2=(self.limca.get()*80)
             self.Drink3=(self.up.get()*90)
             self.Drink4=(self.frooti.get()*60)
             self.Drink5=(self.sprite.get()*100)
             self.Drink6=(self.cola.get()*120)
             self.total_Drink_price=(self.Drink1+self.Drink2+self.Drink3+self.Drink4+self.Drink5+self.Drink6)
            
             self.drinks_price.set("Rs."+str(self.total_Drink_price))
             self.d_tax=round((self.total_Drink_price*0.02),2)
             self.drinks_tax.set("Rs."+str(self.d_tax))
            
             self.total=("Rs."+str(self.total_cosmetic_price+self.total_Grocery_price+self.total_Drink_price+
                         self.c_tax+self.g_tax+self.d_tax))
             
                 
             
        def generate_bill():
    
            self.txtarea.delete('1.0',END)
            self.txtarea.insert(END,"\tWELCOME TO PUVI SUPERMARKET")
            self.txtarea.insert(END,f"\nBILL NO :{self.Bill_no.get()}")
            self.txtarea.insert(END,f"\nDate :{self.date.get()}")
            self.txtarea.insert(END,f"\nCUSTOMER NAME :{self.Customer_name.get()}")
            self.txtarea.insert(END,f"\nPHONE_NUMBER :{self.Customer_phone.get()}")
            self.txtarea.insert(END,f"\n======================================")
            self.txtarea.insert(END,f"\nPRODUCTS\t\tQUANTITY\t\tPRICE")
            self.txtarea.insert(END,f"\n======================================")
            
            #======cosmetics=========

            if self.bath_soap.get()!=0:
                self.txtarea.insert(END,f"\n Bath Soap\t\t{self.bath_soap.get()}\t\t{self.a1}")
            if self.Face_cream.get()!=0:
                self.txtarea.insert(END,f"\n Face Cream\t\t{self.Face_cream.get()}\t\t{self.a2}")
            if self.Face_wash.get()!=0:
                self.txtarea.insert(END,f"\n Face Wash\t\t{self.Face_wash.get()}\t\t{self.a3}")
            if self.Tooth_paste.get()!=0:
                self.txtarea.insert(END,f"\n Tooth Paste\t\t{self.Tooth_paste.get()}\t\t{self.a4}")
            if self.Tooth_brush.get()!=0:
                self.txtarea.insert(END,f"\n Tooth Brush\t\t{self.Tooth_brush.get()}\t\t{self.a5}")
            if self.Hair_wash.get()!=0:
                self.txtarea.insert(END,f"\n Hair Wash\t\t{self.Hair_wash.get()}\t\t{self.a6}")


        #=========GROCERY=======================
            if self.Rice.get()!=0:
                self.txtarea.insert(END,f"\n Rice\t\t{self.Rice.get()}\t\t{self.Grocery1}")
            if self.sugar.get()!=0:
                self.txtarea.insert(END,f"\n Sugar\t\t{self.sugar.get()}\t\t{self.Grocery2}")
            if self.salt.get()!=0:
                self.txtarea.insert(END,f"\n Salt\t\t{self.salt.get()}\t\t{self.Grocery3}")
            if self.dhaal.get()!=0:
                self.txtarea.insert(END,f"\n Dhaal\t\t{self.dhaal.get()}\t\t{self.Grocery4}")
            if self.wheat.get()!=0:
                self.txtarea.insert(END,f"\n Wheat\t\t{self.wheat.get()}\t\t{self.Grocery5}")
            if self.oil.get()!=0:
                self.txtarea.insert(END,f"\n Food Oil\t\t{self.oil.get()}\t\t{self.Grocery6}")

        #=========DRINKS=================
            if self.Maaza.get()!=0:
                self.txtarea.insert(END,f"\n Maaza\t\t{self.Maaza.get()}\t\t{self.Drink1}")
            if self.limca.get()!=0:
                self.txtarea.insert(END,f"\n Limca\t\t{self.limca.get()}\t\t{self.Drink2}")
            if self.up.get()!=0:
                self.txtarea.insert(END,f"\n 7UP\t\t{self.up.get()}\t\t{self.Drink3}")
            if self.frooti.get()!=0:
                self.txtarea.insert(END,f"\n Frooti\t\t{self.frooti.get()}\t\t{self.Drink4}")
            if self.sprite.get()!=0:
                self.txtarea.insert(END,f"\n Sprite\t\t{self.sprite.get()}\t\t{self.Drink5}")
            if self.cola.get()!=0:
                self.txtarea.insert(END,f"\n Cola\t\t{self.cola.get()}\t\t{self.Drink6}")

            self.txtarea.insert(END,"\n--------------------------------------")
            
            if self.cosmetic_tax.get()!="Rs.0.0":
                self.txtarea.insert(END,f"\n Cosmetic Tax :\t\t{self.cosmetic_tax.get()}")
            if self.grocery_tax.get()!="Rs.0.0":
                self.txtarea.insert(END,f"\n Grocery Tax :\t\t{self.grocery_tax.get()}")
            if self.drinks_tax.get()!="Rs.0.0":
                self.txtarea.insert(END,f"\n Drinks Tax :\t\t{self.drinks_tax.get()}")
                
            self.txtarea.insert(END,f"\n--------------------------------------")
            
            self.txtarea.insert(END,f"\n Total Amount :\t\t{self.total}")
                
            self.txtarea.insert(END,f"\n--------------------------------------")

        def reset():
            self.txtarea.delete('1.0',END)
            self.bath_soap.set(0)
            self.Face_cream.set(0)
            self.Face_wash.set(0)
            self.Tooth_paste.set(0)
            self.Tooth_brush.set(0)
            self.Hair_wash.set(0)
        #====Grocery====
            self.Rice.set(0)
            self.salt.set(0)
            self.sugar.set(0)
            self.wheat.set(0)
            self.oil.set(0)
            self.dhaal.set(0)
        #====Drinks======
            self.frooti.set(0)
            self.Maaza.set(0)
            self.limca.set(0)
            self.up.set(0)
            self.sprite.set(0)
            self.cola.set(0)
        #====Total price and Tax====
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.drinks_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.drinks_tax.set("")
        #======Customer=====
            self.Customer_name.set("")
            self.Customer_phone.set("")
            x=random.randint(1000,9999)
            self.Bill_no.set("")
            self.Bill_no.set(str(x))
        reset()
            
                

        def save():
          
##            bill_no=self.Bill_no.get()
##            customer_name = self.Customer_name.get()
##            customer_ph = self.Customer_phone.get()
##            total_amount= self.total
##    
##            db = pymysql.connect("localhost","root","12345","billing")
##            cursor = db.cursor()
##            sql ="""INSERT INTO customer_bill(bill_no,customer_name,customer_ph,total_amount)
##                    VALUES('{}','{}','{}','{}');""".format(bill_no,customer_name,
##                                                           customer_ph,total_amount)
##            try:
##                cursor.execute(sql)
##                db.commit()
##                #print(cursor.fetchall()) 
##            except:
##                print("Error")
##                db.rollback()
##                db.close()
                
                self.bill_data=self.txtarea.get('1.0',END)
                f1=open("C:/bill/"+str(self.Bill_no.get())+".txt","w")
                f1.write(self.bill_data)
                messagebox.showinfo("Saved",f"Bill no. :{self.Bill_no.get()} saved successfully")
                f1.close()

        button_F=Frame(F6,bd=7,relief=GROOVE)
        button_F.place(x=750,width=580,height=105)

        total_btn=Button(button_F,text="Total",command=total,bg="#074463",fg="white",bd=2,pady=15,width=10,
                         font="arial 12 bold").grid(row=0,column=0,padx=5,pady=5)
        G_btn=Button(button_F,text="Generate Bill",command=generate_bill,bg="#074463",fg="white",bd=2,pady=15,width=10,
                         font="arial 12 bold").grid(row=0,column=1,padx=5,pady=5)

        Save_btn=Button(button_F,text="Save",command=save,bg="#074463",fg="white",bd=2,pady=15,width=10,
                         font="arial 12 bold").grid(row=0,column=2,padx=5,pady=5)

        Reset_btn=Button(button_F,text="Reset",command=reset,bg="#074463",fg="white",bd=2,pady=15,width=10,
                        font="arial 12 bold").grid(row=0,column=3,padx=5,pady=5)
      
                                                                     
root=Tk()
obj=Billing(root)
root.mainloop()
