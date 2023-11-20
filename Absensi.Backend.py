from tkinter import *
from openpyxl import Workbook
from openpyxl.styles import Font,Alignment,Border,Side
from tkinter import font as tkfont
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root =tk.Tk()
root.title ("Absensi Siswa")
workbook = Workbook()
sheet = workbook.active

styling = tkfont.Font(family="Poppins", weight="bold", size=20,)
styling2 = tkfont.Font(family="Times New Roman", size=12)
styling3 = tkfont.Font(family="Tahoma", size=15)
alignment=Alignment(horizontal="center", vertical="center")

font= Font(bold=True)
border= Border (left=Side(border_style="thin", color="00000000"),
                right=Side(border_style="thin", color="00000000"),
                top=Side(border_style="thin", color="00000000"),
                bottom=Side(border_style="thin", color="00000000")
                )

alignment=Alignment(horizontal="center", vertical="center")

HEIGHT = 700
WIDTH = 2000

image_path = "Image/Belakang2.jpg"  # Replace with the actual path to your image file
img = Image.open(image_path)
img = ImageTk.PhotoImage(img)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

canvas.create_image(0, 0, anchor=tk.NW, image=img)

sheet["A1"] = "Mata Pelajaran\t:"
A1 = sheet["A1"]
A1.font = font

sheet["A2"] = "Tanggal\t:"
A2 = sheet["A2"]
A2.font = font

sheet["A3"] = "NO\t:"
A3 = sheet["A3"]
A3.font = font
A3.border = border
A3.alignment = alignment

sheet["B3"] = "NAMA\t:"
B3 = sheet["B3"]
B3.font = font
B3.border = border
B3.alignment = alignment

sheet["C3"] = "NISN\t:"
C3 = sheet["C3"]
C3.font = font
C3.border = border
C3.alignment = alignment

sheet["D3"] = "KELAS\t:"
D3 = sheet["D3"]
D3.font = font
D3.border = border
D3.alignment = alignment

sheet["E3"] = "JURUSAN\t:"
E3 = sheet["E3"]
E3.font = font
E3.border = border
E3.alignment = alignment

num=0

def InsertData():
    global num
    num = num+1
    sheetnum = num + 3

    sheet["A"+str(sheetnum)] = num
    DataNo = sheet["A"+str(sheetnum)]
    DataNo.border = border
    DataNo.alignment = alignment

    sheet["B"+str(sheetnum)] = Namaentry.get()
    DataNama = sheet["B"+str(sheetnum)]
    DataNama.border = border
    DataNama.alignment = alignment

    sheet["C"+str(sheetnum)] = NISNentry.get()
    DataNISN = sheet["C"+str(sheetnum)]
    DataNISN.border = border
    DataNISN.alignment = alignment

    sheet["D"+str(sheetnum)] = Kelasentry.get()
    DataKelas = sheet["D"+str(sheetnum)]
    DataKelas.border = border
    DataKelas.alignment = alignment

    sheet["E"+str(sheetnum)] = Jurusanentry.get()
    DataJurusan = sheet["E"+str(sheetnum)]
    DataJurusan.border = border
    DataJurusan.alignment = alignment

    sheet["B1"] = mapelentry.get()
    sheet["B2"] = tanggalentry.get()

    treeview.insert("", "end", values=(num, Namaentry.get(), NISNentry.get(), Kelasentry.get(), Jurusanentry.get()))

    Namaentry.delete(0, END)
    NISNentry.delete(0, END)

def SaveData():
    global Informasi
    workbook.save(filename=str(mapelentry.get())+"_"+str(tanggalentry.get())+".xlsx")
    Informasi["text"] = "Data Absen Telah Di Simpan\nNama file:" + str(mapelentry.get())+"_"+str(tanggalentry.get())+".xlsx"

def CreateNewData():
    global Informasi , num
    Informasi["text"] = "HALO👋, Masukan Data Diri Kamu Kemudian Klick Insert Ya..., Semangat🫶"
    Namaentry.delete(0, END)
    NISNentry.delete(0, END)
    Kelasentry.delete(0, END)
    Jurusanentry.delete(0, END)
    mapelentry.delete(0, END)
    tanggalentry.delete(0, END)
    for item in treeview.get_children():
        treeview.delete(item)
    num = 0

frameJudul = Frame(root)
frameJudul.place(rely=0.025, relx=0.5, relheight=0.1, relwidth=1, anchor='n')
judul = Label(frameJudul,bg="white", text="Absensi Siswa", font=styling)
judul.place(relheight=1, relwidth=1)

frameMapel = Frame(root)
frameMapel.place(rely=0.15, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
mapelinfo = Label(frameMapel,bg="white", text="Mata Pelajaran", font=styling2)
mapelinfo.place(relwidth=0.4, relheight=1 )
mapelentry = Entry(frameMapel)
mapelentry.place(relx=0.4, relheight=1, relwidth=0.6)
mapelentry.get()

frameTanggal = Frame(root)
frameTanggal.place(rely=0.22, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
tanggalinfo = Label(frameTanggal,bg="white", text="Tanggal", font=styling2)
tanggalinfo.place(relwidth=0.4, relheight=1 )
tanggalentry = Entry(frameTanggal)
tanggalentry.place(relx=0.4, relheight=1, relwidth=0.6)
tanggalentry.get()

frameNama = Frame(root)
frameNama.place(rely=0.29, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
Namainfo = Label(frameNama, bg="white", text="Nama Siswa", font=styling2)
Namainfo.place(relwidth=0.4, relheight=1 )
Namaentry = Entry(frameNama)
Namaentry.place(relx=0.4, relheight=1, relwidth=0.6)
Namaentry.get()

frameNISN = Frame(root)
frameNISN.place(rely=0.36, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
NISNinfo = Label(frameNISN,bg="white", text="NISN", font=styling2)
NISNinfo.place(relwidth=0.4, relheight=1 )
NISNentry = Entry(frameNISN)
NISNentry.place(relx=0.4, relheight=1, relwidth=0.6)
NISNentry.get()

frameKelas = Frame(root)
frameKelas.place(rely=0.43, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
Kelasinfo = Label(frameKelas,bg="white", text="Kelas", font=styling2)
Kelasinfo.place(relwidth=0.4, relheight=1 )
Kelasentry = Entry(frameKelas)
Kelasentry.place(relx=0.4, relheight=1, relwidth=0.6)
Kelasentry.get()

frameJurusan = Frame(root)
frameJurusan.place(rely=0.50, relx=0.5, relheight=0.06, relwidth=0.8, anchor='n')
Jurusaninfo = Label(frameJurusan,bg="white", text="Jurusan", font=styling2)
Jurusaninfo.place(relwidth=0.4, relheight=1 )
Jurusanentry = Entry(frameJurusan)
Jurusanentry.place(relx=0.4, relheight=1, relwidth=0.6)
Jurusanentry.get()

Informasi = Label(root, bg='white', font=styling3, text="HALO👋, Masukan Data Diri Kamu kemudian Klick Insert Ya...., Semangat🫶")
Informasi.place(rely=0.58, relx=0.5, relheight=0.1, relwidth=0.8, anchor='n')

frameButton = Frame(root, bg='white')
frameButton.place(rely=0.72, relx=0.5, relheight=0.05, relwidth=0.19, anchor='center')

insert = Button(frameButton, text="Insert", command=InsertData)
insert.place(rely=0, relx=0.5, relheight=0.25, relwidth=1, anchor='center')
insert.pack(side="left", padx=10)

Save = Button(frameButton, text="Save", command=SaveData)
Save.place(rely=0.25, relx=0.5, relheight=0.25, relwidth=1, anchor='center')
Save.pack(side="left",padx=10)

CreateNew = Button(frameButton, text="Create New", command=CreateNewData)
CreateNew.place(rely=0.5, relx=0.5, relheight=0.25, relwidth=1, anchor='center')
CreateNew.pack(side="left", padx=10)

frameButton2 = Frame(root, bg='white')
frameButton2.place(rely=0.77, relx=0.5, relheight=0.16, relwidth=0.8, anchor='n')

columns = ("NO", "NAMA", "NISN", "KELAS", "JURUSAN")
treeview = ttk.Treeview(frameButton2, columns=columns, show="headings")

for col in columns:
    treeview.heading(col, text=col)
    treeview.column(col, anchor=tk.CENTER)

treeview.pack(expand=True, fill=BOTH)

Exit = Button(frameButton, text="Exit", command=root.quit)
Exit.place(rely=0.75, relx=0.5, relheight=0.25, relwidth=1, anchor='center')
Exit.pack(side="left", padx=10)

root.mainloop()