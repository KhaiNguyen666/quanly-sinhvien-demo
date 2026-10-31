"""Lớp Student: biểu diễn một sinh viên."""
from dataclasses import dataclass, asdict


@dataclass
class Student:
    student_id: str
    name: str
    gpa: float

    def __post_init__(self):
        if not self.student_id:
            raise ValueError("Mã sinh viên không được để trống")
        if not self.name:
            raise ValueError("Tên sinh viên không được để trống")
        if not 0.0 <= self.gpa <= 10.0:
            raise ValueError("Điểm GPA phải nằm trong khoảng 0 đến 10")

    def to_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data):
        return cls(data["student_id"], data["name"], float(data["gpa"]))

    def __str__(self):
        return f"{self.student_id} | {self.name} | GPA: {self.gpa}"
