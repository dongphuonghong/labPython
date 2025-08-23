import os
import re

def rename_java_classes(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".java"):
                old_path = os.path.join(dirpath, filename)

                # Đổi tên file nếu chữ cái đầu đang viết thường
                if filename[0].islower():
                    new_filename = filename[0].upper() + filename[1:]
                else:
                    new_filename = filename

                new_path = os.path.join(dirpath, new_filename)

                # Đọc nội dung file
                with open(old_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # Tìm class declaration
                match = re.search(r"\bclass\s+([A-Za-z_][A-Za-z0-9_]*)", content)
                if match:
                    class_name = match.group(1)
                    if class_name[0].islower():
                        new_class_name = class_name[0].upper() + class_name[1:]
                        content = content.replace(f"class {class_name}", f"class {new_class_name}")
                    else:
                        new_class_name = class_name
                else:
                    new_class_name = None

                # Ghi lại nội dung file (nếu có thay đổi class)
                with open(old_path, "w", encoding="utf-8") as f:
                    f.write(content)

                # Đổi tên file (nếu cần)
                if new_path != old_path:
                    os.rename(old_path, new_path)
                    print(f"Đổi tên file: {old_path} -> {new_path}")
                elif new_class_name and new_class_name != class_name:
                    print(f"Đổi tên class trong file: {old_path}")

# Chạy script
if __name__ == "__main__":
    project_dir = "."   # đổi thành đường dẫn thư mục project của bạn
    rename_java_classes(project_dir)
