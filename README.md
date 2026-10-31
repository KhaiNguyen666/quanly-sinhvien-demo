# Quản lý sinh viên (dự án mẫu)

Ứng dụng dòng lệnh nhỏ bằng Python, dùng làm dự án mẫu để thử nghiệm Git và SVN
trong đề tài so sánh hệ thống quản lý phiên bản.

## Cấu trúc
| Tệp | Mô tả |
|---|---|
| `main.py` | Menu dòng lệnh |
| `student.py` | Lớp `Student` |
| `manager.py` | Thêm, xóa, tìm kiếm, thống kê, lưu/đọc JSON |
| `data/sample.json` | Dữ liệu mẫu |
| `tests/test_manager.py` | Kiểm thử bằng pytest |

## Cách chạy
```bash
pip install -r requirements.txt
python main.py     # chạy chương trình
pytest             # chạy kiểm thử
```
Yêu cầu: Python 3.8 trở lên.

## Gợi ý dòng để thử xung đột (kịch bản 2)
Trong `manager.py`, hàm `average_gpa` có dòng `return round(..., 2)`.
Cho hai nhánh sửa cùng dòng này khác nhau (ví dụ làm tròn 1 chữ số và 3 chữ số)
rồi hợp nhất để tạo xung đột có chủ đích.
