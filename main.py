"""Chương trình quản lý sinh viên dòng lệnh."""
import os

from manager import StudentManager
from student import Student

DATA_FILE = os.path.join("data", "sample.json")

MENU = """
===== QUAN LY SINH VIEN =====
1. Xem danh sach
2. Them sinh vien
3. Xoa sinh vien
4. Tim theo ma
5. Tim theo ten
6. Thong ke (GPA trung binh, thu khoa)
0. Thoat va luu
Chon: """


def show(students):
    if not students:
        print("(trong)")
    for s in students:
        print(s)


def main():
    manager = StudentManager()
    if os.path.exists(DATA_FILE):
        manager.load(DATA_FILE)

    while True:
        choice = input(MENU).strip()
        try:
            if choice == "1":
                show(manager.students)
            elif choice == "2":
                sid = input("Ma SV: ").strip()
                name = input("Ten: ").strip()
                gpa = float(input("GPA (0-10): "))
                manager.add_student(Student(sid, name, gpa))
                print("Da them.")
            elif choice == "3":
                ok = manager.remove_student(input("Ma SV can xoa: ").strip())
                print("Da xoa." if ok else "Khong tim thay.")
            elif choice == "4":
                s = manager.find_by_id(input("Ma SV: ").strip())
                print(s if s else "Khong tim thay.")
            elif choice == "5":
                show(manager.search_by_name(input("Tu khoa: ")))
            elif choice == "6":
                print("GPA trung binh:", manager.average_gpa())
                print("Thu khoa:", manager.top_student())
            elif choice == "0":
                manager.save(DATA_FILE)
                print("Da luu. Tam biet!")
                break
            else:
                print("Lua chon khong hop le.")
        except ValueError as e:
            print("Loi:", e)


if __name__ == "__main__":
    main()
