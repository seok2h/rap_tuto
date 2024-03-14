# 파일 기본
import os

# print("=====================================")
# print(os.getcwd())  # current working directory 현재 작업 공간
# # os.chdir("경로")
# os.chdir("..")  # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..")   # 조부모 폴더로 이동
# print(os.getcwd())  
# os.chdir("c:/") # 주어진 절대 경로로 이동
# print(os.getcwd())

# 파일 경로
# open("파일경로") as f :

# 파일 경로 만들기
# file_path = os.path.join(os.getcwd(), "my_file.txt")  # 절대 경로 가져오기
# print(file_path)
# os.path.join(os.getcwd(), "my_file.txt")

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"경로")) 

# 파일 정보 가져오기
import time
import datetime

# 파일의 생성 날짜
# ctime = os.path.getctime("./2_desktop/test.txt")
# print(ctime)
# # 날짜 정보를 strftime을 통해서 연월일 시분초 형태로 출력
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime("./2_desktop/test.txt")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 마지막 접근 날짜
# atime = os.path.getatime('./2_desktop/test.txt')
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# # 파일 크기
# size = os.path.getsize('./2_desktop/test.txt')  # 바이트 단위로 파일 크기 가져오기
# print(size)

# 파일 목록 가져오기
# print(os.listdir())     # 모든 폴더, 파일 목록 가져오기 =
# print(os.listdir("어떤 경로")) # 주어진 폴더 밑에서 모든 폴더, 파일 목록 가져오기

# 파일 목록 가져오기 (하위 폴더 모두 포함)
# result = os.walk('.')  # 주어진 폴더 밑에 있는 모든 폴더, 파일 목록 가져오기
# print(result)

# for root, dirs, files in result:
#     print(root, dirs, files)

# 만약 폴더 내에서 특정 파일들을 찾으려면 ?
# name = "11_file_system.py"
# result = []
# for root, dirs, files in os.walk('.'):
#     if name in files:
#         result.append(os.path.join(root, name))

# print(result)

# # 마냥ㄱ 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# # .xlsx, *.txt, 자동화*.png
# import fnmatch
# pattern = "*.png"  # .py 로 끝나는 모든 파일
# result = []
# for root, dirs, files in os.walk('.'):
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):  # 이름과 패턴이 일치함녀
#             result.append(os.path.join(root, name))

# print(result)


# 주어진 경로가 파일인지? 폴더인지?
# print(os.path.isdir("1_excel"))
# print(os.path.isfile("1_excel"))

# print(os.path.isdir("test.png"))
# print(os.path.isfile("test.png"))

# # 만약에 지정된 경로가 해당하는 파일 / 폴더가 없다면?
# print(os.path.isfile("runasfksjdf"))    # 파일이 존재하지 않으면 걍 False 반환

# # 주어진 경로가 존재하는지?
# if os.path.exists('../rpa_basic'):
#     print("파일 또는 폴더가 존재합니다.")
# else:
#     print("존재하지 않습니다.")

# 파일 만들기 
# open("new_file.txt", "a").close()   # 빈 파일 생성

# # 파일명 변경하기 =
# os.rename("new_file.txt", "new_file_rename.txt")

# # 파일 삭제하기 =
# os.remove("new_file_rename.txt")

# 폴더 만들기
# os.mkdir("new_folder")    # 현재 경로 기준으로 폴더

# os.makedirs("new_folders/a/b/c/") # 하위 폴더를 가지는 폴더 생성

# 폴더 명 변경하기
# os.rename()

# 폴더 지우기
# os.rmdir("new_folder")    # 폴더 안이 비었을 때만 삭제 가능

import shutil   # shell utilities
# shutil.rmtree("new_folders")        # 폴더 안이 비어 있지 않아도 완전 삭제 가능

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("run_icon.png", "2_desktop")
# shutil.copy("run_icon.png", "2_desktop/modified_run_icon.png")  # 파일명 변경해서 복사 가능

# shutil.copyfile("run_icon.png", "copied.png")   # 원본 파일, 대상 파일만 적을 수 있다.

# shutil.copy2("run_icon.png", "2_desktop/copy2.png")     # 원본 파일 경로, 대상 폴더

# copy, copfile : 메타정보 복사 X (만든, 수정한 날짜 정보)
# copy2 : 메타정보 복사 O

# 폴더 복사
# shutil.copytree("test_folder", "test_folder2")  # 원본 폴더 경로, 대상 폴더 경로
# shutil.copytree("test_folder", "test_folder3")  # 항상 폴더만 입력해야 한다.

# 폴더 이동
# shutil.move("test_folder", "test_folder3")  # 원본 폴더를 test_folder3 안으로 이동
# shutil.move("test_folder2", "test_folder3")
# shutil.move("test_folder3", "test_folder_rename")  # 해당하는 폴더가 없을 때에는 폴더명 변경되는 효과






