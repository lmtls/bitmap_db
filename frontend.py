from tkinter import *
from PIL import ImageTk,Image
from backend import Database, BitMapImage
import json

def img():
    canvas=Canvas(window, height=200, width=200)
    canvas.pack()
    img=ImageTk.PhotoImage(Image.open("image.jpg"))
    canvas.create_image(10, 10, anchor=NW, image=img)

class Window(object):
    def __init__(self, window, database):
        self.database = Database(database)
        self.bitmap_img = BitMapImage()
        self.window = window

        l1=Label(self.window,text="Draw your bitmap picture")
        l1.grid(row=0, column=0, columnspan=8)

        self.picture_name = StringVar()
        self.e1=Entry(self.window, text="Picture Name", textvariable=self.picture_name)
        self.e1.grid(row=1, column=0, columnspan=8)
        #first row of checkbuttons
        self.cb_00_var = IntVar()
        self.cb_00=Checkbutton(self.window, variable=self.cb_00_var)
        self.cb_00.grid(row=2, column=0)

        self.cb_01_var = IntVar()
        self.cb_01=Checkbutton(self.window, variable=self.cb_01_var)
        self.cb_01.grid(row=2, column=1)

        self.cb_02_var = IntVar()
        self.cb_02=Checkbutton(self.window, variable=self.cb_02_var)
        self.cb_02.grid(row=2, column=2)

        self.cb_03_var = IntVar()
        self.cb_03=Checkbutton(self.window, variable=self.cb_03_var)
        self.cb_03.grid(row=2, column=3)

        self.cb_04_var = IntVar()
        self.cb_04=Checkbutton(self.window, variable=self.cb_04_var)
        self.cb_04.grid(row=2, column=4)
        
        self.cb_05_var = IntVar()
        self.cb_05=Checkbutton(self.window, variable=self.cb_05_var)
        self.cb_05.grid(row=2, column=5)

        self.cb_06_var = IntVar()
        self.cb_06=Checkbutton(self.window, variable=self.cb_06_var)
        self.cb_06.grid(row=2, column=6)

        self.cb_07_var = IntVar()
        self.cb_07=Checkbutton(self.window, variable=self.cb_07_var)
        self.cb_07.grid(row=2, column=7)

        #second row of checkbuttons

        self.cb_10_var = IntVar()
        self.cb_10=Checkbutton(self.window, variable=self.cb_10_var)
        self.cb_10.grid(row=3, column=0)

        self.cb_11_var = IntVar()
        self.cb_11=Checkbutton(self.window, variable=self.cb_11_var)
        self.cb_11.grid(row=3, column=1)

        self.cb_12_var = IntVar()
        self.cb_12=Checkbutton(self.window, variable=self.cb_12_var)
        self.cb_12.grid(row=3, column=2)

        self.cb_13_var = IntVar()
        self.cb_13=Checkbutton(self.window, variable=self.cb_13_var)
        self.cb_13.grid(row=3, column=3)

        self.cb_14_var = IntVar()
        self.cb_14=Checkbutton(self.window, variable=self.cb_14_var)
        self.cb_14.grid(row=3, column=4)
        
        self.cb_15_var = IntVar()
        self.cb_15=Checkbutton(self.window, variable=self.cb_15_var)
        self.cb_15.grid(row=3, column=5)

        self.cb_16_var = IntVar()
        self.cb_16=Checkbutton(self.window, variable=self.cb_16_var)
        self.cb_16.grid(row=3, column=6)

        self.cb_17_var = IntVar()
        self.cb_17=Checkbutton(self.window, variable=self.cb_17_var)
        self.cb_17.grid(row=3, column=7)

        #third row of checkbuttons

        self.cb_20_var = IntVar()
        self.cb_20=Checkbutton(self.window, variable=self.cb_20_var)
        self.cb_20.grid(row=4, column=0)

        self.cb_21_var = IntVar()
        self.cb_21=Checkbutton(self.window, variable=self.cb_21_var)
        self.cb_21.grid(row=4, column=1)

        self.cb_22_var = IntVar()
        self.cb_22=Checkbutton(self.window, variable=self.cb_22_var)
        self.cb_22.grid(row=4, column=2)

        self.cb_23_var = IntVar()
        self.cb_23=Checkbutton(self.window, variable=self.cb_23_var)
        self.cb_23.grid(row=4, column=3)

        self.cb_24_var = IntVar()
        self.cb_24=Checkbutton(self.window, variable=self.cb_24_var)
        self.cb_24.grid(row=4, column=4)

        self.cb_25_var = IntVar()
        self.cb_25=Checkbutton(self.window, variable=self.cb_25_var)
        self.cb_25.grid(row=4, column=5)

        self.cb_26_var = IntVar()
        self.cb_26=Checkbutton(self.window, variable=self.cb_26_var)
        self.cb_26.grid(row=4, column=6)

        self.cb_27_var = IntVar()
        self.cb_27=Checkbutton(self.window, variable=self.cb_27_var)
        self.cb_27.grid(row=4, column=7)

        #fourth row of checkbuttons

        self.cb_30_var = IntVar()
        self.cb_30=Checkbutton(self.window, variable=self.cb_30_var)
        self.cb_30.grid(row=5, column=0)

        self.cb_31_var = IntVar()
        self.cb_31=Checkbutton(self.window, variable=self.cb_31_var)
        self.cb_31.grid(row=5, column=1)

        self.cb_32_var = IntVar()
        self.cb_32=Checkbutton(self.window, variable=self.cb_32_var)
        self.cb_32.grid(row=5, column=2)

        self.cb_33_var = IntVar()
        self.cb_33=Checkbutton(self.window, variable=self.cb_33_var)
        self.cb_33.grid(row=5, column=3)

        self.cb_34_var = IntVar()
        self.cb_34=Checkbutton(self.window, variable=self.cb_34_var)
        self.cb_34.grid(row=5, column=4)

        self.cb_35_var = IntVar()
        self.cb_35=Checkbutton(self.window, variable=self.cb_35_var)
        self.cb_35.grid(row=5, column=5)

        self.cb_36_var = IntVar()
        self.cb_36=Checkbutton(self.window, variable=self.cb_36_var)
        self.cb_36.grid(row=5, column=6)

        self.cb_37_var = IntVar()
        self.cb_37=Checkbutton(self.window, variable=self.cb_37_var)
        self.cb_37.grid(row=5, column=7)

        #fifth row of checkboxes

        self.cb_40_var = IntVar()
        self.cb_40=Checkbutton(self.window, variable=self.cb_40_var)
        self.cb_40.grid(row=6, column=0)

        self.cb_41_var = IntVar()
        self.cb_41=Checkbutton(self.window, variable=self.cb_41_var)
        self.cb_41.grid(row=6, column=1)

        self.cb_42_var = IntVar()
        self.cb_42=Checkbutton(self.window, variable=self.cb_42_var)
        self.cb_42.grid(row=6, column=2)

        self.cb_43_var = IntVar()
        self.cb_43=Checkbutton(self.window, variable=self.cb_43_var)
        self.cb_43.grid(row=6, column=3)

        self.cb_44_var = IntVar()
        self.cb_44=Checkbutton(self.window, variable=self.cb_44_var)
        self.cb_44.grid(row=6, column=4)

        self.cb_45_var = IntVar()
        self.cb_45=Checkbutton(self.window, variable=self.cb_45_var)
        self.cb_45.grid(row=6, column=5)

        self.cb_46_var = IntVar()
        self.cb_46=Checkbutton(self.window, variable=self.cb_46_var)
        self.cb_46.grid(row=6, column=6)

        self.cb_47_var = IntVar()
        self.cb_47=Checkbutton(self.window, variable=self.cb_47_var)
        self.cb_47.grid(row=6, column=7)

        #sixth row of checkboxes

        self.cb_50_var = IntVar()
        self.cb_50=Checkbutton(self.window, variable=self.cb_50_var)
        self.cb_50.grid(row=7, column=0)

        self.cb_51_var = IntVar()
        self.cb_51=Checkbutton(self.window, variable=self.cb_51_var)
        self.cb_51.grid(row=7, column=1)

        self.cb_52_var = IntVar()
        self.cb_52=Checkbutton(self.window, variable=self.cb_52_var)
        self.cb_52.grid(row=7, column=2)

        self.cb_53_var = IntVar()
        self.cb_53=Checkbutton(self.window, variable=self.cb_53_var)
        self.cb_53.grid(row=7, column=3)

        self.cb_54_var = IntVar()
        self.cb_54=Checkbutton(self.window, variable=self.cb_54_var)
        self.cb_54.grid(row=7, column=4)

        self.cb_55_var = IntVar()
        self.cb_55=Checkbutton(self.window, variable=self.cb_55_var)
        self.cb_55.grid(row=7, column=5)

        self.cb_56_var = IntVar()
        self.cb_56=Checkbutton(self.window, variable=self.cb_56_var)
        self.cb_56.grid(row=7, column=6)

        self.cb_57_var = IntVar()
        self.cb_57=Checkbutton(self.window, variable=self.cb_57_var)
        self.cb_57.grid(row=7, column=7)

        #seventh row of checkbuttons

        self.cb_60_var = IntVar()
        self.cb_60=Checkbutton(self.window, variable=self.cb_60_var)
        self.cb_60.grid(row=8, column=0)

        self.cb_61_var = IntVar()
        self.cb_61=Checkbutton(self.window, variable=self.cb_61_var)
        self.cb_61.grid(row=8, column=1)

        self.cb_62_var = IntVar()
        self.cb_62=Checkbutton(self.window, variable=self.cb_62_var)
        self.cb_62.grid(row=8, column=2)

        self.cb_63_var = IntVar()
        self.cb_63=Checkbutton(self.window, variable=self.cb_63_var)
        self.cb_63.grid(row=8, column=3)

        self.cb_64_var = IntVar()
        self.cb_64=Checkbutton(self.window, variable=self.cb_64_var)
        self.cb_64.grid(row=8, column=4)

        self.cb_65_var = IntVar()
        self.cb_65=Checkbutton(self.window, variable=self.cb_65_var)
        self.cb_65.grid(row=8, column=5)

        self.cb_66_var = IntVar()
        self.cb_66=Checkbutton(self.window, variable=self.cb_66_var)
        self.cb_66.grid(row=8, column=6)

        self.cb_67_var = IntVar()
        self.cb_67=Checkbutton(self.window, variable=self.cb_67_var)
        self.cb_67.grid(row=8, column=7)

        #eighth row of checkboxes

        self.cb_70_var = IntVar()
        self.cb_70=Checkbutton(self.window, variable=self.cb_70_var)
        self.cb_70.grid(row=9, column=0)

        self.cb_71_var = IntVar()
        self.cb_71=Checkbutton(self.window, variable=self.cb_71_var)
        self.cb_71.grid(row=9, column=1)

        self.cb_72_var = IntVar()
        self.cb_72=Checkbutton(self.window, variable=self.cb_72_var)
        self.cb_72.grid(row=9, column=2)

        self.cb_73_var = IntVar()
        self.cb_73=Checkbutton(self.window, variable=self.cb_73_var)
        self.cb_73.grid(row=9, column=3)

        self.cb_74_var = IntVar()
        self.cb_74=Checkbutton(self.window, variable=self.cb_74_var)
        self.cb_74.grid(row=9, column=4)

        self.cb_75_var = IntVar()
        self.cb_75=Checkbutton(self.window, variable=self.cb_75_var)
        self.cb_75.grid(row=9, column=5)

        self.cb_76_var = IntVar()
        self.cb_76=Checkbutton(self.window, variable=self.cb_76_var)
        self.cb_76.grid(row=9, column=6)

        self.cb_77_var = IntVar()
        self.cb_77=Checkbutton(self.window, variable=self.cb_77_var)
        self.cb_77.grid(row=9, column=7)

        #action buttons
        
        b1=Button(self.window, text="View All", command=self.view_command)
        b1.grid(row=10, column = 0, columnspan=8)

        b2=Button(self.window, text="View Selected", command=self.create_window)
        b2.grid(row=11, column = 0, columnspan=8)

        b3=Button(self.window, text="Add the image", command=self.add_command)
        b3.grid(row=12, column = 0, columnspan=8)

        b4=Button(self.window, text="Delete Selected")
        b4.grid(row=13, column = 0, columnspan=8)

        b5=Button(self.window, text="Update Selected")
        b5.grid(row=14, column = 0, columnspan=8)

        b6=Button(self.window, text="Search by Name")
        b6.grid(row=15, column = 0, columnspan=8)

        b7=Button(self.window, text="Close", command=self.window.destroy)
        b7.grid(row=16, column = 0, columnspan=8)

        #listbox

        sb1=Scrollbar(self.window)
        sb1.grid(row=2, column=8, rowspan=8)

        self.list1=Listbox(self.window, height=16, width=35)
        self.list1.grid(row=1, column=9, rowspan=12)

        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        self.list1.bind("<<ListboxSelect>>", self.get_selected_row)

    def create_window(self):
        new_window=Toplevel(self.window)
        img_name = self.bitmap_img.create(self.data)
        print (img_name)
        canvas=Canvas(new_window, height=16, width=16)
        canvas.pack()
        img=ImageTk.PhotoImage(Image.open(img_name))
        canvas.create_image(8, 8, anchor=NW, image=img)

    def get_selected_row(self, event):
        index=self.list1.curselection()
        self.data=self.database.search_by_id(index[0]+1)
        print(self.data)
        self.e1.insert(END, self.data[1])
        checker = lambda cb, n: cb.select() if n=='1' else cb.deselect() 
        row0=self.data[2]
        checker(self.cb_00, row0[0])
        checker(self.cb_01, row0[1])
        checker(self.cb_02, row0[2])
        checker(self.cb_03, row0[3])
        checker(self.cb_04, row0[4])
        checker(self.cb_05, row0[5])
        checker(self.cb_06, row0[6])
        checker(self.cb_07, row0[7])
        row1=self.data[3]
        checker(self.cb_10, row1[0])
        checker(self.cb_11, row1[1])
        checker(self.cb_12, row1[2])
        checker(self.cb_13, row1[3])
        checker(self.cb_14, row1[4])
        checker(self.cb_15, row1[5])
        checker(self.cb_16, row1[6])
        checker(self.cb_17, row1[7])
        row2=self.data[4]
        checker(self.cb_20, row2[0])
        checker(self.cb_21, row2[1])
        checker(self.cb_22, row2[2])
        checker(self.cb_23, row2[3])
        checker(self.cb_24, row2[4])
        checker(self.cb_25, row2[5])
        checker(self.cb_26, row2[6])
        checker(self.cb_27, row2[7])
        row3=self.data[5]
        checker(self.cb_30, row3[0])
        checker(self.cb_31, row3[1])
        checker(self.cb_32, row3[2])
        checker(self.cb_33, row3[3])
        checker(self.cb_34, row3[4])
        checker(self.cb_35, row3[5])
        checker(self.cb_36, row3[6])
        checker(self.cb_37, row3[7])
        row4=self.data[6]
        checker(self.cb_40, row4[0])
        checker(self.cb_41, row4[1])
        checker(self.cb_42, row4[2])
        checker(self.cb_43, row4[3])
        checker(self.cb_44, row4[4])
        checker(self.cb_45, row4[5])
        checker(self.cb_46, row4[6])
        checker(self.cb_47, row4[7])
        row5=self.data[7]
        checker(self.cb_50, row5[0])
        checker(self.cb_51, row5[1])
        checker(self.cb_52, row5[2])
        checker(self.cb_53, row5[3])
        checker(self.cb_54, row5[4])
        checker(self.cb_55, row5[5])
        checker(self.cb_56, row5[6])
        checker(self.cb_57, row5[7])
        row6=self.data[8]
        checker(self.cb_60, row6[0])
        checker(self.cb_61, row6[1])
        checker(self.cb_62, row6[2])
        checker(self.cb_63, row6[3])
        checker(self.cb_64, row6[4])
        checker(self.cb_65, row6[5])
        checker(self.cb_66, row6[6])
        checker(self.cb_67, row6[7])
        row7=self.data[9]
        checker(self.cb_70, row7[0])
        checker(self.cb_71, row7[1])
        checker(self.cb_72, row7[2])
        checker(self.cb_73, row7[3])
        checker(self.cb_74, row7[4])
        checker(self.cb_75, row7[5])
        checker(self.cb_76, row7[6])
        checker(self.cb_77, row7[7])


    def view_command(self):
        self.list1.delete(0, END)
        for row in self.database.view_all():
            self.list1.insert(END, row)

    def add_command(self):
        r0=str(self.cb_00_var.get())+str(self.cb_01_var.get())+str(self.cb_02_var.get())+str(self.cb_03_var.get())+str(self.cb_04_var.get())+str(self.cb_05_var.get())+str(self.cb_06_var.get())+str(self.cb_07_var.get())
        r1=str(self.cb_10_var.get())+str(self.cb_11_var.get())+str(self.cb_12_var.get())+str(self.cb_13_var.get())+str(self.cb_14_var.get())+str(self.cb_15_var.get())+str(self.cb_16_var.get())+str(self.cb_17_var.get())
        r2=str(self.cb_20_var.get())+str(self.cb_21_var.get())+str(self.cb_22_var.get())+str(self.cb_23_var.get())+str(self.cb_24_var.get())+str(self.cb_25_var.get())+str(self.cb_26_var.get())+str(self.cb_27_var.get())
        r3=str(self.cb_30_var.get())+str(self.cb_31_var.get())+str(self.cb_32_var.get())+str(self.cb_33_var.get())+str(self.cb_34_var.get())+str(self.cb_35_var.get())+str(self.cb_36_var.get())+str(self.cb_37_var.get())
        r4=str(self.cb_40_var.get())+str(self.cb_41_var.get())+str(self.cb_42_var.get())+str(self.cb_43_var.get())+str(self.cb_44_var.get())+str(self.cb_45_var.get())+str(self.cb_46_var.get())+str(self.cb_47_var.get())
        r5=str(self.cb_50_var.get())+str(self.cb_51_var.get())+str(self.cb_52_var.get())+str(self.cb_53_var.get())+str(self.cb_54_var.get())+str(self.cb_55_var.get())+str(self.cb_56_var.get())+str(self.cb_57_var.get())
        r6=str(self.cb_60_var.get())+str(self.cb_61_var.get())+str(self.cb_62_var.get())+str(self.cb_63_var.get())+str(self.cb_64_var.get())+str(self.cb_65_var.get())+str(self.cb_66_var.get())+str(self.cb_67_var.get())
        r7=str(self.cb_70_var.get())+str(self.cb_71_var.get())+str(self.cb_72_var.get())+str(self.cb_73_var.get())+str(self.cb_74_var.get())+str(self.cb_75_var.get())+str(self.cb_76_var.get())+str(self.cb_77_var.get())
        self.database.add(str(self.picture_name.get()), r0, r1, r2, r3, r4, r5, r6, r7)
        print([r0,r1,r2,r3,r4,r5,r6,r7])
            

window = Tk()
Window(window, "bitmap_database.db")
window.mainloop()