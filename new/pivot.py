import os

def parse_obj_and_recenter(obj_filename, output_filename):
    vertices = []
    other_lines = []

    # 1️⃣ OBJ 파일 읽기
    with open(obj_filename, 'r') as f:
        for line in f:
            if line.startswith('v '):
                parts = line.strip().split()
                x, y, z = map(float, parts[1:4])
                vertices.append([x, y, z])
            else:
                other_lines.append(line.rstrip('\n'))

    if not vertices:
        print("No vertices found in the OBJ file.")
        return

    # 2️⃣ Center 계산
    xs, ys, zs = zip(*vertices)
    center_x = sum(xs) / len(xs)
    center_y = sum(ys) / len(ys)
    center_z = sum(zs) / len(zs)

    print(f"[INFO] Original Center: ({center_x}, {center_y}, {center_z})")

    # 3️⃣ 모든 vertex 좌표에서 center를 빼서 0,0,0 기준으로 이동
    new_vertices = []
    for x, y, z in vertices:
        new_x = x - center_x
        new_y = y - center_y
        new_z = z - center_z
        new_vertices.append([new_x, new_y, new_z])

    # 4️⃣ 새 .obj 파일 저장
    with open(output_filename, 'w') as f:
        for v in new_vertices:
            f.write(f"v {v[0]} {v[1]} {v[2]}\n")
        for line in other_lines:
            f.write(line + "\n")

    print(f"[SUCCESS] Recentered OBJ saved to {output_filename}")


if __name__ == "__main__":
    input_path = r"C:\Users\my\Desktop\motorcenter.obj"
    output_path = r"C:\Users\my\Desktop\motorcenter_center.obj"

    if os.path.exists(input_path):
        parse_obj_and_recenter(input_path, output_path)
    else:
        print(f"[ERROR] 파일이 존재하지 않습니다: {input_path}")
