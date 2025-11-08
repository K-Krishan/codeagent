from functions.get_files_info import get_files_info

print(get_files_info("Calc", "."))
print(get_files_info("Calc", "pkg"))
print(get_files_info("Calc", "/bin"))
print(get_files_info("Calc", "../"))