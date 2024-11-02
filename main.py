import customtkinter as ctk
import sqlite3
import tkcalendar
import test
from tkinter import *
from tkinter import messagebox, ttk
from screeninfo import get_monitors
from awesometkinter.bidirender import add_bidi_support
from bidi.algorithm import get_display
from arabic_reshaper import reshape

con = sqlite3.connect("data_base.db")
cur = con.cursor()
cur.execute(
    "create table if not exists customer(cod text, name text , num text , gender text , age text, date text , "
    "adrss text ,ray text , "
    "person text ,kind Text)")
cur.execute("select * from customer")
patients = cur.fetchall()
cur.execute("SELECT MAX(CAST(cod AS INTEGER)) FROM customer")
all_code = cur.fetchone()[0]
if all_code is None:
    code = 1
else:
    code = int(all_code) + 1
con.commit()
con.close()
# اساسيات لغوية و عرض شاشة
screen = get_monitors()[0]
genders_arabic = (["انثى", "ذكر"])
genders_display = [get_display(reshape(gender)) for gender in genders_arabic]
genders_arabic2 = (["الاسم", "رقم الصفحة"])
search_display = [get_display(reshape(search)) for search in genders_arabic2]
dises = ["صدفية", "حالات اخرى", "بهاق", "ثعلبة"]
search_dieses = [get_display(reshape(a)) for a in dises]
adrss = ["امامى", "امامى خلفى"]
search_adrss = [get_display(reshape(a)) for a in adrss]
date_pattern = 'dd-MM-yyyy'
ray = ["UVA", "UVB"]
machine = ["1", "2", "3", "4"]


class Home:
    def __init__(self):
        super().__init__()
        self.access_instance = None
        self.click_count = 0
        ctk.set_appearance_mode("light")
        self.app = ctk.CTk()
        self.app.geometry(f"{screen.width}x{screen.height}+0+0")
        self.app.title('x_data entry v:1.0'.title())
        self.app.resizable(False,False)
        self.frm1 = ctk.CTkFrame(self.app, fg_color="#A0B1CF", border_color="black", border_width=2)
        self.frm1.place(relx=0.74, rely=0.12 , relwidth=0.25, relheight=0.87)
        self.frm2 = ctk.CTkFrame(self.app, fg_color="#A0B1CF", border_color="black", border_width=2)
        self.frm2.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.09)
        self.frm3 = ctk.CTkFrame(self.app, fg_color="white", border_color="black", border_width=2)
        self.frm3.place(relx=0.01, rely=0.12 ,relwidth=0.72, relheight=0.87)

        self.header = ctk.CTkLabel(self.frm1, text_color="black", width=300, height=60, font=("arial", 18, "bold"),
                                   text=get_display(reshape("تسجيل بيانات المريض")), corner_radius=10,
                                   fg_color="#ccbc6c")
        self.header.place(x=20, y=20)
        self.lab_cod = ctk.CTkLabel(self.frm1, text_color="black", width=105, height=30, font=("arial", 14, "bold"),
                                    text=get_display(reshape("رقم الصفحة")), corner_radius=10, fg_color="#ccbc6c")
        self.lab_cod.place(x=225, y=125)
        self.lab_name = ctk.CTkLabel(self.frm1, text_color="black", width=100, height=30, font=("arial", 14, "bold"),
                                     text=get_display(reshape("اسم المريض")), corner_radius=10, fg_color="#ccbc6c")
        self.lab_name.place(x=225, y=165)
        self.lab_num = ctk.CTkLabel(self.frm1, text_color="black", width=100, height=30, font=("arial", 14, "bold"),
                                    text=get_display(reshape("ID")), corner_radius=10, fg_color="#ccbc6c")
        self.lab_num.place(x=225, y=205)
        self.lab_gender = ctk.CTkLabel(self.frm1, text_color="black", width=103, height=30, font=("arial", 14, "bold"),
                                       text=get_display(reshape("الجنس ")), corner_radius=10, fg_color="#ccbc6c")
        self.lab_gender.place(x=225, y=245)
        self.lab_adrss = ctk.CTkLabel(self.frm1, text_color="black", width=103, height=30, font=("arial", 14, "bold"),
                                      text=get_display(reshape("الاتجاه ")), corner_radius=10, fg_color="#ccbc6c")
        self.lab_adrss.place(x=225, y=365)
        self.lab_date = ctk.CTkLabel(self.frm1, text_color="black", width=103, height=30, font=("arial", 14, "bold"),
                                     text=get_display(reshape("تاريخ البداية ")), corner_radius=10, fg_color="#ccbc6c")
        self.lab_date.place(x=225, y=325)
        self.lab_age = ctk.CTkLabel(self.frm1, text_color="black", width=103, height=30, font=("arial", 14, "bold"),
                                    text=get_display(reshape("السن ")), corner_radius=10, fg_color="#ccbc6c")
        self.lab_age.place(x=225, y=285)

        self.lab_ray = ctk.CTkLabel(self.frm1, text_color="black", width=103, height=30, font=("arial", 14, "bold"),
                                    text=get_display(reshape("نوع الأشعة ")), corner_radius=10, fg_color="#ccbc6c")
        self.lab_ray.place(x=225, y=405)
        self.lab_person = ctk.CTkLabel(self.frm1, text_color="black", width=103, height=30, font=("arial", 12, "bold"),
                                       text=get_display(reshape("نوع التشخيص ")), corner_radius=10, fg_color="#ccbc6c")
        self.lab_person.place(x=225, y=445)
        self.lab_kind = ctk.CTkLabel(self.frm1, text_color="black", width=103, height=30, font=("arial", 14, "bold"),
                                     text=get_display(reshape("نوع الجهاز ")), corner_radius=10, fg_color="#ccbc6c")
        self.lab_kind.place(x=225, y=485)

        # المدخلات
        self.cod_ent = Entry(self.frm1, font=("arial", 12, "bold"), fg="white", foreground="black", border=2,
                             borderwidth=2, highlightcolor="yellow", justify="center")
        self.cod_ent.insert(0, str(code))
        self.cod_ent.config(state="readonly")
        self.cod_ent.place(x=10, y=126, width=205, height=30)
        self.name_ent = Entry(self.frm1, font=("arial", 10, "bold"), fg="white", foreground="black", border=2,
                              borderwidth=2, highlightcolor="yellow")
        self.name_ent.place(x=10, y=166, width=205, height=30)
        self.num_ent = Entry(self.frm1, font=("arial", 10, "bold"), fg="white", foreground="black", border=2,
                             borderwidth=2, highlightcolor="yellow")
        self.num_ent.place(x=10, y=206, width=205, height=30)
        self.gender_ent = ttk.Combobox(self.frm1, font=("arial", 10, "bold"), values=genders_display, state="readonly")
        self.gender_ent.place(x=10, y=246, width=205, height=30)
        self.adrss_ent = ttk.Combobox(self.frm1, font=("arial", 10, "bold"), values=search_adrss, state="readonly")
        self.adrss_ent.place(x=10, y=366, width=205, height=30)
        self.date_ent = tkcalendar.DateEntry(self.frm1, date_pattern=date_pattern, font=("arial", 12, "bold"),
                                             state="readonly")
        self.date_ent.place(x=10, y=326, width=205, height=30)
        self.age_ent = Entry(self.frm1, font=("arial", 10, "bold"), fg="white", foreground="black", border=2,
                             borderwidth=2, highlightcolor="yellow")
        self.age_ent.place(x=10, y=286, width=205, height=30)
        self.ray_ent = ttk.Combobox(self.frm1, font=("arial", 10, "bold"), values=ray, state="readonly")
        self.ray_ent.place(x=10, y=406, width=205, height=30)
        self.person = ttk.Combobox(self.frm1, font=("arial", 10, "bold"), values=search_dieses, state="readonly")
        self.person.place(x=10, y=446, width=205, height=30)
        self.kind = ttk.Combobox(self.frm1, font=("arial", 10, "bold"), values=machine, state="readonly")
        self.kind.place(x=10, y=486, width=205, height=30)

        # الفريم الثانى
        self.lab_search = ctk.CTkLabel(self.frm2, text_color="black", width=140, height=30, font=("arial", 14, "bold"),
                                       text=get_display(reshape("البحث عن طريق ")), corner_radius=10,
                                       fg_color="#ccbc6c")
        self.lab_search.place(x=820, y=20)
        self.search_comb = ttk.Combobox(self.frm2, font=("arial", 10, "bold"), values=search_display, state="readonly")
        self.search_comb.place(x=650, y=20, width=150, height=30)

        self.search_ent = Entry(self.frm2, font=("arial", 10, "bold"), fg="white", foreground="black", border=2,
                                borderwidth=2, highlightcolor="yellow")
        self.search_ent.place(x=430, y=20, width=205, height=30)

        # ازرار التحكم بالنظام
        self.btn_add = ctk.CTkButton(self.frm1, text_color="white", text=get_display(reshape("اضافة مريض")),
                                     font=("arial", 14, "bold"), width=150, height=35, fg_color="#132A52",
                                     command=self.add)
        self.btn_add.place(x=10, y=530)
        self.btn_del = ctk.CTkButton(self.frm1, text_color="white", text=get_display(reshape("حذف مريض")),
                                     font=("arial", 14, "bold"), width=150, height=35, fg_color="#7C1824",
                                     command=self.del_patient)
        self.btn_del.place(x=180, y=530)

        self.btn_edit_done = ctk.CTkButton(self.frm1, text_color="white", text=get_display(reshape("حفظ البيانات")),
                                           font=("arial", 14, "bold"), width=150, height=35, fg_color="#5C8C18",
                                           command=self.edit_done)

        self.btn_edit_done.place(x=100, y=580)
        self.btn_edit = ctk.CTkButton(self.frm1, text_color="white", text=get_display(reshape("تعديل بيانات")),
                                      font=("arial", 14, "bold"), width=150, height=35, fg_color="#188C57",
                                      command=self.edit_patent)
        self.btn_edit.place(x=100, y=580)

        self.btn_search = ctk.CTkButton(self.frm2, text_color="white", text=get_display(reshape("بـحـث")),
                                        font=("arial", 14, "bold"), width=100, height=30, fg_color="#132A52",
                                        command=self.search_by_name)
        self.btn_search.place(x=320, y=20)
        # اظهار المدخلات باللغة العربية
        add_bidi_support(self.name_ent)
        add_bidi_support(self.adrss_ent)
        add_bidi_support(self.search_ent)

        # جدول ادخال المرضى
        style = ttk.Style()
        style.configure("Treeview.Heading", background="#ccbc6c", foreground="black", font=('arial', 12, 'bold'),
                        height=20)
        style.configure('Treeview', background=[('selected', '#02050f')], text_color="white",
                        font=('arial', 12))
        self.table_name = ttk.Treeview(self.frm3)
        self.table_name.place(x=16, y=20, width=960, height=570)
        self.table_name['columns'] = ["cod", "name", "num", "gender", "age", "date", "adrss", "ray", "person", "kind"]
        self.table_name.column('#0', width=0, stretch=NO)
        self.table_name.column("cod", width=100)
        self.table_name.column("name", width=200)
        self.table_name.column("num", width=130)
        self.table_name.column("gender", width=80)
        self.table_name.column("age", width=80)
        self.table_name.column("date", width=150)
        self.table_name.column("adrss", width=120)
        self.table_name.column("ray", width=100)
        self.table_name.column("person", width=100)
        self.table_name.column("kind", width=100)

        # رأس الجداول النصية
        self.table_name.heading("cod", text=get_display(reshape("رقم الصفحة")))
        self.table_name.heading("name", text=get_display(reshape("اسم المريض")))
        self.table_name.heading("num", text=get_display(reshape("ID")))
        self.table_name.heading("gender", text=get_display(reshape("الجنس")))
        self.table_name.heading("age", text=get_display(reshape("السن")))
        self.table_name.heading("date", text=get_display(reshape("تاريخ البداية")))
        self.table_name.heading("adrss", text=get_display(reshape("الاتجاه")))
        self.table_name.heading("ray", text=get_display(reshape("نوع الاشعة")))
        self.table_name.heading("person", text=get_display(reshape("التشخيص")))
        self.table_name.heading("kind", text=get_display(reshape("الجهاز")))

        scroll_v = ctk.CTkScrollbar(self.frm3, orientation="vertical", command=self.table_name.xview, height=200,
                                    fg_color="gray", button_color="#ccbc6c")
        self.table_name.configure(yscrollcommand=scroll_v.set)
        scroll_v.place(x=2, y=22)
        scroll_H = ctk.CTkScrollbar(self.frm3, orientation="horizontal", command=self.table_name.xview, width=150,
                                    fg_color="gray", button_color="#ccbc6c")
        self.table_name.configure(xscrollcommand=scroll_H.set)
        scroll_H.place(x=2, y=2)
        for i, patient in enumerate(patients):
            patient_arabic = [get_display(reshape(str(value))) if i else str(value) for
                              i, value in
                              enumerate(patient)]
            self.table_name.insert("", END, values=patient_arabic)

        # تشغيل المعادلة دائما فى الخلفية على الجدول
        self.table_name.bind("<Double-1>", self.double_click)
        self.table_name.bind("<<TreeviewSelect>>", lambda event: self.selection_antother())
        # كود اغلاق جميع النوافذ
        self.app.protocol("WM_DELETE_WINDOW", lambda: self.exit())

    # معادلة اغلاق جميع النوافذ
    def exit(self):
        self.app.destroy()
        if self.access_instance:  # التحقق مما إذا كانت access_instance معينة
            self.access_instance.shome.quit()

    # معادلة اضافة مرضى
    def add(self):
        if self.cod_ent.get() == "" or self.num_ent.get() == "" or self.name_ent.get() == "" or (
                self.gender_ent.get()) == "" or self.adrss_ent.get() == "" or self.ray_ent.get() == "" or self.person.get() == "" or self.kind.get() == "" \
                or self.age_ent.get() == "":
            messagebox.showerror(reshape("خطأ"), get_display(reshape(" من فضلك املأ الحقول")))
        elif not self.age_ent.get().isdigit():
            messagebox.showerror(reshape("خطأ"), get_display(reshape("السن يجب أن يحتوي على أرقام فقط")))
        elif not self.num_ent.get().isdigit():
            messagebox.showerror(reshape("خطأ"), get_display(reshape("ID يجب أن يحتوي على أرقام فقط")))
        else:
            con = sqlite3.connect("data_base.db")
            cur = con.cursor()
            cur.execute(
                f"insert into customer ( cod , name , num , gender ,age, date, adrss , ray , person , kind)values ('{self.cod_ent.get()}','{self.name_ent.get()}','{self.num_ent.get()}','{get_display(self.gender_ent.get())}','{self.age_ent.get()}','{self.date_ent.get()}','{get_display(self.adrss_ent.get())}','{self.ray_ent.get()}','{get_display(self.person.get())}','{self.kind.get()}')")
            con.commit()
            cur.execute("SELECT MAX(CAST(cod AS INTEGER)) FROM customer")
            all_code = cur.fetchone()[0]
            code = all_code + 1
            self.cod_ent.configure(state=NORMAL)
            self.cod_ent.delete("0", END)
            self.cod_ent.insert(0, str(code))
            self.cod_ent.configure(state="readonly")
            self.num_ent.delete("0", END)
            self.name_ent.delete("0", END)
            self.gender_ent.set("")
            self.age_ent.delete("0", END)
            self.date_ent.set_date(None)
            self.adrss_ent.set("")
            self.ray_ent.set("")
            self.kind.set("")
            self.person.set("")
            messagebox.showinfo(reshape("نجاح"), get_display(reshape(" تم اضافة المريض")))
            cur.execute("select * from customer")
            add_patient = cur.fetchall()
            self.table_name.delete(*self.table_name.get_children())
            for i, patient in enumerate(add_patient):
                # تحويل البيانات النصية باللغة العربية باستثناء البيان رقم 5و3
                patient_add_arabic = [get_display(reshape(str(value))) if i else str(value)
                                      for i, value
                                      in
                                      enumerate(patient)]
                # إدراج البيانات في الجدول
                self.table_name.insert("", END, values=patient_add_arabic)

            con.commit()
            con.close()

    # معادلة حذف المريضمن قاعدة البيانات
    def del_patient(self):
        if self.table_name.selection():
            message = messagebox.askyesno(reshape("حذف مريض"), get_display(reshape("هل تريد حذف المريض")))
            if message:
                del_patients = self.table_name.selection()
                for patient_d in del_patients:
                    values = self.table_name.item(patient_d, 'values')
                    con = sqlite3.connect("data_base.db")
                    cur = con.cursor()
                    cod = values[0]
                    num = values[2]
                    cur.execute(f"DELETE FROM customer WHERE cod=? AND num=?", (cod, num))
                    con.commit()
                    cur.execute("SELECT MAX(CAST(cod AS INTEGER)) FROM customer")
                    all__code = cur.fetchone()[0]
                    if all__code is None:
                        code_ = 1
                    else:
                        code_ = int(all__code) + 1
                    self.cod_ent.configure(state=NORMAL)
                    self.cod_ent.delete("0", END)
                    self.cod_ent.insert(0, str(code_))
                    self.cod_ent.configure(state="readonly")
                    self.table_name.delete(patient_d)
                    messagebox.showinfo(reshape("نجاح"), get_display(reshape("تم الحذف بنجاح")))
                    con.close()

        else:
            messagebox.showerror(reshape("خطأ"), get_display(reshape("من فضلك اختر مريض من الجدول")))

    # معادلة البحث النصى و الرقمى للمريض
    def search_by_name(self):
        if self.search_ent.get() == "" and (
                (self.search_comb.get() == "ﻢﺳﻻﺍ") or (self.search_comb.get() == "ﺔﺤﻔﺼﻟﺍ ﻢﻗﺭ")):
            con = sqlite3.connect("data_base.db")
            cur = con.cursor()
            cur.execute("select * from customer")
            search_non = cur.fetchall()
            self.table_name.delete(*self.table_name.get_children())
            for patient in search_non:
                patient_arabic = [get_display(reshape(str(value))) if i else str(value) for
                                  i, value in
                                  enumerate(patient)]
                self.table_name.insert("", END, values=patient_arabic)
            con.commit()
            con.close()
        else:
            # الحصول على الاسم المدخل من المستخدم
            search_name = self.search_ent.get()
            search_cod = self.search_ent.get()
            # فحص ما إذا كان الاسم مدخلًا أم لا
            if self.search_comb.get() == "ﻢﺳﻻﺍ":
                # الاتصال بقاعدة البيانات
                con = sqlite3.connect("data_base.db")
                cur = con.cursor()
                # تنفيذ الاستعلام للبحث عن السجلات التي تحتوي على الاسم المدخل
                cur.execute(f"SELECT * FROM customer WHERE name LIKE '%{search_name}%'")
                search_results = cur.fetchall()
                # عرض نتائج البحث في الجدول
                self.table_name.delete(*self.table_name.get_children())
                for patient in search_results:
                    patient_arabic = [get_display(reshape(str(value))) if i else str(value)
                                      for i, value in
                                      enumerate(patient)]
                    self.table_name.insert("", END, values=patient_arabic)
                con.close()
            elif self.search_comb.get() == "ﺔﺤﻔﺼﻟﺍ ﻢﻗﺭ":
                # الاتصال بقاعدة البيانات
                con = sqlite3.connect("data_base.db")
                cur = con.cursor()
                # تنفيذ الاستعلام للبحث عن السجلات التي تحتوي على الاسم المدخل
                cur.execute(f"SELECT * FROM customer WHERE cod LIKE '%{search_cod}%'")
                search_results = cur.fetchall()
                # عرض نتائج البحث في الجدول
                self.table_name.delete(*self.table_name.get_children())
                for patient in search_results:
                    patient_arabic = [get_display(reshape(str(value))) if i else str(value)
                                      for i, value in
                                      enumerate(patient)]
                    self.table_name.insert("", END, values=patient_arabic)
            else:
                # عرض رسالة خطأ إذا لم يتم إدخال اسم للبحث
                messagebox.showerror(reshape("خطأ"), get_display(reshape("من فضلك اختر من خيارات البحث")))

    # معادلة التعديلات
    def edit_patent(self):
        global patient
        if self.table_name.selection():
            self.btn_add.configure(state=DISABLED)
            edit_patients = self.table_name.selection()
            for patient_ed in edit_patients:
                values = self.table_name.item(patient_ed, 'values')
                con = sqlite3.connect("data_base.db")
                cur = con.cursor()
                cod = values[0]
                num = values[2]
                cur.execute(f"select * FROM customer WHERE cod=? AND num=?", (cod, num))
                row_edit = cur.fetchall()

                for patient in row_edit:
                    # تعيين قيم كل متغير نصي
                    self.cod_ent.configure(state=NORMAL)
                    self.cod_ent.delete("0", END)
                    self.cod_ent.insert(0, patient[0])
                    self.cod_ent.configure(state="readonly")
                    self.name_ent.insert(0, get_display(reshape(patient[1])))
                    self.num_ent.insert(0, patient[2])
                    self.adrss_ent.set(get_display(reshape(patient[6])))
                    self.gender_ent.set(get_display(reshape(patient[3])))
                    self.date_ent.set_date(patient[5])
                    self.age_ent.insert(0, patient[4])
                    self.ray_ent.set(patient[7])
                    self.person.set(get_display(reshape(patient[8])))
                    self.kind.set(patient[9])
                    self.btn_edit.destroy()
                con.commit()
        else:
            messagebox.showerror(reshape("تنبيه"), get_display(reshape("اختر من الجدول")))

    # كعادلة تحديث الاختيارات
    def selection_antother(self):
        if self.table_name.selection():
            self.rec_edit()
        else:
            pass

    # معادلة حفظ التعديلات
    def edit_done(self):
        # التأكد من الخانات مكررة فى دالة الحفظ
        if self.cod_ent.get() == "" or self.num_ent.get() == "" or self.name_ent.get() == "" or (
                self.gender_ent.get()) == "" or self.adrss_ent.get() == "" or self.ray_ent.get() == "" or self.person.get() == "" or self.kind.get() == "" or self.age_ent.get() == "" or self.date_ent.get_date() == "":
            messagebox.showerror(reshape("خطأ"), get_display(reshape(" من فضلك املأ الحقول")))
        elif not self.age_ent.get().isdigit():
            messagebox.showerror(reshape("خطأ"), get_display(reshape("السن يجب أن يحتوي على أرقام فقط")))
        elif not self.num_ent.get().isdigit():
            messagebox.showerror(reshape("خطأ"), get_display(reshape("ID يجب أن يحتوي على أرقام فقط")))
        else:
            message = messagebox.askyesno(reshape("تعديل"), get_display(reshape("هل تريد التعديل ؟")))
            if message == True:
                con = sqlite3.connect("data_base.db")
                cur = con.cursor()
                cur.execute(
                    f"UPDATE customer SET cod='{self.cod_ent.get()}', name='{self.name_ent.get()}', num='{self.num_ent.get()}', gender='{get_display(self.gender_ent.get())}',age='{self.age_ent.get()}', date='{self.date_ent.get()}',  adrss='{get_display(self.adrss_ent.get())}' , ray='{self.ray_ent.get()}' , person='{get_display(self.person.get())}', kind='{self.kind.get()}' WHERE cod='{self.cod_ent.get()}' ")
                con.commit()
                cur.execute("select * from customer")
                edit_patient = cur.fetchall()
                self.table_name.delete(*self.table_name.get_children())
                for i, patient in enumerate(edit_patient):
                    patient_edit_arabic = [
                        get_display(reshape(str(value))) if i else str(value) for i, value in
                        enumerate(patient)]
                    self.table_name.insert("", END, values=patient_edit_arabic)
                messagebox.showinfo(reshape("نجاح"), get_display(reshape("تم التعديل بنجاح")))
                self.rec_edit()
                con.close()
            else:
                self.rec_edit()

    # معادلة تبديل ازرار
    def rec_edit(self):
        self.btn_edit_done = ctk.CTkButton(self.frm1, text_color="white", text=get_display(reshape("حفظ البيانات")),
                                           font=("arial", 14, "bold"), width=150, height=35, fg_color="#5C8C18",
                                           command=self.edit_done)
        self.btn_edit_done.place(x=100, y=580)
        self.btn_edit = ctk.CTkButton(self.frm1, text_color="white", text=get_display(reshape("تعديل بيانات")),
                                      font=("arial", 14, "bold"), width=150, height=35, fg_color="#188C57",
                                      command=self.edit_patent)
        self.btn_edit.place(x=100, y=580)
        self.btn_add.configure(state=NORMAL)
        self.cod_ent.delete("0", END)
        self.num_ent.delete("0", END)
        self.name_ent.delete("0", END)
        self.gender_ent.set("")
        self.age_ent.delete("0", END)
        self.date_ent.set_date(None)
        self.adrss_ent.set("")
        self.ray_ent.set("")
        self.kind.set("")
        self.person.set("")
        con = sqlite3.connect("data_base.db")
        cur = con.cursor()
        cur.execute("SELECT MAX(CAST(cod AS INTEGER)) FROM customer")
        all_code = cur.fetchone()[0]
        code = all_code + 1
        self.cod_ent.configure(state=NORMAL)
        self.cod_ent.delete("0", END)
        self.cod_ent.insert(0, str(code))
        self.cod_ent.configure(state="readonly")
        con.close()

    # الضغط مرتين
    def double_click(self, event):
        if self.table_name.selection():
            personal_patients = self.table_name.selection()
            for patient_d in personal_patients:
                values = self.table_name.item(patient_d, 'values')
                cod = values[0]
                cod_num = "table_" + str(cod)
                name = values[1]
                kind = values[9]
                person = values[8]
                con = sqlite3.connect("data_base.db")
                cur = con.cursor()
                cur.execute(f"CREATE TABLE IF NOT EXISTS {cod_num} (num INTEGER, qun TEXT, date TEXT , timer text)")
                con.commit()
                con.close()
                self.access_instance = test.access(kind=kind, name=name, code=cod, person=person)  # إنشاء مثيل


    def run(self):
        self.app.mainloop()


if __name__ == '__main__':
    app = Home()
    app.run()
