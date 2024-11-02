from tkinter import *
from tkinter import ttk
import customtkinter as ctk
import sqlite3
import tkcalendar
from bidi.algorithm import get_display
from arabic_reshaper import reshape

date_pattern = 'dd-MM-yyyy'
pir_arabic3 = (["تأمين صحى", "شركات", "سداد نقدى"])
pir_display3 = [get_display(reshape(search)) for search in pir_arabic3]


class counter_by:
    def __init__(self, lab_code):
        self.lab = lab_code
        self.count_app = ctk.CTk()
        self.count_app.title(reshape("اضافة جلسات"))
        self.count_app.geometry("500x500")
        self.count_app.resizable(False, False)
        frm1 = ctk.CTkFrame(self.count_app, width=490, height=480, fg_color="silver", border_color="black",
                            border_width=2)
        frm1.place(x=5, y=10)
        lab_pir = ctk.CTkLabel(frm1, text=get_display(reshape("نوع التعاقد")), font=("arial", 14, "bold"), width=115,
                               height=30, fg_color="#D2B56E", corner_radius=10)
        lab_pir.place(x=250, y=10)
        lab_count = ctk.CTkLabel(frm1, text=get_display(reshape("كمية الجلسات")), font=("arial", 14, "bold"), width=100,
                                 height=30, fg_color="#D2B56E", corner_radius=10)
        lab_count.place(x=250, y=50)
        lab_date = ctk.CTkLabel(frm1, text=get_display(reshape("تاريخ الجلسات")), font=("arial", 14, "bold"), width=100,
                                height=30, fg_color="#D2B56E", corner_radius=10)
        lab_date.place(x=250, y=90)
        lab_reset = ctk.CTkLabel(frm1, text=get_display(reshape("رقم الايصال")), font=("arial", 14, "bold"), width=115,
                               height=30, fg_color="#D2B56E", corner_radius=10)
        lab_reset.place(x=250, y=130)
        lab_money = ctk.CTkLabel(frm1, text=get_display(reshape("المبلغ")), font=("arial", 14, "bold"), width=115,
                                 height=30, fg_color="#D2B56E", corner_radius=10)
        lab_money.place(x=250, y=170)
        self.pir_ent = ttk.Combobox(frm1, font=("arial", 10, "bold"), values=pir_display3, state="readonly")
        self.pir_ent.place(x=110, y=10, width=140, height=30)
        self.count_ent = Entry(frm1, font=("arial", 12, "bold"), justify="center")
        self.count_ent.place(x=110, y=50, width=140, height=30)
        self.date_ent = tkcalendar.DateEntry(frm1, date_pattern=date_pattern, font=("arial", 12, "bold"),
                                             state="readonly")
        self.date_ent.place(x=110, y=90, width=140, height=30)
        self.reset_ent = Entry(frm1, font=("arial", 12, "bold"), justify="center")
        self.reset_ent.place(x=110, y=130, width=140, height=30)
        self.money_ent = Entry(frm1, font=("arial", 12, "bold"), justify="center")
        self.money_ent.place(x=110, y=170, width=140, height=30)
        self.table_count = ttk.Treeview(frm1)
        self.table_count.place(x=10, y=210, width=470, height=220)
        self.table_count['columns'] = ["pir", "count", "date", "money", "reset"]
        self.table_count.column("#0", width=0, stretch=NO)
        self.table_count.column("pir", width=80)
        self.table_count.column("count", width=80)
        self.table_count.column("date", width=110)
        self.table_count.column("money", width=80)
        self.table_count.column("reset", width=80)
        self.table_count.heading("pir", text=get_display(reshape("التعاقد")))
        self.table_count.heading("count", text=get_display(reshape("الجلسات")))
        self.table_count.heading("date", text=get_display(reshape("التاريخ")))
        self.table_count.heading("money", text=get_display(reshape("المبلغ")))
        self.table_count.heading("reset", text=get_display(reshape("الايصال")))
        btn_add_set = ctk.CTkButton(frm1, text=get_display(reshape("اضافة")), fg_color="#2D5081",
                                    font=("arial", 14, "bold"), width=80, height=35, corner_radius=10,
                                    command=self.btn_add_)
        btn_add_set.place(x=10, y=440)
        btn_del_set = ctk.CTkButton(frm1, text=get_display(reshape("حذف")), fg_color="#971010",
                                    font=("arial", 14, "bold"), width=80, height=35, corner_radius=10,
                                    command=self.btn_del_)
        btn_del_set.place(x=400, y=440)
        self.add_data_set()
        self.table_info_set()

    def add_data_set(self):
        con = sqlite3.connect("data_base.db")
        cur = con.cursor()
        cur.execute(
            f"CREATE TABLE IF NOT EXISTS {'counter_' + self.lab} (pir text, count text, date text, "
            f" money text , reset text ,num text)")
        con.commit()
        con.close()

    def table_info_set(self):
        self.table_count.delete(*self.table_count.get_children())
        con = sqlite3.connect("data_base.db")
        cur = con.cursor()
        cur.execute(f"select * from {'counter_' + self.lab} ")
        all_sets = cur.fetchall()

        for i, sets in enumerate(all_sets):
            # تحويل البيانات النصية باللغة العربية باستثناء البيان رقم 5و3
            set_arabic = [get_display(reshape(str(value))) if i != 0  else str(value) for i, value in
                          enumerate(sets)]
            self.table_count.insert("", END, values=set_arabic)
        con.commit()
        con.close()

    def btn_add_(self):
        if self.pir_ent.get() == "" or self.count_ent.get() == "":
            return
        elif not self.count_ent.get().isdigit():
            return
        elif self.pir_ent.get() == "ﻯﺪﻘﻧ ﺩﺍﺪﺳ":
            if self.money_ent.get() == "" or self.reset_ent.get() == "" or not self.reset_ent.get().isdigit() or not self.money_ent.get().replace('.', '', 1).isdigit():
                return
            else:
                con = sqlite3.connect("data_base.db")
                cur = con.cursor()
                cur.execute(
                    f"SELECT MAX(CAST(num AS INTEGER)) FROM {'counter_' + self.lab} ")
                unit = cur.fetchone()
                if unit[0] == None:
                    num = 1
                else:
                    num = 1 + int(unit[0])
                cur.execute(
                    f"insert into {'counter_' + self.lab} (pir , count , date  , money  , reset ,num)values ('{self.pir_ent.get()}', '{self.count_ent.get()}', '{self.date_ent.get()}','{self.money_ent.get()}','{self.reset_ent.get()}','{num}')")
                con.commit()
                con.close()
                self.pir_ent.set("")
                self.count_ent.delete(0, END)
                self.date_ent.delete(0, END)
                self.money_ent.delete(0, END)
                self.reset_ent.delete(0, END)
                self.table_info_set()
        else:
            con = sqlite3.connect("data_base.db")
            cur = con.cursor()
            cur.execute(
                f"SELECT MAX(CAST(num AS INTEGER)) FROM {'counter_' + self.lab} ")
            unit = cur.fetchone()
            if unit[0] == None:
                num = 1
            else:
                num = 1 + int(unit[0])
            cur.execute(
                f"insert into {'counter_' + self.lab} (pir , count , date  , money  , reset ,num)values ('{self.pir_ent.get()}', '{self.count_ent.get()}', '{self.date_ent.get()}','_','_','{num}')")
            con.commit()
            con.close()
            self.pir_ent.set("")
            self.count_ent.delete(0, END)
            self.date_ent.delete(0, END)
            self.money_ent.delete(0, END)
            self.reset_ent.delete(0, END)
            self.table_info_set()

    def btn_del_(self):
        if self.table_count.selection():
            del_patients = self.table_count.selection()
            for patient_d in del_patients:
                values = self.table_count.item(patient_d, 'values')
                con = sqlite3.connect("data_base.db")
                cur = con.cursor()
                num = values[5]
                cur.execute(f"DELETE FROM {'counter_' + self.lab} WHERE num='{str(num)}' ")
                con.commit()
                con.close()
                self.pir_ent.set("")
                self.count_ent.delete(0, END)
                self.date_ent.delete(0, END)
                self.table_info_set()
                return self.table_count.selection()
        else:
            return

    def run_count(self):
        self.count_app.mainloop()


if __name__ == '__main__':
    app = counter_by(lab_code="")
    app.run_count()
