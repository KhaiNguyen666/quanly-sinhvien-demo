"""Quản lý danh sách sinh viên: thêm, xóa, tìm kiếm, thống kê, lưu/đọc JSON."""
import json
import os

from student import Student


class StudentManager:
    def __init__(self):
        self.students = []

    # ----- Thêm / xóa -----
    def add_student(self, student):
        if self.find_by_id(student.student_id) is not None:
            raise ValueError(f"Mã sinh viên {student.student_id} đã tồn tại")
        self.students.append(student)

    def remove_student(self, student_id):
        student = self.find_by_id(student_id)
        if student is None:
            return False
        self.students.remove(student)
        return True

    # ----- Tìm kiếm -----
    def find_by_id(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None

    def search_by_name(self, keyword):
        keyword = keyword.lower()
        return [s for s in self.students if keyword in s.name.lower()]

    # ----- Thống kê -----
    def average_gpa(self):
        if not self.students:
            return 0.0
        return round(sum(s.gpa for s in self.students) / len(self.students), 2)

    def top_student(self):
        if not self.students:
            return None
        return max(self.students, key=lambda s: s.gpa)

    def sorted_by_gpa(self, descending=True):
        return sorted(self.students, key=lambda s: s.gpa, reverse=descending)

    # ----- Lưu / đọc tệp JSON -----
    def save(self, path):
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump([s.to_dict() for s in self.students], f,
                      ensure_ascii=False, indent=2)

    def load(self, path):
        with open(path, "r", encoding="utf-8") as f:
            self.students = [Student.from_dict(d) for d in json.load(f)]
