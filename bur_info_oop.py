import tkinter as tk
from tkinter import ttk
from ttkbootstrap import *
from ttkbootstrap.constants import *
from math import *


# -------------------------------------- spisok burenya ---------------------------------------------
lst_doloto = [0, 92.1, 95.2, 98.4, 104.8, 114.3, 117.5, 120.7, 123.8,
              127.0, 133.4, 139.7, 146.1, 149.2, 152.4, 155.6, 158.8,
              165.1, 171.4, 190.5, 200.0, 212.7, 215.9, 222.2, 241.3,
              250.8, 266.7, 269.9, 279.4, 295.3, 301.6, 304.8, 311.1,
              349.3, 355.6, 374.6, 393.7, 406.4, 431.6, 444.5, 469.9,
              508.0, 558.8, 584.2, 609.6, 660.4, 711.2, 762.0]

lst_kls = [0]
lst_klp = [0]
lst_ubt_l = [0]
lst_ubt_d = [0, 79, 89, 108, 121, 127, 146, 165, 171, 178, 197, 203, 216,
             229, 241, 248, 254, 279]
lst_ubt_i = [0, '', '---- UBT 79 içki Ø  ----', '', 32,
             '', '---- UBT 89 içki Ø  ----', '', 38,
             '', '---- UBT 108 içki Ø  ----', '', 46,
             '', '---- UBT 121 içki Ø  ----', '', 51,
             '', '---- UBT 127 içki Ø  ----', '', 57,
             '', '---- UBT 146 içki Ø  ----', '', 57,
             '', '---- UBT 165 içki Ø  ----', '', 57, 71,
             '', '---- UBT 171 içki Ø  ----', '', 57, 71,
             '', '---- UBT 178 içki Ø  ----', '', 57, 71,
             '', '---- UBT 197 içki Ø  ----', '', 71,
             '', '---- UBT 203 içki Ø  ----', '', 80,
             '', '---- UBT 216 içki Ø  ----', '', 71, 76,
             '', '---- UBT 229 içki Ø  ----', '', 71, 80,
             '', '---- UBT 241 içki Ø  ----', '', 71, 76,
             '', '---- UBT 248 içki Ø  ----', '', 71, 76, 80,
             '', '---- UBT 254 içki Ø  ----', '', 100,
             '', '---- UBT 279 içki Ø  ----', '', 76, 100]
lst_bt_l = [0]
lst_bt_d = [0, 60.33, 73.03, 88.90, 101.6, 114.3, 127.0, 139.7]
lst_bt_i = [0, '', '---- BT 60 içki Ø  ----', '', 46.11, 42.3,
            '', '---- BT 73 içki Ø  ----', '',59.0, 55.0, 51.0,
            '', '---- BT 89 içki Ø  ----', '',  75.0, 70.2, 66.1,
            '', '---- BT 102 içki Ø ----', '',  87.6, 85.6, 84.6, 81.6,
            '', '---- BT 114 içki Ø ----', '', 100.3, 98.3, 97.1, 94.3, 92.4,
            '', '---- BT 127 içki Ø ----', '', 113.0, 111.0, 108.6, 106.0, 101.6,
            '', '---- BT 140 içki Ø ----', '', 123.7, 121.3, 119.7, 118.6]
lst_ergin_dyk = [0]
lst_matr_dyk = [1, '', '----  Polat  ----', '', 7.85,
                '', '---- Alýumin ----', '', 2.7,
                '', '----   Med   ----', '', 8.96,
                '', '----  Latun  ----', '', 8.5]

count = 0.9
while True:
    lst_ergin_dyk.append(count * 100 // 1 / 100)
    count += 0.02
    if len(lst_ergin_dyk) == 105:
        break

cnt = 10
while True:
    lst_ubt_l.append(cnt)
    cnt += 1
    if len(lst_ubt_l) == 166:
        break

cnt1 = 10
while True:
    lst_bt_l.append(cnt1)
    cnt1 += 1
    if len(lst_bt_l) == 9502:
        break

cnt2 = 1
while True:
    lst_kls.append(cnt2)
    cnt2 += 1
    if len(lst_kls) == 15:
        break

cnt3 = 1
while True:
    lst_klp.append(cnt3)
    cnt3 += 1
    if len(lst_klp) == 15:
        break

# -------------------------------------- spisok nasosa ---------------------------------------------

lst_porshn = [0]
lst_hermey = [0]
lst_stok = [0]
lst_minher = [0]
lst_sany = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

cnt_prn = 10
while True:
    lst_porshn.append(cnt_prn)
    cnt_prn += 5
    if len(lst_porshn) == 61:
        break

cnt_mm = 5
while True:
    lst_hermey.append(cnt_mm)
    cnt_mm += 5
    if len(lst_hermey) == 101:
        break

cnt_st = 1
while True:
    lst_stok.append(cnt_st)
    cnt_st += 1
    if len(lst_stok) == 151:
        break

cnt_hm = 1
while True:
    lst_minher.append(cnt_hm)
    cnt_hm += 1
    if len(lst_minher) == 1501:
        break
# -------------------------------------- Bur parametr barada ---------------------------------------------
class BurParametr(Frame):
    def __init__(self, master):
        super(BurParametr, self).__init__(master)
        self.pack(fill=BOTH, expand=True)
        self.creat_widgets()

    # arassala knopka
    def clr(self):
        self.lbx_ans.delete(0, END)

    # jogap knopka
    def pls(self):
        try:
            d_dolata = float(self.cbx_doloto.get())
            l_kls = float(self.cbx_kls.get())
            l_klp = float(self.cbx_klp.get())
            l_ubt = float(self.cbx_ubt_l.get())
            d_ubt_d = float(self.cbx_ubt_d.get())
            d_ubt_i = float(self.cbx_ubt_i.get())
            l_bt = float(self.cbx_bt_l.get())
            d_bt_d = float(self.cbx_bt_d.get())
            d_bt_i = float(self.cbx_bt_i.get())
            p_ergin = float(self.cbx_ergin_dyk.get())
            p_matr = float(self.cbx_matr_dyk.get())
            # zaboy cunluk
            l_zaboy = (0.40 + l_kls + l_klp + l_ubt + l_bt) * 100 // 1 / 100
            # dlina komponowka
            l_komp = l_kls + l_klp + l_ubt
            # wes kompomowka
            wes_komp = (p_matr * (pi / 4) * (pow(d_ubt_d, 2) - pow(d_ubt_i, 2)) * l_komp) / 1000000
            # wes BT
            wes_bt = (p_matr * (pi / 4) * (pow(d_bt_d, 2) - pow(d_bt_i, 2)) * l_bt) / 1000000
            # wes na wozduhe
            wes_n_w = wes_komp + wes_bt
            # koeffissent plawucesti
            koef_plw = 1 - (p_ergin / p_matr)
            # wes na rastwore
            wes_n_r = wes_n_w * koef_plw
            # obyom skwazhiny
            v_guyy = pi * pow(((d_dolata / 2) / 1000), 2) * l_zaboy
            # kolsowoy obyom komponowka
            v_komp = (pi / 4) * (pow((d_ubt_d / 1000), 2) - pow((d_ubt_i / 1000), 2)) * l_komp
            # kolsowoy obyom BT
            v_bt = (pi / 4) * (pow((d_bt_d / 1000), 2) - pow((d_bt_i / 1000), 2)) * l_bt
            # obyom instrumenta
            v_instr = v_komp + v_bt
            # obyom rastwora
            v_rast = v_guyy - v_instr
            # obyom wnutri ubt
            v_v_komp = pi * pow(((d_ubt_i / 2) / 1000), 2) * l_komp
            # obyom wnutri bt
            v_v_bt = pi * pow(((d_bt_i / 2) / 1000), 2) * l_bt
            # obshiy obyom wnutri instr
            ob_o_v_inst = v_v_komp + v_v_bt
            # obshiy obyom naruzhe instr
            ob_o_n_inst = v_rast - ob_o_v_inst
            # jogaplar
            zaboy = f' Zaboy L = {l_zaboy} m'
            wes_na_wozd = f' Howadaky agramy = {wes_n_w * 1000 // 1 / 1000} t'
            wes_na_rast = f' Ergindaki agramy = {wes_n_r * 1000 // 1 / 1000} t'
            oby_guy = f' Guyyn V = {v_guyy * 1000 // 1 / 1000} m³'
            oby_rast_j = f' Guyun erginin jemi V = {v_rast * 1000 // 1 / 1000} m³'
            oby_rast_i = f' Inst-n icki erginin V = {ob_o_v_inst * 1000 // 1 / 1000} m³'
            oby_rast_d = f' Inst-n dasky erginin V = {ob_o_n_inst * 1000 // 1 / 1000} m³'
            oby_instr = f' Instrumedyn V = {v_instr * 100 // 1 / 100} m³'
            self.lbx_ans.delete(0, END)
            self.lbx_ans.insert(0, '  --------------------  Zaboy  --------------------', '',
                           zaboy,
                           '', '  --------------------   Wes   --------------------', '',
                           wes_na_wozd, wes_na_rast,
                           '', '  ------------------   Obyom   -------------------', '',
                           oby_guy, oby_rast_j, oby_rast_i, oby_rast_d, oby_instr)
        except:
            self.lbx_ans.delete(0, END)

    def creat_widgets(self):
        self.lbl_doloto = Label(self, text='Doloto Ø : ', font=('Arial', 14))
        self.lbl_doloto.grid(row=3, column=2, ipadx=10, ipady=5, sticky='e')

        self.lbl_kls = Label(self, text='KLS L : ', font=('Aral', 14))
        self.lbl_kls.grid(row=4, column=2, ipadx=10, ipady=5, sticky='e')

        self.lbl_klp = Label(self, text='KLP L : ', font=('Arial', 14))
        self.lbl_klp.grid(row=5, column=2, ipadx=10, ipady=5, sticky='e')

        self.lbl_ubt_l = Label(self, text='UBT L : ', font=('Arial', 14))
        self.lbl_ubt_l.grid(row=6, column=2, ipadx=10, ipady=5, sticky='e')

        self.lbl_ubt_d = Label(self, text='UBT daşky Ø : ', font=('Arial', 14))
        self.lbl_ubt_d.grid(row=7, column=2, ipadx=10, ipady=5, sticky='e')

        self.lbl_ubt_i = Label(self, text='UBT içki Ø : ', font=('Arial', 14))
        self.lbl_ubt_i.grid(row=8, column=2, ipadx=10, ipady=5, sticky='e')

        self.lbl_bt_l = Label(self, text='BT L : ', font=('Arial', 14))
        self.lbl_bt_l.grid(row=9, column=2, ipadx=10, ipady=5, sticky='e')

        self.lbl_bt_d = Label(self, text='BT daşky Ø : ', font=('Arial', 14))
        self.lbl_bt_d.grid(row=10, column=2, ipadx=10, ipady=5, sticky='e')

        self.lbl_bt_i = Label(self, text='BT içki Ø : ', font=('Arial', 14))
        self.lbl_bt_i.grid(row=11, column=2, ipadx=10, ipady=5, sticky='e')

        self.lbl_ergin_dyk = Label(self, text='ρ ergin g/sm³ : ', font=('Arial', 14))
        self.lbl_ergin_dyk.grid(row=12, column=2, ipadx=10, ipady=5, sticky='e')

        self.lbl_mater_dyk = Label(self, text='ρ materýal g/sm³ : ', font=('Arial', 14))
        self.lbl_mater_dyk.grid(row=13, column=2, ipadx=10, ipady=5, sticky='e')

        self.doloto_var = DoubleVar(value=lst_doloto[0])

        self.kls_var = IntVar(value=lst_kls[0])

        self.klp_var = IntVar(value=lst_klp[0])

        self.ubt_l_var = IntVar(value=lst_ubt_l[0])

        self.ubt_d_var = IntVar(value=lst_ubt_d[0])

        self.ubt_i_var = IntVar(value=lst_ubt_i[0])

        self.bt_l_var = IntVar(value=lst_bt_l[0])

        self.bt_d_var = DoubleVar(value=lst_bt_d[0])

        self.bt_i_var = DoubleVar(value=lst_bt_i[0])

        self.ergin_dyk_var = DoubleVar(value=lst_ergin_dyk[0])

        self.matr_dyk_var = DoubleVar(value=lst_matr_dyk[0])

        self.cbx_doloto = Combobox(self, textvariable=self.doloto_var, values=lst_doloto, state='readonly')
        self.cbx_doloto.grid(row=3, column=3)

        self.cbx_kls = Combobox(self, textvariable=self.kls_var, values=lst_kls, state='readonly')
        self.cbx_kls.grid(row=4, column=3)

        self.cbx_klp = Combobox(self, textvariable=self.klp_var, values=lst_klp, state='readonly')
        self.cbx_klp.grid(row=5, column=3)

        self.cbx_ubt_l = Combobox(self, textvariable=self.ubt_l_var, values=lst_ubt_l, state="readonly")
        self.cbx_ubt_l.grid(row=6, column=3)

        self.cbx_ubt_d = Combobox(self, textvariable=self.ubt_d_var, values=lst_ubt_d, state='readonly')
        self.cbx_ubt_d.grid(row=7, column=3)

        self.cbx_ubt_i = Combobox(self, textvariable=self.ubt_i_var, values=lst_ubt_i, state='readonly')
        self.cbx_ubt_i.grid(row=8, column=3)

        self.cbx_bt_l = Combobox(self, textvariable=self.bt_l_var, values=lst_bt_l, state='readonly')
        self.cbx_bt_l.grid(row=9, column=3)

        self.cbx_bt_d = Combobox(self, textvariable=self.bt_d_var, values=lst_bt_d, state='readonly')
        self.cbx_bt_d.grid(row=10, column=3)

        self.cbx_bt_i = Combobox(self, textvariable=self.bt_i_var, values=lst_bt_i, state='readonly')
        self.cbx_bt_i.grid(row=11, column=3)

        self.cbx_ergin_dyk = Combobox(self, textvariable=self.ergin_dyk_var, values=lst_ergin_dyk, state='readonly')
        self.cbx_ergin_dyk.grid(row=12, column=3)

        self.cbx_matr_dyk = Combobox(self, textvariable=self.matr_dyk_var, values=lst_matr_dyk, state='readonly')
        self.cbx_matr_dyk.grid(row=13, column=3)

        self.lbx_ans = tk.Listbox(self, font=('Arial', 14))
        self.lbx_ans.configure(fg='black')
        self.lbx_ans.grid(row=3, rowspan=11, column=4, ipadx=54, ipady=77.5)

        self.ans_btn = Button(self, text='Jogap', bootstyle='success toolbutton outline', command=self.pls)
        self.ans_btn.grid(row=14, column=3, ipadx=45, ipady=10)

        self.clr_btn = Button(self, text='Arassala', bootstyle='danger toolbutton outline', command=self.clr)
        self.clr_btn.grid(row=14, column=4, ipadx=133, ipady=10)

        self.clc_btn = Button(self, text='Calculator', bootstyle='primary toolbutton outline', command=self.calc)
        self.clc_btn.grid(row=14, column=2, ipadx=65, ipady=10)

    # Calculator knopka
    def calc(self):
        root = Window()
        root.geometry('346x355+200+200')
        root.title('Calculator')
        root.resizable(False, False)

        def mtd_1():
            enter.insert(END, '1')

        def mtd_2():
            enter.insert(END, '2')

        def mtd_3():
            enter.insert(END, '3')

        def mtd_4():
            enter.insert(END, '4')

        def mtd_5():
            enter.insert(END, '5')

        def mtd_6():
            enter.insert(END, '6')

        def mtd_7():
            enter.insert(END, '7')

        def mtd_8():
            enter.insert(END, '8')

        def mtd_9():
            enter.insert(END, '9')

        def mtd_0():
            enter.insert(END, '0')

        def mtd_div():
            enter.insert(END, '/')

        def mtd_mult():
            enter.insert(END, '*')

        def mtd_min():
            enter.insert(END, '-')

        def mtd_pls():
            enter.insert(END, '+')

        def mtd_pnt():
            enter.insert(END, '.')

        def equal():
            tex = enter.get()
            try:
                ans = eval(str(tex))
                enter.delete(0, END)
                enter.insert(0, str(ans * 100 // 1 / 100))
            except:
                enter.delete(0, END)
                enter.insert(0, 'Nadogry!!!')
                enter.config(state=DISABLED)

        def clear():
            enter.delete(0, END)
            enter.config(state=ACTIVE)
            enter.delete(0, END)

        def delete():
            txt = enter.get()
            enter.delete(len(txt) - 1, END)

        enter = Entry(root, textvariable='', justify=RIGHT, font=('Arial', 20))
        enter.grid(row=0, column=0, columnspan=4, rowspan=2, ipady=10, ipadx=20)

        tk.Button(root, text='1', command=mtd_1, font=('Arial', 20)).grid(row=3, column=0, stick='wens')
        tk.Button(root, text='2', command=mtd_2, font=('Arial', 20)).grid(row=3, column=1, stick='wens')
        tk.Button(root, text='3', command=mtd_3, font=('Arial', 20)).grid(row=3, column=2, stick='wens')
        tk.Button(root, text='4', command=mtd_4, font=('Arial', 20)).grid(row=4, column=0, stick='wens')
        tk.Button(root, text='5', command=mtd_5, font=('Arial', 20)).grid(row=4, column=1, stick='wens')
        tk.Button(root, text='6', command=mtd_6, font=('Arial', 20)).grid(row=4, column=2, stick='wens')
        tk.Button(root, text='7', command=mtd_7, font=('Arial', 20)).grid(row=5, column=0, stick='wens')
        tk.Button(root, text='8', command=mtd_8, font=('Arial', 20)).grid(row=5, column=1, stick='wens')
        tk.Button(root, text='9', command=mtd_9, font=('Arial', 20)).grid(row=5, column=2, stick='wens')
        tk.Button(root, text='0', command=mtd_0, font=('Arial', 20)).grid(row=6, column=0, stick='wens')
        tk.Button(root, text='/', command=mtd_div, font=('Arial', 20)).grid(row=3, column=3, stick='wens')
        tk.Button(root, text='*', command=mtd_mult, font=('Arial', 20)).grid(row=4, column=3, stick='wens')
        tk.Button(root, text='-', command=mtd_min, font=('Arial', 20)).grid(row=5, column=3, stick='wens')
        tk.Button(root, text='+', command=mtd_pls, font=('Arial', 20)).grid(row=6, column=3, stick='wens')
        tk.Button(root, text='.', command=mtd_pnt, font=('Arial', 20)).grid(row=6, column=1, stick='wens')
        tk.Button(root, text='=', command=equal, font=('Arial', 20)).grid(row=6, column=2, stick='wens')
        tk.Button(root, text='C', command=clear, font=('Arial', 20)).grid(row=2, column=0, columnspan=2, stick='wens')
        tk.Button(root, text='delete', command=delete, font=('Arial', 20)).grid(row=2, column=2, columnspan=2,
                                                                                stick='wens')

        root.grid_columnconfigure(0, minsize=60)
        root.grid_columnconfigure(1, minsize=60)
        root.grid_columnconfigure(2, minsize=60)
        root.grid_columnconfigure(3, minsize=60)

        root.grid_rowconfigure(2, minsize=60)
        root.grid_rowconfigure(3, minsize=60)
        root.grid_rowconfigure(4, minsize=60)
        root.grid_rowconfigure(5, minsize=60)
        root.grid_rowconfigure(6, minsize=60)

# ---------------------------------  Nasosyn ondurijiligi barada   ---------------------------------------

class NasosParametr(Frame):
    def __init__(self, master):
        super(NasosParametr, self).__init__(master)
        self.pack(fill=BOTH, expand=True)

        self.zagalowok = tk.LabelFrame(self, text='Nasosyň öndürijiligi', labelanchor=N, font=('Arial', 20))
        self.zagalowok.pack(fill=BOTH, expand=True)

        self.clc_btn = Button(self.zagalowok, text='Calculator', bootstyle='primary toolbutton outline', command=self.calc)
        self.clc_btn.grid(row=2, column=1, columnspan=2, ipadx=65, ipady=10, pady=15)

        self.ans_btn1 = Button(self.zagalowok, text='Jogap', bootstyle='success toolbutton outline', command=self.bir_tarap_has)
        self.ans_btn1.grid(row=1, column=0, ipadx=47, ipady=7, pady=5)

        self.clr_btn1 = Button(self.zagalowok, text='Arassala', bootstyle='danger toolbutton outline', command=self.bir_tarap_poz)
        self.clr_btn1.grid(row=1, column=1, ipadx=40, ipady=7, pady=5)

        self.ans_btn2 = Button(self.zagalowok, text='Jogap', bootstyle='success toolbutton outline', command=self.iki_tarap_has)
        self.ans_btn2.grid(row=1, column=2, ipadx=47, ipady=7, pady=5)

        self.clr_btn2 = Button(self.zagalowok, text='Arassala', bootstyle='danger toolbutton outline', command=self.iki_tarap_poz)
        self.clr_btn2.grid(row=1, column=3, ipadx=40, ipady=7, pady=5)

        self.bir_tarap()
        self.iki_tarap()

    def calc(self):
        root = Window()
        root.geometry('346x355+200+200')
        root.title('Calculator')
        root.resizable(False, False)

        def mtd_1():
            enter.insert(END, '1')

        def mtd_2():
            enter.insert(END, '2')

        def mtd_3():
            enter.insert(END, '3')

        def mtd_4():
            enter.insert(END, '4')

        def mtd_5():
            enter.insert(END, '5')

        def mtd_6():
            enter.insert(END, '6')

        def mtd_7():
            enter.insert(END, '7')

        def mtd_8():
            enter.insert(END, '8')

        def mtd_9():
            enter.insert(END, '9')

        def mtd_0():
            enter.insert(END, '0')

        def mtd_div():
            enter.insert(END, '/')

        def mtd_mult():
            enter.insert(END, '*')

        def mtd_min():
            enter.insert(END, '-')

        def mtd_pls():
            enter.insert(END, '+')

        def mtd_pnt():
            enter.insert(END, '.')

        def equal():
            tex = enter.get()
            try:
                ans = eval(str(tex))
                enter.delete(0, END)
                enter.insert(0, str(ans * 100 // 1 / 100))
            except:
                enter.delete(0, END)
                enter.insert(0, 'Nadogry!!!')
                enter.config(state=DISABLED)

        def clear():
            enter.delete(0, END)
            enter.config(state=ACTIVE)
            enter.delete(0, END)

        def delete():
            txt = enter.get()
            enter.delete(len(txt) - 1, END)

        enter = Entry(root, textvariable='', justify=RIGHT, font=('Arial', 20))
        enter.grid(row=0, column=0, columnspan=4, rowspan=2, ipady=10, ipadx=20)

        tk.Button(root, text='1', command=mtd_1, font=('Arial', 20)).grid(row=3, column=0, stick='wens')
        tk.Button(root, text='2', command=mtd_2, font=('Arial', 20)).grid(row=3, column=1, stick='wens')
        tk.Button(root, text='3', command=mtd_3, font=('Arial', 20)).grid(row=3, column=2, stick='wens')
        tk.Button(root, text='4', command=mtd_4, font=('Arial', 20)).grid(row=4, column=0, stick='wens')
        tk.Button(root, text='5', command=mtd_5, font=('Arial', 20)).grid(row=4, column=1, stick='wens')
        tk.Button(root, text='6', command=mtd_6, font=('Arial', 20)).grid(row=4, column=2, stick='wens')
        tk.Button(root, text='7', command=mtd_7, font=('Arial', 20)).grid(row=5, column=0, stick='wens')
        tk.Button(root, text='8', command=mtd_8, font=('Arial', 20)).grid(row=5, column=1, stick='wens')
        tk.Button(root, text='9', command=mtd_9, font=('Arial', 20)).grid(row=5, column=2, stick='wens')
        tk.Button(root, text='0', command=mtd_0, font=('Arial', 20)).grid(row=6, column=0, stick='wens')
        tk.Button(root, text='/', command=mtd_div, font=('Arial', 20)).grid(row=3, column=3, stick='wens')
        tk.Button(root, text='*', command=mtd_mult, font=('Arial', 20)).grid(row=4, column=3, stick='wens')
        tk.Button(root, text='-', command=mtd_min, font=('Arial', 20)).grid(row=5, column=3, stick='wens')
        tk.Button(root, text='+', command=mtd_pls, font=('Arial', 20)).grid(row=6, column=3, stick='wens')
        tk.Button(root, text='.', command=mtd_pnt, font=('Arial', 20)).grid(row=6, column=1, stick='wens')
        tk.Button(root, text='=', command=equal, font=('Arial', 20)).grid(row=6, column=2, stick='wens')
        tk.Button(root, text='C', command=clear, font=('Arial', 20)).grid(row=2, column=0, columnspan=2, stick='wens')
        tk.Button(root, text='delete', command=delete, font=('Arial', 20)).grid(row=2, column=2, columnspan=2,
                                                                                stick='wens')

        root.grid_columnconfigure(0, minsize=60)
        root.grid_columnconfigure(1, minsize=60)
        root.grid_columnconfigure(2, minsize=60)
        root.grid_columnconfigure(3, minsize=60)

        root.grid_rowconfigure(2, minsize=60)
        root.grid_rowconfigure(3, minsize=60)
        root.grid_rowconfigure(4, minsize=60)
        root.grid_rowconfigure(5, minsize=60)
        root.grid_rowconfigure(6, minsize=60)


    def bir_tarap_has(self):
        dp = float(self.porshn_sanaw.get()) / 1000
        im = float(self.porshn_hermey.get()) / 1000
        mh = float(self.porshn_minher.get())
        ps = float(self.porshn_sany_combo.get())
        ls = (((pi * ((dp/2) ** 2) * im * mh) / 60) * ps) * 1000
        mk = (ls * 3600) / 1000
        self.ent_ls.delete(0, END)
        self.ent_ksag.delete(0, END)
        self.ent_ls.insert(0, (ls * 100 // 1 / 100))
        self.ent_ksag.insert(0, (mk * 100 // 1 / 100))

    def bir_tarap_poz(self):
        self.ent_ls.delete(0, END)
        self.ent_ksag.delete(0, END)

    def iki_tarap_has(self):
        dp = float(self.porshn_sanaw1.get()) / 1000
        im = float(self.porshn_hermey1.get()) / 1000
        st = float(self.diam_stok1.get()) / 1000
        mh = float(self.porshn_minher1.get())
        ps = float(self.porshn_sany_combo1.get())
        ls = (((((pi * ((dp/2) ** 2) * im) + ((pi * ((dp/2) ** 2) * im)- (pi * ((st/2) ** 2) * im))) * mh) / 60) * ps) * 1000
        mk = (ls * 3600) / 1000
        self.ent_ls1.delete(0, END)
        self.ent_ksag1.delete(0, END)
        self.ent_ls1.insert(0, (ls * 100 // 1 / 100))
        self.ent_ksag1.insert(0, (mk * 100 // 1 / 100))

    def iki_tarap_poz(self):
        self.ent_ls1.delete(0, END)
        self.ent_ksag1.delete(0, END)

    def bir_tarap(self):
        self.bir_tarap = tk.LabelFrame(self.zagalowok, text='Bir taraplaýyn öndüriji', labelanchor=N, font=('Arial', 20))
        self.bir_tarap.grid(row=0, column=0, columnspan=2, padx=10, pady=5)

        self.d_porshn = Label(self.bir_tarap, text='porşun Ø', font=('Arial', 14))
        self.d_porshn.grid(row=0, column=0, sticky='e')

        self.porshn_sanaw_var = IntVar(value=lst_porshn[0])
        self.porshn_sanaw = Combobox(self.bir_tarap, width=5, textvariable=self.porshn_sanaw_var, values=lst_porshn, state='readonly')
        self.porshn_sanaw.grid(row=0, column=1, padx=10, pady=15)

        self.dm_mm = Label(self.bir_tarap, text='mm', font=('Arial', 12))
        self.dm_mm.grid(row=0, column=2, sticky='w')

        self.d_ismey = Label(self.bir_tarap, text='iş meýdany', font=('Arial', 14))
        self.d_ismey.grid(row=1, column=0, sticky='e')

        self.porshn_hermey_var = IntVar(value=lst_hermey[0])
        self.porshn_hermey = Combobox(self.bir_tarap, width=5, textvariable=self.porshn_hermey_var, values=lst_hermey, state='readonly')
        self.porshn_hermey.grid(row=1, column=1, padx=10, pady=15)

        self.hm_mm = Label(self.bir_tarap, text='mm', font=('Arial', 12))
        self.hm_mm.grid(row=1, column=2, sticky='w')

        self.her_porshn = Label(self.bir_tarap, text='min/hereket', font=('Arial', 14))
        self.her_porshn.grid(row=2, column=0, sticky='e')

        self.porshn_minher_var = IntVar(value=lst_minher[0])
        self.porshn_minher = Combobox(self.bir_tarap, width=5, textvariable=self.porshn_minher_var, values=lst_minher, state='readonly')
        self.porshn_minher.grid(row=2, column=1, padx=10, pady=15)

        self.mh = Label(self.bir_tarap, text='san', font=('Arial', 12))
        self.mh.grid(row=2, column=2, sticky='w')

        self.porshn_sany = Label(self.bir_tarap, text='porşun sany', font=('Arial', 14))
        self.porshn_sany.grid(row=3, column=0, sticky='e')

        self.porshn_sany_var = IntVar(value=lst_sany[0])
        self.porshn_sany_combo = Combobox(self.bir_tarap, width=5, textvariable=self.porshn_sany_var, values=lst_sany, state='readonly')
        self.porshn_sany_combo.grid(row=3, column=1, padx=10, pady=15)

        self.ps = Label(self.bir_tarap, text='san', font=('Arial', 12))
        self.ps.grid(row=3, column=2, sticky='w')

        self.lbl_ls = Label(self.bir_tarap, text='l/s', font=('Arial', 14))
        self.lbl_ls.grid(row=0, column=3, sticky='s')

        self.ent_ls = Entry(self.bir_tarap, width=7, font=('Arial', 12))
        self.ent_ls.grid(row=1, column=3, padx=15, sticky='n')

        self.lbl_ksag = Label(self.bir_tarap, text='m³/sag', font=('Arial', 14))
        self.lbl_ksag.grid(row=2, column=3, sticky='s')

        self.ent_ksag = Entry(self.bir_tarap, width=7, font=('Arial', 12))
        self.ent_ksag.grid(row=3, column=3, padx=15, sticky='n')

    def iki_tarap(self):
        self.iki_tarap = tk.LabelFrame(self.zagalowok, text='Iki taraplaýyn öndüriji', labelanchor=N, font=('Arial', 20))
        self.iki_tarap.grid(row=0, column=2, columnspan=2, padx=10, pady=5)

        self.d_porshn1 = Label(self.iki_tarap, text='porşun Ø', font=('Arial', 14))
        self.d_porshn1.grid(row=0, column=0, sticky='e')

        self.porshn_sanaw_var1 = IntVar(value=lst_porshn[0])
        self.porshn_sanaw1 = Combobox(self.iki_tarap, width=5, textvariable=self.porshn_sanaw_var1, values=lst_porshn, state='readonly')
        self.porshn_sanaw1.grid(row=0, column=1, padx=10, pady=9)

        self.dm_mm1 = Label(self.iki_tarap, text='mm', font=('Arial', 12))
        self.dm_mm1.grid(row=0, column=2, sticky='w')

        self.d_ismey1 = Label(self.iki_tarap, text='iş meýdany', font=('Arial', 14))
        self.d_ismey1.grid(row=1, column=0, sticky='e')

        self.porshn_hermey_var1 = IntVar(value=lst_hermey[0])
        self.porshn_hermey1 = Combobox(self.iki_tarap, width=5, textvariable=self.porshn_hermey_var1, values=lst_hermey, state='readonly')
        self.porshn_hermey1.grid(row=1, column=1, padx=10, pady=9)

        self.hm_mm1 = Label(self.iki_tarap, text='mm', font=('Arial', 12))
        self.hm_mm1.grid(row=1, column=2, sticky='w')

        self.diam_st1 = Label(self.iki_tarap, text='ştok Ø', font=('Arial', 14))
        self.diam_st1.grid(row=2, column=0, sticky='e')

        self.diam_st_var1 = IntVar(value=lst_stok[0])
        self.diam_stok1 = Combobox(self.iki_tarap, width=5, textvariable=self.diam_st_var1, values=lst_stok, state='readonly')
        self.diam_stok1.grid(row=2, column=1, padx=10, pady=9)

        self.st_mm1 = Label(self.iki_tarap, text='mm', font=('Arial', 12))
        self.st_mm1.grid(row=2, column=2, sticky='w')

        self.her_porshn1 = Label(self.iki_tarap, text='min/hereket', font=('Arial', 14))
        self.her_porshn1.grid(row=3, column=0, sticky='e')

        self.porshn_minher_var1 = IntVar(value=lst_minher[0])
        self.porshn_minher1 = Combobox(self.iki_tarap, width=5, textvariable=self.porshn_minher_var1, values=lst_minher, state='readonly')
        self.porshn_minher1.grid(row=3, column=1, padx=10, pady=9)

        self.mh1 = Label(self.iki_tarap, text='san', font=('Arial', 12))
        self.mh1.grid(row=3, column=2, sticky='w')

        self.porshn_sany1 = Label(self.iki_tarap, text='porşun sany', font=('Arial', 14))
        self.porshn_sany1.grid(row=4, column=0, sticky='e')

        self.porshn_sany_var1 = IntVar(value=lst_sany[0])
        self.porshn_sany_combo1 = Combobox(self.iki_tarap, width=5, textvariable=self.porshn_sany_var1, values=lst_sany, state='readonly')
        self.porshn_sany_combo1.grid(row=4, column=1, padx=10, pady=10)

        self.ps1 = Label(self.iki_tarap, text='san', font=('Arial', 12))
        self.ps1.grid(row=4, column=2, sticky='w')

        self.lbl_ls1 = Label(self.iki_tarap, text='l/s', font=('Arial', 14))
        self.lbl_ls1.grid(row=0, column=3, sticky='s')

        self.ent_ls1 = Entry(self.iki_tarap, width=7, font=('Arial', 12))
        self.ent_ls1.grid(row=1, column=3, padx=15, sticky='n')

        self.lbl_ksag1 = Label(self.iki_tarap, text='m³/sag', font=('Arial', 14))
        self.lbl_ksag1.grid(row=2, column=3, sticky='s')

        self.ent_ksag1 = Entry(self.iki_tarap, width=7, font=('Arial', 12))
        self.ent_ksag1.grid(row=3, column=3, padx=15, sticky='n')


win = Window(themename='morph')
win.geometry('693x480+640+200')
# win.state('zoomed')
win.title('BUR-INFO')
win.resizable(False, False)

notebook = Notebook()
notebook.pack(expand=True, fill=BOTH)

frame1 = BurParametr(notebook)
frame2 = NasosParametr(notebook)
frame3 = Frame(notebook)

frame3.pack(fill=BOTH, expand=True)

notebook.add(frame1, text="Bur parametr")
notebook.add(frame2, text="Nasos parametr")
notebook.add(frame3, text="Programma barada")

# -------------------------------------------  text Programma barada   ---------------------------------------------

mglmt = '''         Salam BUR-INFO programmasyny ulanyjylar!, men programmanyň awtory 
Kemal Haladow, bu programmany düzmegimiň sebäbi, men 2 ýyl bäri " Python " 
programirleme dilini öwrenip gelýan we tejribämi barlap gormek üçin şu 
programmany düzdim, bu "Beta" versia ýagny barlag (test) versiasy. Bu programma 
nebitgaz guýularyny burawlamak işlerinde gazylýan guýynyn göwrümi, çuňlugy, 
burawlaýjy turbalaryň agramy, buraw ergininiň göwrümi we nasos ödürijiligi
barada hasap çykaryar. 
        Meniň ulanyjylara haýyşym şu programmany ulanyp görüp, programmanyň
kemçiligi barada, ýa bolmasa ýenede programma goşmaly zat bolsa, düzetmeli 
ýeri bar bolsa, meniň elektron poçtama hat üsti bilen maglumat berseňiz, hem 
maslahat berseňiz menem gelen maglumatlara görä programmany hasda giňişleýin 
maglumat hasaplaýan programma öwürsem sizden minnetdar bolaryn.

meniň elektron poçtam: haladowkemal@gmail.com 




                                                                                                               versia 1.0
 '''

text_magmt = Text(frame3, font=('Times new roman', 15), wrap='word')
text_magmt.pack(fill=BOTH)
text_magmt.insert(END, mglmt)
text_magmt.config(state=DISABLED, fg='black')

win.mainloop()
