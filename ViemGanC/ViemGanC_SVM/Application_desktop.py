import pickle
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyodbc

server = 'LAPTOP-J2EVE03L\SQLEXPRESS'
database = 'ViemGanC'
username = 'sa'
password = '123'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
tendangnhap=''
# Tạo cửa sổ giao diện đăng nhập
login_window = tk.Tk()
login_window.title('Đăng nhập')

# Kích thước cửa sổ
window_width = 400
window_height = 300

# Lấy kích thước màn hình
screen_width = login_window.winfo_screenwidth()
screen_height = login_window.winfo_screenheight()

# Tính toán vị trí để hiển thị cửa sổ ở giữa màn hình
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Đặt vị trí cho cửa sổ
login_window.geometry(f"{window_width}x{window_height}+{x}+{y}")


# Hàm kiểm tra đăng nhập
def login():
    username = entry_username.get()
    password = entry_password.get()

    # Kiểm tra thông tin đăng nhập
    if username == "" or password == "":
        messagebox.showerror("Cảnh báo", "Vui lòng nhập tên đăng nhập và mật khẩu!")
    else:
        # Kiểm tra thông tin đăng nhập thành công
        if kiem_tra_dang_nhap(username, password):
            login_window.destroy()  # Đóng cửa sổ đăng nhập
            if username == "Admin" and password == "123":
                show_admin_window()  # Hiển thị cửa sổ form quản trị
            else:
                show_predict_window(username)  # Hiển thị cửa sổ dự đoán với tên đăng nhập


# Hàm đăng ký tài khoản
def Reg():
    username = entry_username.get()
    password = entry_password.get()
    phone = entry_phone.get()

    if username == "" or password == "" or phone=="":
        messagebox.showerror("Cảnh báo", "Vui lòng nhập tên đăng nhập, mật khẩu, số điện thoại")
    else:
        # Kiểm tra xem tên đăng nhập đã tồn tại trong cơ sở dữ liệu chưa
        cursor = conn.cursor()
        query = "SELECT * FROM TaiKhoan WHERE TenDangNhap=?"
        params = (username,)
        result = cursor.execute(query, params).fetchone()
        if result:
            messagebox.showerror("Lỗi", "Tên đăng nhập đã tồn tại!")
        else:
            # Tạo mới tài khoản trong cơ sở dữ liệu
            query = "INSERT INTO TaiKhoan (TenDangNhap, MatKhau, SoDienThoai) VALUES (?, ?, ?)"
            params = (username, password, phone)
            cursor.execute(query, params)
            cursor.commit()
            messagebox.showinfo("Thông báo", "Đăng ký thành công!")
        cursor.close()


# Tạo nút Đăng ký


# Hàm kiểm tra thông tin đăng nhập trong cơ sở dữ liệu
def kiem_tra_dang_nhap(username, password):
    cursor = conn.cursor()
    query = "SELECT * FROM TaiKhoan WHERE TenDangNhap=? AND MatKhau=?"
    params = (username, password)
    result = cursor.execute(query, params).fetchone()
    cursor.close()

    if result:
        return True
    else:
        return False

# Tạo giao diện đăng nhập
label_username = tk.Label(login_window, text="Tên đăng nhập")
label_username.pack()
entry_username = tk.Entry(login_window)
entry_username.pack()

label_password = tk.Label(login_window, text="Mật khẩu")
label_password.pack()
entry_password = tk.Entry(login_window, show="*")
entry_password.pack()

label_phone = tk.Label(login_window, text="Số điện thoại")
label_phone.pack()
entry_phone = tk.Entry(login_window)
entry_phone.pack()

button_login = tk.Button(login_window, text="Đăng nhập", command=login, bg="#5783db", fg="white",font=("Arial", 12, "bold"), width=15)
button_login.pack(pady=10)

button_register = tk.Button(login_window, text="Đăng ký", command=Reg, bg="#55c2da",fg="white",font=("Arial", 10, "bold"))
button_register.pack(pady=10)

# Để tạo khoảng cách ngang giữa hai nút, bạn có thể sử dụng tham số padx để đặt giá trị khoảng cách (theo đơn vị pixel)
button_login.pack(pady=10)
button_register.pack(pady=10)

def show_admin_window():
    admin_window = tk.Tk()
    admin_window.title("Form quản trị")

    # Tạo Treeview để hiển thị dữ liệu
    treeview = tk.ttk.Treeview(admin_window)
    treeview.pack()

    # Thiết lập cột cho Treeview
    treeview["columns"] = ("TenDangNhap", "Ngay", "Tuoi", "Sex", "ALB", "ALP", "ALT", "AST", "BIL", "CHE", "CHOL", "CREA", "GGT", "PROT", "KetQuaDuDoan")
    treeview.column("#0", width=0, stretch=tk.NO)  # Ẩn cột đầu tiên
    treeview.column("TenDangNhap", width=100, anchor=tk.W)
    treeview.column("Ngay", width=100, anchor=tk.W)
    treeview.column("Tuoi", width=50, anchor=tk.CENTER)
    treeview.column("Sex", width=50, anchor=tk.CENTER)
    treeview.column("ALB", width=50, anchor=tk.CENTER)
    treeview.column("ALP", width=50, anchor=tk.CENTER)
    treeview.column("ALT", width=50, anchor=tk.CENTER)
    treeview.column("AST", width=50, anchor=tk.CENTER)
    treeview.column("BIL", width=50, anchor=tk.CENTER)
    treeview.column("CHE", width=50, anchor=tk.CENTER)
    treeview.column("CHOL", width=50, anchor=tk.CENTER)
    treeview.column("CREA", width=50, anchor=tk.CENTER)
    treeview.column("GGT", width=50, anchor=tk.CENTER)
    treeview.column("PROT", width=50, anchor=tk.CENTER)
    treeview.column("KetQuaDuDoan", width=100, anchor=tk.W)

    # Đặt tiêu đề cho các cột
    treeview.heading("TenDangNhap", text="Tên đăng nhập")
    treeview.heading("Ngay", text="Ngày")
    treeview.heading("Tuoi", text="Tuổi")
    treeview.heading("Sex", text="Giới tính")
    treeview.heading("ALB", text="ALB")
    treeview.heading("ALP", text="ALP")
    treeview.heading("ALT", text="ALT")
    treeview.heading("AST", text="AST")
    treeview.heading("BIL", text="BIL")
    treeview.heading("CHE", text="CHE")
    treeview.heading("CHOL", text="CHOL")
    treeview.heading("CREA", text="CREA")
    treeview.heading("GGT", text="GGT")
    treeview.heading("PROT", text="PROT")
    treeview.heading("KetQuaDuDoan", text="Kết quả dự đoán")

    # Lấy dữ liệu từ bảng SucKhoe
    cursor = conn.cursor()
    query = "SELECT * FROM SucKhoe"
    result = cursor.execute(query).fetchall()
    cursor.close()

    # Hiển thị dữ liệu trên Treeview
    for row in result:

        ketqua = str(row[-1])
        treeview.insert("", tk.END, values=row[:-1] + (ketqua,))


    tree = ttk.Treeview(admin_window)
    tree["columns"] = ("TenDangNhap", "SoDienThoai")
    tree.heading("TenDangNhap", text="Tên đăng nhập")
    tree.heading("SoDienThoai", text="Số điện thoại")

    # Lấy dữ liệu từ bảng TaiKhoan
    cursor = conn.cursor()
    query = "SELECT TenDangNhap, SoDienThoai FROM TaiKhoan"
    result = cursor.execute(query).fetchall()
    cursor.close()

    # Hiển thị dữ liệu từ bảng TaiKhoan trong Treeview
    for row in result:
        tree.insert("", "end", values=(row[0], row[1]))

    # Hiển thị Treeview trong form quản trị
    tree.pack()

    admin_window.mainloop()


# Hàm hiển thị cửa sổ dự đoán
def show_predict_window(username):
    # Tạo cửa sổ giao diện dự đoán viêm gan C
    predict_window = tk.Tk()
    predict_window.title('Chuẩn đoán viêm gan C')

    chart_frame = tk.Frame(predict_window)
    chart_frame.grid(row=0, column=3, rowspan=15)

    # Load Model
    HepatitisC_model = pickle.load(open('viemganc_SVM.sav', 'rb'))

    # Hàm hiển thị biểu đồ cột
    # Hàm hiển thị biểu đồ cột

    # Hàm xử lý sự kiện khi nhấn nút "Dự đoán"

    def predict():

        if any([
            not entry_age.get(),
            not entry_gender.get(),
            not entry_alb.get(),
            not entry_alp.get(),
            not entry_alt.get(),
            not entry_ast.get(),
            not entry_bil.get(),
            not entry_che.get(),
            not entry_chol.get(),
            not entry_crea.get(),
            not entry_ggt.get(),
            not entry_prot.get()
        ]):
            messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return
        Age = float(entry_age.get())
        Gender = float(entry_gender.get())
        ALB = float(entry_alb.get())
        ALP = float(entry_alp.get())
        ALT = float(entry_alt.get())
        AST = float(entry_ast.get())
        BIL = float(entry_bil.get())
        CHE = float(entry_che.get())
        CHOL = float(entry_chol.get())
        CREA = float(entry_crea.get())
        GGT = float(entry_ggt.get())
        PROT = float(entry_prot.get())

        hepa_prediction = HepatitisC_model.predict([[Age, Gender, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT]])

        if hepa_prediction[0] == 0:
            dudoan = 'Không bị viêm gan C'
        else:
            dudoan = 'Bị viêm gan C'

        result_label.config(text=dudoan)
        cursor = conn.cursor()
        query = "INSERT INTO SucKhoe (TenDangNhap, Ngay, Tuoi, Sex, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT, KetQuaDuDoan) VALUES (?, GETDATE(), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        params = (username, Age, Gender, ALB, ALP, ALT, AST, BIL, CHE, CHOL, CREA, GGT, PROT, dudoan)

        cursor.execute(query, params)
        cursor.commit()
        cursor.close()



    # Tạo các thành phần giao diện dự đoán
    label_age = tk.Label(predict_window, text='Nhập tuổi của bạn.')
    label_age.grid(row=1, column=0, columnspan=2)

    label_username = tk.Label(predict_window, text="Tên đăng nhập: " + username)
    label_username.grid(row=0, column=0, columnspan=2)

    label_gender = tk.Label(predict_window, text='Nhập giới tính của bạn: 0(nam) 1(nữ)')
    label_gender.grid(row=2, column=0, columnspan=2)

    label_alb = tk.Label(predict_window, text='Nhập giá trị ALB')
    label_alb.grid(row=3, column=0, columnspan=2)

    label_alp = tk.Label(predict_window, text='Nhập giá trị ALP')
    label_alp.grid(row=4, column=0, columnspan=2)

    label_alt = tk.Label(predict_window, text='Nhập giá trị ALT')
    label_alt.grid(row=5, column=0, columnspan=2)

    label_ast = tk.Label(predict_window, text='Nhập giá trị AST')
    label_ast.grid(row=6, column=0, columnspan=2)

    label_bil = tk.Label(predict_window, text='Nhập giá trị BIL')
    label_bil.grid(row=7, column=0, columnspan=2)

    label_che = tk.Label(predict_window, text='Nhập giá trị CHE')
    label_che.grid(row=8, column=0, columnspan=2)

    label_chol = tk.Label(predict_window, text='Nhập giá trị CHOL')
    label_chol.grid(row=9, column=0, columnspan=2)

    label_crea = tk.Label(predict_window, text='Nhập giá trị CREA')
    label_crea.grid(row=10, column=0, columnspan=2)

    label_ggt = tk.Label(predict_window, text='Nhập giá trị GGT')
    label_ggt.grid(row=11, column=0, columnspan=2)

    label_prot = tk.Label(predict_window, text='Nhập giá trị PROT')
    label_prot.grid(row=12, column=0, columnspan=2)

    entry_age = tk.Entry(predict_window)
    entry_age.grid(row=1, column=2)

    entry_gender = tk.Entry(predict_window)
    entry_gender.grid(row=2, column=2)

    entry_alb = tk.Entry(predict_window)
    entry_alb.grid(row=3, column=2)

    entry_alp = tk.Entry(predict_window)
    entry_alp.grid(row=4, column=2)

    entry_alt = tk.Entry(predict_window)
    entry_alt.grid(row=5, column=2)

    entry_ast = tk.Entry(predict_window)
    entry_ast.grid(row=6, column=2)

    entry_bil = tk.Entry(predict_window)
    entry_bil.grid(row=7, column=2)

    entry_che = tk.Entry(predict_window)
    entry_che.grid(row=8, column=2)

    entry_chol = tk.Entry(predict_window)
    entry_chol.grid(row=9, column=2)

    entry_crea = tk.Entry(predict_window)
    entry_crea.grid(row=10, column=2)

    entry_ggt = tk.Entry(predict_window)
    entry_ggt.grid(row=11, column=2)

    entry_prot = tk.Entry(predict_window)
    entry_prot.grid(row=12, column=2)

    button_predict = tk.Button(predict_window, text='Dự đoán', command=predict)
    button_predict.grid(row=13, column=0, columnspan=3)

    result_label = tk.Label(predict_window, text='')
    result_label.grid(row=14, column=0, columnspan=3)



    # Bắt đầu chạy ứng dụng dự đoán
    predict_window.mainloop()

# Bắt đầu chạy ứng dụng đăng nhập
login_window.mainloop()
