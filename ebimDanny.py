from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3


# ======================== Database Defination Code ==========================

# tablisa doretmek
def creat_table():

	con = sqlite3.connect("BazaDanny_EBIM.db")
	cur = con.cursor()
	cur.execute('''CREATE TABLE IF NOT EXISTS Isgar_Sanaw
						(
							TabN INTEGER PRIMARY KEY,
							Familya TEXT,
							Ady TEXT,
							Wezipe TEXT,
							Dereje CHAR,
							Bilimi TEXT,
							Is_Yeri CHAR,
							Doglan_Wagty CHAR
						)
					''')
	con.commit()
	con.close()

# tablisadan saylamak
def fetch_rows():

	con = sqlite3.connect("BazaDanny_EBIM.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM Isgar_Sanaw")
	rows = cur.fetchall()
	con.close()
	return rows

# tablisa setr gosmak
def insert_row(tabel, famil, ady, wezipe, dereje, bilimi, is_yeri, doglan_wagty):

	con = sqlite3.connect("BazaDanny_EBIM.db")
	cur = con.cursor()
	cur.execute('''INSERT INTO Isgar_Sanaw
						(
							TabN,
							Familya,
							Ady,
							Wezipe,
							Dereje,
							Bilimi,
							Is_Yeri,
							Doglan_Wagty
						) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (tabel, famil, ady, wezipe, dereje, bilimi, is_yeri, doglan_wagty))
	con.commit()
	con.close()

# tablisadan setr pozmak
def delete_rows(tabel):

	con = sqlite3.connect("BazaDanny_EBIM.db")
	cur = con.cursor()
	cur.execute("DELETE FROM Isgar_Sanaw WHERE TabN = ?", (tabel,))
	con.commit()
	con.close()

# tablisadan setr uytgetmek
def update_rows(new_famil, new_ady, new_wezipe, new_dereje, new_bilimi, new_is_yeri, new_doglan_wagty, tabel):

	con = sqlite3.connect("BazaDanny_EBIM.db")
	cur = con.cursor()
	cur.execute("UPDATE Isgar_Sanaw SET Familya=?, Ady=?, Wezipe=?, Dereje=?, Bilimi=?, Is_Yeri=?, Doglan_Wagty=? WHERE TabN = ?",
		(new_famil, new_ady, new_wezipe, new_dereje, new_bilimi, new_is_yeri, new_doglan_wagty, tabel))
	con.commit()
	con.close()

# id exists
def id_exists(tabel):

	con = sqlite3.connect("BazaDanny_EBIM.db")
	cur = con.cursor()
	cur.execute("SELECT COUNT(*) FROM Isgar_Sanaw WHERE TabN = ?", (tabel,))
	result = cur.fetchone()
	con.close()
	return result[0] > 0

creat_table()

# ======================== Create GUI Code ==========================

root = Tk()
root.title("EekeremBIM işgär sanaw")
root.geometry("1000x700")
root.resizable(False, False)
root.configure(background="#f2e36f")

style = ttk.Style()
style.theme_use("default")
style.configure("Treeview.Heading", font=("Times", 16), background="#595de3", foreground="#f2f7f7", fieldbackground="#ffffff")
style.configure("Treeview", font=("Times", 14), background="#ffffff", foreground="black", rowheight=30, fieldbackground="#hfhfhf")

style.map("Treeview", background=[('selected', '#18d97f')])
style.map("Treeview.Heading", background=[('focus', '#65f046')])


class widget_frame(Frame):
    def __init__(self, master):
        super(widget_frame, self).__init__(master)
        self.pack(fill=BOTH, pady=5, padx=5)
        self.configure(background="#f2e36f")

        self.my_menu = Menu(self)
        root.config(menu=self.my_menu)

        self.search_menu = Menu(self.my_menu, tearoff=0, font=("Times", 14))
        self.my_menu.add_cascade(label="Gozleg", menu=self.search_menu)
        self.search_menu.add_separator()
        self.search_menu.add_command(label="Tabel №, boýunça", command=self.tabel_search)
        self.search_menu.add_separator()
        self.search_menu.add_command(label="Familiýa, boýunça", command=self.famil_search)
        self.search_menu.add_separator()
        self.search_menu.add_command(label="Ady, boýunça", command=self.ady_search)
        self.search_menu.add_separator()
        self.search_menu.add_command(label="Wezipe, boýunça", command=self.wezipe_search)
        self.search_menu.add_separator()
        self.search_menu.add_command(label="Dereje, boýunça", command=self.dereje_search)
        self.search_menu.add_separator()
        self.search_menu.add_command(label="Bilimi, boýunça", command=self.bilimi_search)
        self.search_menu.add_separator()
        self.search_menu.add_command(label="Iş ýeri, boýunça", command=self.isyeri_search)
        self.search_menu.add_separator()
        self.search_menu.add_command(label="Doglan wagty, boýunça", command=self.doglanwagty_search)
        self.search_menu.add_separator()

        style = ttk.Style()
        style.configure("TLabelframe", font=("Times", 14), background="#6df7a7", foreground="#101036")
        style.configure("TLabelframe.Label", font=("Times", 16), background="#6df7a7", foreground="#101036")
        style.configure("TLabel", font=("Times", 14), background="#6df7a7", foreground="#101036")

        style.configure("TButton", font=("Times", 14), background="#595de3", foreground="#f2f3f7")
        style.map("TButton", background=[('active', "#595de3")], foreground=[('active', '!disabled', "#f2f3f7")])


        self.create_tree()
        self.data_widgets()
        self.button_widgets()
        self.add_to_tree()
        self.my_tree.bind('<<TreeviewSelect>>', self.display_data)

# ====================  search menu commands  ========================
    def query_tabel(self):
        look_record = search_entry_tabel.get()
        persons = fetch_rows()
        self.my_tree.delete(*self.my_tree.get_children())

        con = sqlite3.connect("BazaDanny_EBIM.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM Isgar_Sanaw WHERE TabN=?", (look_record,))
        rows = cur.fetchall()

        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#adeff0")

        global count
        count = 0

        for person in rows:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("oddrow",))
            count += 1

        self.sch['text'] = count

        con.commit()
        con.close()

        search_tabel_top.destroy()

    def query_famil(self):
        look_record = search_entry_famil.get()
        persons = fetch_rows()
        self.my_tree.delete(*self.my_tree.get_children())

        con = sqlite3.connect("BazaDanny_EBIM.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM Isgar_Sanaw WHERE Familya like ?", (look_record,))
        rows = cur.fetchall()

        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#adeff0")

        global count
        count = 0

        for person in rows:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("oddrow",))
            count += 1

        self.sch['text'] = count

        con.commit()
        con.close()

        search_famil_top.destroy()

    def query_ady(self):
        look_record = search_entry_ady.get()
        persons = fetch_rows()
        self.my_tree.delete(*self.my_tree.get_children())

        con = sqlite3.connect("BazaDanny_EBIM.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM Isgar_Sanaw WHERE Ady like ?", (look_record,))
        rows = cur.fetchall()

        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#adeff0")

        global count
        count = 0

        for person in rows:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("oddrow",))
            count += 1

        self.sch['text'] = count

        con.commit()
        con.close()

        search_ady_top.destroy()

    def query_wezipe(self):
        look_record = search_entry_wezipe.get()
        persons = fetch_rows()
        self.my_tree.delete(*self.my_tree.get_children())

        con = sqlite3.connect("BazaDanny_EBIM.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM Isgar_Sanaw WHERE Wezipe like ?", (look_record,))
        rows = cur.fetchall()

        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#adeff0")

        global count
        count = 0

        for person in rows:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("oddrow",))
            count += 1

        self.sch['text'] = count

        con.commit()
        con.close()

        search_wezipe_top.destroy()

    def query_dereje(self):
        look_record = search_entry_dereje.get()
        persons = fetch_rows()
        self.my_tree.delete(*self.my_tree.get_children())

        con = sqlite3.connect("BazaDanny_EBIM.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM Isgar_Sanaw WHERE Dereje like ?", (look_record,))
        rows = cur.fetchall()

        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#adeff0")

        global count
        count = 0

        for person in rows:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("oddrow",))
            count += 1

        self.sch['text'] = count
        
        con.commit()
        con.close()

        search_dereje_top.destroy()

    def query_bilimi(self):
        look_record = search_entry_bilimi.get()
        persons = fetch_rows()
        self.my_tree.delete(*self.my_tree.get_children())

        con = sqlite3.connect("BazaDanny_EBIM.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM Isgar_Sanaw WHERE Bilimi like ?", (look_record,))
        rows = cur.fetchall()

        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#adeff0")

        global count
        count = 0

        for person in rows:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("oddrow",))
            count += 1

        self.sch['text'] = count

        con.commit()
        con.close()

        search_bilimi_top.destroy()

    def query_isyeri(self):
        look_record = "".join(search_entry_isyeri.get())
        persons = fetch_rows()
        self.my_tree.delete(*self.my_tree.get_children())

        con = sqlite3.connect("BazaDanny_EBIM.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM Isgar_Sanaw WHERE Is_Yeri like ?", (look_record,))
        rows = cur.fetchall()

        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#adeff0")

        global count
        count = 0

        for person in rows:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("oddrow",))
            count += 1

        self.sch['text'] = count

        con.commit()
        con.close()

        search_isyeri_top.destroy()

    def query_doglanwagty(self):
        look_record = search_entry_doglanwagty.get()
        persons = fetch_rows()
        self.my_tree.delete(*self.my_tree.get_children())

        con = sqlite3.connect("BazaDanny_EBIM.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM Isgar_Sanaw WHERE Doglan_Wagty like ?", (look_record,))
        rows = cur.fetchall()

        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#adeff0")

        global count
        count = 0

        for person in rows:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("oddrow",))
            count += 1

        self.sch['text'] = count

        con.commit()
        con.close()

        search_doglanwagty_top.destroy()
# ===============================  Create Toplevel widget ============================
    def tabel_search(self):
        global search_entry_tabel, search_tabel_top
        search_tabel_top = Toplevel(root)
        search_tabel_top.title("Tabel №, boýunça gözle")
        search_tabel_top.geometry("300x150")

        search_entry_tabel = ttk.Entry(search_tabel_top, font=("Times", 16), width=18)
        search_entry_tabel.pack(pady=20)

        search_btn = ttk.Button(search_tabel_top, text="Gözle", command=self.query_tabel)
        search_btn.pack(pady=10)

    def famil_search(self):
        global search_entry_famil, search_famil_top
        search_famil_top = Toplevel(root)
        search_famil_top.title("Familiýa, boýunça gözle")
        search_famil_top.geometry("300x150")

        search_entry_famil = ttk.Entry(search_famil_top, font=("Times", 16), width=18)
        search_entry_famil.pack(pady=20)

        search_btn = ttk.Button(search_famil_top, text="Gözle", command=self.query_famil)
        search_btn.pack(pady=10)

    def ady_search(self):
        global search_entry_ady, search_ady_top
        search_ady_top = Toplevel(root)
        search_ady_top.title("Ady, boýunça gözle")
        search_ady_top.geometry("300x150")

        search_entry_ady = ttk.Entry(search_ady_top, font=("Times", 16), width=18)
        search_entry_ady.pack(pady=20)

        search_btn = ttk.Button(search_ady_top, text="Gözle", command=self.query_ady)
        search_btn.pack(pady=10)

    def wezipe_search(self):
        global search_entry_wezipe, search_wezipe_top
        search_wezipe_top = Toplevel(root)
        search_wezipe_top.title("Wezipe, boýunça gözle")
        search_wezipe_top.geometry("300x150")

        search_entry_wezipe = ttk.Entry(search_wezipe_top, font=("Times", 16), width=18)
        search_entry_wezipe.pack(pady=20)

        search_btn = ttk.Button(search_wezipe_top, text="Gözle", command=self.query_wezipe)
        search_btn.pack(pady=10)

    def dereje_search(self):
        global search_entry_dereje, search_dereje_top
        search_dereje_top = Toplevel(root)
        search_dereje_top.title("Dereje, boýunça gözle")
        search_dereje_top.geometry("300x150")

        search_entry_dereje = ttk.Entry(search_dereje_top, font=("Times", 16), width=18)
        search_entry_dereje.pack(pady=20)

        search_btn = ttk.Button(search_dereje_top, text="Gözle", command=self.query_dereje)
        search_btn.pack(pady=10)

    def bilimi_search(self):
        global search_entry_bilimi, search_bilimi_top
        search_bilimi_top = Toplevel(root)
        search_bilimi_top.title("Bilimi, boýunça gözle")
        search_bilimi_top.geometry("300x150")

        search_entry_bilimi = ttk.Entry(search_bilimi_top, font=("Times", 16), width=18)
        search_entry_bilimi.pack(pady=20)

        search_btn = ttk.Button(search_bilimi_top, text="Gözle", command=self.query_bilimi)
        search_btn.pack(pady=10)

    def isyeri_search(self):
        global search_entry_isyeri, search_isyeri_top
        search_isyeri_top = Toplevel(root)
        search_isyeri_top.title("Iş ýeri, boýunça gözle")
        search_isyeri_top.geometry("300x150")

        search_entry_isyeri = ttk.Entry(search_isyeri_top, font=("Times", 16), width=18)
        search_entry_isyeri.pack(pady=20)

        search_btn = ttk.Button(search_isyeri_top, text="Gözle", command=self.query_isyeri)
        search_btn.pack(pady=10)

    def doglanwagty_search(self):
        global search_entry_doglanwagty, search_doglanwagty_top
        search_doglanwagty_top = Toplevel(root)
        search_doglanwagty_top.title("Doglan wagty, boýunça gözle")
        search_doglanwagty_top.geometry("300x150")

        search_entry_doglanwagty = ttk.Entry(search_doglanwagty_top, font=("Times", 16), width=18)
        search_entry_doglanwagty.pack(pady=20)

        search_btn = ttk.Button(search_doglanwagty_top, text="Gözle", command=self.query_doglanwagty)
        search_btn.pack(pady=10)

# ================================== Button Commands ==================================
    def query_database(self):
        persons = fetch_rows()
        self.my_tree.delete(*self.my_tree.get_children())

        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#adeff0")

        global count
        count = 0

        for person in persons:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("oddrow",))
            count += 1
            
        self.sch['text'] = '0'
        self.sct['text'] = '0'


    def add_to_tree(self):
        add_persons = fetch_rows()
        self.my_tree.delete(*self.my_tree.get_children())

        self.my_tree.tag_configure("oddrow", background="white")
        self.my_tree.tag_configure("evenrow", background="#adeff0")

        global count
        count = 0

        for person in add_persons:
            if count % 2 == 0:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("evenrow",))
            else:
                self.my_tree.insert(parent='', index=END, iid=count, text="", values=(
                    person[0], person[1], person[2], person[3], person[4], person[5], person[6], person[7]),
                                    tags=("oddrow",))
            count += 1

        ttk.Label(self.button_labelFrame, text="  Sanawda jemi adam sany: ").grid(row=1, column=0, pady=10)

        self.all_cnt = ttk.Label(self.button_labelFrame)
        self.all_cnt.grid(row=1, column=1, pady=10, sticky=W)
        self.all_cnt['text'] = count       

        ttk.Label(self.button_labelFrame, text='   |   ').grid(row=1, column=2, pady=10)

        ttk.Label(self.button_labelFrame, text="Gözlenen setr sany: ").grid(row=1, column=3, pady=10)

        self.sch = ttk.Label(self.button_labelFrame, text='0')
        self.sch.grid(row=1, column=4, pady=10, sticky=W)

        ttk.Label(self.button_labelFrame, text='   |   ').grid(row=1, column=5, pady=10)

        ttk.Label(self.button_labelFrame, text=f"Sanawdan saýlanan setr sany: ").grid(row=1, column=6, pady=10)

        self.sct = ttk.Label(self.button_labelFrame, text="0")
        self.sct.grid(row=1, column=7, pady=10, sticky=W)


    def clear(self, *clicked):
        if clicked:
            self.my_tree.selection_remove(self.my_tree.selection())
        self.tabel_ent.delete(0, END)
        self.familya_ent.delete(0, END)
        self.ady_ent.delete(0, END)
        self.wezipe_ent.delete(0, END)
        self.dereje_ent.delete(0, END)
        self.bilimi_ent.delete(0, END)
        self.doglanwagty_ent.delete(0, END)
        self.isyeri_ent.delete(0, END)

        self.sct['text'] = '0'
        

    def display_data(self, event):
        try:
            selected_item = self.my_tree.selection()
            if selected_item:
                row = self.my_tree.item(selected_item)['values']
                self.clear()
                self.tabel_ent.insert(0, row[0])
                self.familya_ent.insert(0, row[1])
                self.ady_ent.insert(0, row[2])
                self.wezipe_ent.insert(0, row[3])
                self.dereje_ent.insert(0, row[4])
                self.bilimi_ent.insert(0, row[5])
                self.isyeri_ent.insert(0, row[6])
                self.doglanwagty_ent.insert(0, row[7])
            else:
                pass
        except:
            count_select = len(selected_item)
            self.sct['text'] = count_select
            

    def delete(self):
        selected_item = self.my_tree.selection()
        if not selected_item:
            tkinter.messagebox.showwarning('Üns ber!', 'Pozmak üçin setr saýla.')
        else:
            response = tkinter.messagebox.askyesno("Tassykla", "Yazgyny pozmak üçin tassykla.")
            if response == 1:
                tabel = self.tabel_ent.get()
                delete_rows(tabel)
                self.add_to_tree()
                self.clear()
                tkinter.messagebox.showinfo('Ok', 'Saýlanan setr pozuldy.')

    def update(self):
        selected_item = self.my_tree.selection()
        if not selected_item:
            tkinter.messagebox.showwarning('Üns ber!', 'Üýtgetmek üçin setr saýla.')
        else:
            self.tabel = self.tabel_ent.get()
            self.famil = self.familya_ent.get()
            self.ady = self.ady_ent.get()
            self.wezipe = self.wezipe_ent.get()
            self.dereje = self.dereje_ent.get()
            self.bilimi = self.bilimi_ent.get()
            self.is_yeri = self.isyeri_ent.get()
            self.doglan_wagty = self.doglanwagty_ent.get()
            update_rows(self.famil, self.ady, self.wezipe, self.dereje, self.bilimi, self.is_yeri, self.doglan_wagty, self.tabel)
            self.add_to_tree()
            self.clear()
            tkinter.messagebox.showinfo('Ok', 'Saýlanan ýazgy üýtgedildi.')

    def insert(self):
        try:
            self.tabel = self.tabel_ent.get()
            self.famil = self.familya_ent.get()
            self.ady = self.ady_ent.get()
            self.wezipe = self.wezipe_ent.get()
            self.dereje = self.dereje_ent.get()
            self.bilimi = self.bilimi_ent.get()
            self.is_yeri = self.isyeri_ent.get()
            self.doglan_wagty = self.doglanwagty_ent.get()
            if not (
                    self.tabel and self.famil and self.ady and self.wezipe and self.dereje and self.bilimi and self.is_yeri and self.doglan_wagty):
                tkinter.messagebox.showwarning('Üns ber!', 'Maglumat yok.')
            elif id_exists(self.tabel):
                tkinter.messagebox.showerror('Yalňyş', f'Tabel № {self.tabel} öň bar')
            else:
                insert_row(self.tabel, self.famil, self.ady, self.wezipe, self.dereje, self.bilimi, self.is_yeri, self.doglan_wagty)
                self.add_to_tree()
                tkinter.messagebox.showinfo('Ok', 'Täze setir goşuldy')
        except:
            self.tabel_ent.delete(0, END)
            self.familya_ent.delete(0, END)
            self.ady_ent.delete(0, END)
            self.wezipe_ent.delete(0, END)
            self.dereje_ent.delete(0, END)
            self.bilimi_ent.delete(0, END)
            self.isyeri_ent.delete(0, END)
            self.doglanwagty_ent.delete(0, END)

    def create_tree(self):
        self.tree_frame = ttk.Frame(self)
        self.tree_frame.pack(fill=BOTH, expand=True, pady=5)

        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)

        self.my_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set, height=13, selectmode="extended")
        self.my_tree.pack(fill=X)

        self.tree_scroll.config(command=self.my_tree.yview)

        self.my_tree["columns"] = ("#1", "#2", "#3", "#4", "#5", "#6", "#7", "#8")
        self.my_tree.column("#0", width=0, minwidth=0,)
        self.my_tree.column("#1", anchor=CENTER, width=60, minwidth=60, stretch=NO)
        self.my_tree.column("#2", anchor=W, width=150, minwidth=150)
        self.my_tree.column("#3", anchor=W, width=130, minwidth=130)
        self.my_tree.column("#4", anchor=W, width=150, minwidth=150)
        self.my_tree.column("#5", anchor=CENTER, width=80, minwidth=80)
        self.my_tree.column("#6", anchor=W, width=100, minwidth=100)
        self.my_tree.column("#7", anchor=W, width=160, minwidth=175)
        self.my_tree.column("#8", anchor=CENTER, width=130, minwidth=130)

        self.my_tree.heading("#0", text="", anchor=W)
        self.my_tree.heading("#1", text="Tab №", anchor=CENTER)
        self.my_tree.heading("#2", text="Familiýa", anchor=CENTER)
        self.my_tree.heading("#3", text="Ady", anchor=CENTER)
        self.my_tree.heading("#4", text="Wezipe", anchor=CENTER)
        self.my_tree.heading("#5", text="Dereje", anchor=CENTER)
        self.my_tree.heading("#6", text="Bilimi", anchor=CENTER)
        self.my_tree.heading("#7", text="Iş ýeri", anchor=CENTER)
        self.my_tree.heading("#8", text="Doglan wagty", anchor=CENTER)

# ================================ Create widgets ============================
    def data_widgets(self):
        self.data_labeFrame = ttk.LabelFrame(self)
        self.data_labeFrame.config(text="Ýazgy meýdany")
        self.data_labeFrame.pack(fill=BOTH, expand=True, pady=5)

        self.tabel_lbl = ttk.Label(self.data_labeFrame, text="Tab №:")
        self.tabel_lbl.grid(row=0, column=0, padx=5, pady=10, sticky=W)
        self.tabel_ent = ttk.Entry(self.data_labeFrame, font=("Times", 16), width=6)
        self.tabel_ent.grid(row=0, column=1, padx=5, pady=10)

        self.familya_lbl = ttk.Label(self.data_labeFrame, text="Familiýa:")
        self.familya_lbl.grid(row=0, column=2, padx=5, pady=10, sticky=W)
        self.familya_ent = ttk.Entry(self.data_labeFrame, font=("Times", 16), width=17)
        self.familya_ent.grid(row=0, column=3, padx=5, pady=10)

        self.ady_lbl = ttk.Label(self.data_labeFrame, text="Ady:")
        self.ady_lbl.grid(row=1, column=2, padx=5, pady=10, sticky=W)
        self.ady_ent = ttk.Entry(self.data_labeFrame, font=("Times", 16), width=17)
        self.ady_ent.grid(row=1, column=3, padx=5, pady=10)

        self.dereje_lbl = ttk.Label(self.data_labeFrame, text="Dereje:")
        self.dereje_lbl.grid(row=1, column=0, padx=5, pady=10, sticky=W)
        self.dereje_ent = ttk.Entry(self.data_labeFrame, font=("Times", 16), width=6)
        self.dereje_ent.grid(row=1, column=1, padx=5, pady=10)

        self.wezipe_lbl = ttk.Label(self.data_labeFrame, text="Wezipe:")
        self.wezipe_lbl.grid(row=0, column=4, padx=5, pady=10, sticky=W)
        self.wezipe_ent = ttk.Entry(self.data_labeFrame, font=("Times", 16), width=18)
        self.wezipe_ent.grid(row=0, column=5, padx=5, pady=10)

        self.bilimi_lbl = ttk.Label(self.data_labeFrame, text="Bilimi:")
        self.bilimi_lbl.grid(row=0, column=6, padx=5, pady=10, sticky=W)
        self.bilimi_ent = ttk.Entry(self.data_labeFrame, font=("Times", 16), width=12)
        self.bilimi_ent.grid(row=0, column=7, padx=8, pady=10)

        self.isyeri_lbl = ttk.Label(self.data_labeFrame, text="Iş ýeri:")
        self.isyeri_lbl.grid(row=1, column=4, padx=5, pady=10, sticky=W)
        self.isyeri_ent = ttk.Entry(self.data_labeFrame, font=("Times", 16), width=18)
        self.isyeri_ent.grid(row=1, column=5, padx=5, pady=10)

        self.doglanwagty_lbl = ttk.Label(self.data_labeFrame, text="Doglan wagty:")
        self.doglanwagty_lbl.grid(row=1, column=6, padx=5, pady=10, sticky=W)
        self.doglanwagty_ent = ttk.Entry(self.data_labeFrame, font=("Times", 16), width=12)
        self.doglanwagty_ent.grid(row=1, column=7, padx=5, pady=10)

    def button_widgets(self):
        self.button_labelFrame = ttk.LabelFrame(self)
        self.button_labelFrame.config(text="Işjen meýdany")
        self.button_labelFrame.pack(fill=BOTH, expand=True, pady=5)

        self.frame = Frame(self.button_labelFrame, background="#6df7a7")
        self.frame.grid(row=0, column=0, columnspan=8)

        self.add_btn = ttk.Button(self.frame, text="Ýazgyny goş", command=self.insert)
        self.add_btn.grid(row=0, column=0, padx=15, pady=10)

        self.update_btn = ttk.Button(self.frame, text="Ýazgyny täzele", command=self.update)
        self.update_btn.grid(row=0, column=1, padx=15, pady=10)

        self.clear_btn = ttk.Button(self.frame, text="Arassala", command=lambda:self.clear(True))
        self.clear_btn.grid(row=0, column=2, padx=15, pady=10)

        self.delete_btn = ttk.Button(self.frame, text="Ýazgyny poz", command=self.delete)
        self.delete_btn.grid(row=0, column=3, padx=15, pady=10)

        self.reset_btn = ttk.Button(self.frame, text="Täzele", command=self.query_database)
        self.reset_btn.grid(row=0, column=4, padx=15, pady=10)


widget_frame(root)

root.mainloop()
