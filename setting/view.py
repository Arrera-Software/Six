def ViewBTN(btn1,btn2,btn3,btn4,btn5,btn6):
    btn1.place(x=20,y=70)
    btn2.place(x=20,y=140)
    btn3.place(x=20,y=210)
    btn4.place(x=20,y=280)
    btn5.place(x=20,y=350)
    btn6.place(x=20,y=420)
    
def NoViewBTN(btn1,btn2,btn3,btn4,btn5,btn6):
    btn1.place_forget()
    btn2.place_forget()
    btn3.place_forget()
    btn4.place_forget()
    btn5.place_forget()
    btn6.place_forget()