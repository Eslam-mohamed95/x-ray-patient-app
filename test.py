from tkinter import *
from tkinter import ttk
import counter_sets
import customtkinter as ctk
import sqlite3
import tkcalendar
from bidi.algorithm import get_display
from arabic_reshaper import reshape

unit_num = 1
date_pattern = 'dd-MM-yyyy'


class access:
    def __init__(self, kind, name, person , code):
        self.lab_cotishan = None
        self.lab_time = None
        self.time_ent_h = None
        self.time_ent_m = None

        self.Third_window_closed = False
        self.sets_dd = None
        self.mane = name
        self.person = person
        self.cod = code
        self.kind = kind
        self.count = 0
        ctk.set_appearance_mode("light")
        self.shome = ctk.CTk()
        self.shome.geometry("650x600")
        self.shome.resizable(False, False)
        self.shome.title(reshape("الجرعات"))

        Header = ctk.CTkLabel(self.shome, text=get_display(reshape("كشف تسجيل و متابعة جرعات")), fg_color="#ccbc6c",
                              width=300, height=50, font=("arial", 18, "bold"), corner_radius=10)
        Header.place(x=170, y=10)
        self.frame1 = ctk.CTkFrame(self.shome, fg_color="gray", width=300, height=290)
        self.frame1.place(x=330, y=70)
        self.frame2 = ctk.CTkFrame(self.shome, fg_color="gray", width=300, height=200)
        self.frame2.place(x=330, y=370)
        self.frame3 = ctk.CTkFrame(self.shome, fg_color="gray", width=305, height=500)
        self.frame3.place(x=10, y=70)
        # الفريم الأول
        self.lab_name_ = ctk.CTkLabel(self.frame1, fg_color="#ccbc6c", font=("arial", 12, "bold"), corner_radius=10,
                                      width=200, height=40, text=name)
        self.lab_name_.place(x=90, y=20)
        self.lab_code = ctk.CTkLabel(self.frame1, fg_color="#ccbc6c", font=("arial", 12, "bold"), corner_radius=10,
                                     width=70, height=40, text=code)
        self.lab_code.place(x=10, y=20)
        self.lab_person = ctk.CTkLabel(self.frame1, fg_color="#ccbc6c", font=("arial", 12, "bold"), corner_radius=10,
                                       width=140, height=30, text=person)
        self.lab_person.place(x=150, y=70)
        self.lab_kind = ctk.CTkLabel(self.frame1, fg_color="#ccbc6c", font=("arial", 12, "bold"), corner_radius=10,
                                     text=get_display(reshape(self.kind)), width=130, height=30)
        self.lab_kind.place(x=10, y=70)
        self.lab_num_q = ctk.CTkLabel(self.frame1, fg_color="#32BB79", font=("arial", 16, "bold"), corner_radius=5,
                                      text=get_display(reshape("رقم الجلسة")), width=105, height=30)
        self.lab_num_q.place(x=190, y=110)
        self.lab_qun = ctk.CTkLabel(self.frame1, fg_color="#8A92D8", font=("arial", 16, "bold"), corner_radius=5,
                                    text=get_display(reshape("كمية الجرعة")), width=100, height=30)
        self.lab_qun.place(x=190, y=150)
        self.lab_date_q = ctk.CTkLabel(self.frame1, fg_color="#AF8AD8", font=("arial", 16, "bold"), corner_radius=5,
                                       text=get_display(reshape("تاريخ الجرعة")), width=100, height=30)
        self.lab_date_q.place(x=190, y=190)
        self.lab_date_q = ctk.CTkLabel(self.frame1, fg_color="white", text_color="black", font=("arial", 13, "bold"),
                                       corner_radius=5, text=get_display(reshape("ملل\جول")), width=60, height=30)
        self.lab_date_q.place(x=10, y=150)

        # الفريم الثانى
        self.search_lab_head = ctk.CTkLabel(self.frame2, fg_color="#0B1042", text_color="white",
                                            font=("arial", 14, "bold"), corner_radius=5,
                                            text=get_display(reshape("من تاريخ")), width=200, height=30)
        self.search_lab_head.place(x=50, y=10)
        self.search_lab_from = ctk.CTkLabel(self.frame2, fg_color="#0B1042", text_color="white",
                                            font=("arial", 14, "bold"), corner_radius=5,
                                            text=get_display(reshape("من تاريخ")), width=80, height=30)
        self.search_lab_from.place(x=210, y=60)
        self.search_lab_to = ctk.CTkLabel(self.frame2, fg_color="#0B1042", text_color="white",
                                          font=("arial", 14, "bold"), corner_radius=5,
                                          text=get_display(reshape("الى تاريخ")), width=80, height=30)
        self.search_lab_to.place(x=210, y=100)

        # مدخلات الفريم الأول
        self.num_q_ent = Entry(self.frame1, font=("arial", 12, "bold"), justify="center")
        self.num_q_ent.place(x=80, y=110, width=100, height=30)
        self.counter = Entry(self.frame1, font=("arial", 12, "bold"), justify="center")
        self.counter.place(x=10, y=110, width=60, height=30)
        self.date_ent = tkcalendar.DateEntry(self.frame1, date_pattern=date_pattern, font=("arial", 12, "bold"))
        self.date_ent.place(x=10, y=190, width=170, height=30)
        self.qun_ent = Entry(self.frame1, font=("arial", 12, "bold"))
        self.qun_ent.place(x=80, y=150, width=100, height=30)

        # مدخلات الفريم الثانى
        self.date_from = tkcalendar.DateEntry(self.frame2, date_pattern=date_pattern, font=("arial", 12, "bold"))
        self.date_from.place(x=10, y=60, width=190, height=30)
        self.date_to = tkcalendar.DateEntry(self.frame2, date_pattern=date_pattern, font=("arial", 12, "bold"))
        self.date_to.place(x=10, y=100, width=190, height=30)

        self.btn_add_q = ctk.CTkButton(self.frame1, text=get_display(reshape("اضافة")), fg_color="#683591",
                                       font=("arial", 14, "bold"), width=80, height=35, corner_radius=10,
                                       command=self.add_inject)
        self.btn_add_q.place(x=10, y=250)
        self.btn_done_e = ctk.CTkButton(self.frame1, text=get_display(reshape("حفظ ")), fg_color="#199710",
                                        font=("arial", 14, "bold"), width=80, height=35, corner_radius=10,
                                        command=self.done_edit)
        self.btn_done_e.place(x=110, y=250)
        self.btn_edit = ctk.CTkButton(self.frame1, text=get_display(reshape("تعديل")), fg_color="#109789",
                                      font=("arial", 14, "bold"), width=80, height=35, corner_radius=10,
                                      command=self.edit_qun)
        self.btn_edit.place(x=110, y=250)
        self.btn_del_q = ctk.CTkButton(self.frame1, text=get_display(reshape("حذف")), fg_color="#971010",
                                       font=("arial", 14, "bold"), width=80, height=35, corner_radius=10,
                                       command=self.del_inject)
        self.btn_del_q.place(x=210, y=250)

        self.btn_search = ctk.CTkButton(self.frame2, text=get_display(reshape("بحث")), fg_color="#353F91",
                                        font=("arial", 14, "bold"), width=160, height=35, corner_radius=10,
                                        command=self.search_date)
        self.btn_search.place(x=130, y=150)

        self.btn_refresh = ctk.CTkButton(self.frame2, text=get_display(reshape("تحديث")), fg_color="#5B0C0C",
                                         font=("arial", 14, "bold"), width=80, height=35, corner_radius=10,
                                         command=lambda: (self.table(), self.num_defualt()))
        self.btn_refresh.place(x=20, y=150)
        self.btn_count_add = ctk.CTkButton(self.frame3, text=get_display(reshape("اضافة جلسات")), fg_color="#5B0C0C",
                                           font=("arial", 14, "bold"), width=100, height=35, corner_radius=10,
                                           command=self.add_sets)
        self.btn_count_add.place(x=20, y=450)

        self.table_qun = ttk.Treeview(self.frame3)
        self.table_qun.place(x=17, y=20, width=280, height=400)
        self.table_qun['columns'] = ("num", "qun", "date", "timer")
        self.table_qun.column("#0", width=0, stretch=NO)
        self.table_qun.column("num", width=60)
        self.table_qun.column("qun", width=60)
        self.table_qun.column("date", width=160)
        self.table_qun.heading("num", text=get_display(reshape("الرقم ")))
        self.table_qun.heading("qun", text=get_display(reshape("الكمية ")))
        self.table_qun.heading("date", text=get_display(reshape("تاريخ الجرعة")))
        scroll_v = ctk.CTkScrollbar(self.frame3, orientation="vertical", command=self.table_qun.xview, height=200,
                                    fg_color="gray", button_color="#ccbc6c")
        self.table_qun.configure(yscrollcommand=scroll_v.set)
        scroll_v.place(x=2, y=20)
        # اغلاق النافذة الثالثة
        self.shome.protocol("WM_DELETE_WINDOW", lambda: self.exit())
        self.fun_timer()
        self.table()
        self.num_defualt()



# معادلة الخروج من البرنامج
    def exit(self):
        try:
            if self.sets_dd and hasattr(self.sets_dd, 'count_app'):
                self.sets_dd.count_app.destroy()
                self.Third_window_closed = False
        except Exception as e:
            self.Third_window_closed = False
            pass
        self.shome.destroy()
        return self.Third_window_closed

   #معادلة تحديث الجدول
    def table(self):
        self.table_qun.delete(*self.table_qun.get_children())
        con = sqlite3.connect("data_base.db")
        cur = con.cursor()
        cur.execute(f"select * from {'table_' + str(self.cod)}")
        all_inject = cur.fetchall()
        for inject in all_inject:
            self.table_qun.insert("", END, values=inject)

    #معادلة جهاز معين
    def fun_timer(self):
        if self.lab_kind.cget("text") == "4":
            self.qun_ent.place(x=55, y=150, width=50, height=30)
            self.lab_date_q.configure(text=get_display(reshape("جول")), width=30)
            self.lab_qun.configure(text=get_display(reshape("الجرعة")), width=40)
            self.lab_qun.place(x=110, y=150)
            self.lab_time = ctk.CTkLabel(self.frame1, fg_color="white", text_color="black", font=("arial", 13, "bold"),
                                         corner_radius=5, text=get_display(reshape("الوقت")), width=40, height=30)
            self.lab_time.place(x=245, y=150)
            self.time_ent_h = Entry(self.frame1, font=("arial", 12, "bold"), justify="center")
            self.time_ent_h.place(x=177, y=150, width=25, height=30)
            self.lab_cotishan = ctk.CTkLabel(self.frame1, fg_color="white", text_color="black",
                                             font=("arial", 13, "bold"),
                                             text=get_display(reshape(":")), width=7, height=30)
            self.lab_cotishan.place(x=203, y=150)
            self.time_ent_m = Entry(self.frame1, font=("arial", 12, "bold"), justify="center")
            self.time_ent_m.place(x=210, y=150, width=30, height=30)
            self.table_qun.column("timer", width=60)
            self.table_qun.heading("timer", text=get_display(reshape("الوقت")))

    # معادلة اضافة جرعة
    def add_inject(self):
        if self.lab_kind.cget("text") == "4":
            if not self.qun_ent.get().replace('.', '', 1).isdigit():
                return
            elif (self.date_ent.get_date() is None) or self.qun_ent.get() == "":
                return
            elif not self.time_ent_h.get().isdigit() or not self.time_ent_m.get().isdigit():
                return
            elif self.time_ent_h.get() == "" or self.time_ent_m.get() == "":
                return
            else:
                con = sqlite3.connect("data_base.db")
                cur = con.cursor()
                cur.execute(
                    f"insert into {'table_' + self.lab_code.cget('text')} (num , qun , date ,timer)values ('{self.num_q_ent.get()}', '{float(self.qun_ent.get())}', '{self.date_ent.get()}','{self.time_ent_h.get() + ' : ' + self.time_ent_m.get()}')")
                con.commit()
                con.close()
                self.num_q_ent.delete(0, END)
                self.qun_ent.delete(0, END)
                self.date_ent.delete(0, END)
                self.time_ent_h.delete(0, END)
                self.time_ent_m.delete(0, END)
                self.table()
                self.num_defualt()

        else:
            if not self.qun_ent.get().replace('.', '', 1).isdigit():
                return
            elif (self.date_ent.get_date() is None) or self.qun_ent.get() == "":
                return
            else:
                con = sqlite3.connect("data_base.db")
                cur = con.cursor()
                cur.execute(
                    f"insert into {'table_' + self.lab_code.cget('text')} (num , qun , date ,timer)values ('{self.num_q_ent.get()}', '{float(self.qun_ent.get())}', '{self.date_ent.get()}','_')")
                con.commit()
                con.close()
                self.num_q_ent.delete(0, END)
                self.qun_ent.delete(0, END)
                self.date_ent.delete(0, END)
                self.table()
                self.num_defualt()

    # معادلة حذف جرعة
    def del_inject(self):
        if self.table_qun.selection():
            del_qun = self.table_qun.selection()
            for qun_d in del_qun:
                values = self.table_qun.item(qun_d, 'values')
                con = sqlite3.connect("data_base.db")
                cur = con.cursor()
                num = values[0]
                qun = values[1]
                cur.execute(f"DELETE FROM {'table_' + self.lab_code.cget('text')} WHERE num=? AND qun=?", (num, qun))
                con.commit()
                con.close()
                self.table()
                self.num_defualt()

    # معادلة التعديل
    def edit_qun(self):
        if self.table_qun.selection():
            edit_qun = self.table_qun.selection()
            for qun_e in edit_qun:
                values = self.table_qun.item(qun_e, 'values')
                num = values[0]
                qun = values[1]
                date = values[2]
                value = values[3]
                if self.lab_kind.cget("text") == "4":
                    timer = value.split(" : ")
                    timer_h = timer[0]
                    timer_m = timer[0]
                    self.time_ent_h.delete(0, END)
                    self.time_ent_m.delete(0, END)
                    self.time_ent_h.insert(0, timer_h)
                    self.time_ent_m.insert(0, timer_m)
                else:
                    pass
                self.num_q_ent.configure(state=NORMAL)
                self.num_q_ent.delete(0, END)
                self.qun_ent.delete(0, END)
                self.date_ent.delete(0, END)

                self.num_q_ent.insert(0, num)
                self.qun_ent.insert(0, qun)
                self.date_ent.insert(0, date)

                self.btn_add_q.configure(state=DISABLED)
                self.num_q_ent.configure(state="readonly")
                self.btn_edit.destroy()
                self.table()

    # معادلة الحفظ على التعديل
    def done_edit(self):
        def is_float(value):
            try:
                float(value)
                return True
            except ValueError:
                return False

        qun_value = self.qun_ent.get()
        if (self.date_ent.get_date() is None) or qun_value == "":
            return
        else:
            if not qun_value.isdigit() and not is_float(qun_value):
                return
            else:
                if self.lab_kind.cget("text") == "4":
                    if self.time_ent_h.get() == "" or self.time_ent_m.get() == "":
                        return
                    elif not self.time_ent_h.get().isdigit() or not self.time_ent_m.get().isdigit():
                        return
                    else:
                        date = self.date_ent.get()
                        con = sqlite3.connect("data_base.db")
                        cur = con.cursor()
                        cur.execute(
                            f"update {'table_' + self.lab_code.cget('text')} set qun = '{float(self.qun_ent.get())}', date ='{str(date)}', timer = '{self.time_ent_h.get() + ' : ' + self.time_ent_m.get()}' where num='{self.num_q_ent.get()}'")
                        con.commit()
                        con.close()
                        self.time_ent_h.delete(0, END)
                        self.time_ent_m.delete(0, END)
                else:
                    date = self.date_ent.get()
                    con = sqlite3.connect("data_base.db")
                    cur = con.cursor()
                    cur.execute(
                        f"update {'table_' + self.lab_code.cget('text')} set qun = '{float(self.qun_ent.get())}', date ='{str(date)}' where num='{self.num_q_ent.get()}'")
                    con.commit()
                    con.close()
                self.qun_ent.delete(0, END)
                self.date_ent.delete(0, END)
                self.table()
                self.btn_done_e = ctk.CTkButton(self.frame1, text=get_display(reshape("حفظ ")), fg_color="#199710",
                                                font=("arial", 14, "bold"), width=80, height=35, corner_radius=10,
                                                command=self.done_edit)
                self.btn_done_e.place(x=110, y=250)
                self.btn_edit = ctk.CTkButton(self.frame1, text=get_display(reshape("تعديل")), fg_color="#109789",
                                              font=("arial", 14, "bold"), width=80, height=35, corner_radius=10,
                                              command=self.edit_qun)
                self.btn_edit.place(x=110, y=250)
                self.btn_add_q.configure(state=NORMAL)
                self.num_defualt()

    # البحث من تاريخ الى تاريخ
    def search_date(self):
        self.table_qun.delete(*self.table_qun.get_children())
        con = sqlite3.connect("data_base.db")
        cur = con.cursor()
        cur.execute(
            f"SELECT * FROM {'table_' + self.lab_code.cget('text')} WHERE date BETWEEN '{self.date_from.get()}' AND '{self.date_to.get()}'")
        all_search = cur.fetchall()
        for search in all_search:
            self.table_qun.insert("", END, values=search)
        con.commit()
        con.close()

    # معادلة وضع رقم ثابت للجرعة
    def num_defualt(self):
        self.counter.configure(state=NORMAL)
        self.num_q_ent.configure(state=NORMAL)
        self.counter.delete(0, END)
        self.num_q_ent.delete(0, END)
        con = sqlite3.connect("data_base.db")
        cur = con.cursor()
        cur.execute(
            f"SELECT MAX(CAST(num AS INTEGER)) FROM {'table_' + str(self.cod)} ")
        unit = cur.fetchone()
        if unit[0] is None:
            self.num_q_ent.insert(0, "1")
        else:
            self.num_q_ent.insert(0, unit[0] + 1)
        self.num_q_ent.configure(state="readonly")

        # التحقق من وجود الجدول
        table_name = 'counter_' + self.lab_code.cget("text")
        print(self.lab_code.cget("text"))
        cur.execute(f"SELECT count(*) FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cur.fetchone()
        # إذا كان الجدول موجودًا، قم بالاستعلام عن القيمة
        if result and result[0] > 0:
            if self.num_q_ent.get() is not None:
                cur.execute(f"SELECT SUM(CAST(count AS INTEGER)) FROM {table_name}")
                self.count = cur.fetchone()[0]
                print(self.count)
                self.count -= int(self.num_q_ent.get())

        else:
            self.count = 0
        self.counter.insert(0, str(self.count))
        self.counter.configure(state="readonly")

    # فتح الملف الثالث و النافذة الثالثة
    def add_sets(self):
        self.sets_dd = counter_sets.counter_by(lab_code=self.cod)
        self.Third_window_closed = True

    def run_shome(self):
        self.shome.mainloop()


if __name__ == '__main__':
    app = access(kind="", person="", code="" , name="")
    app.run_shome()
