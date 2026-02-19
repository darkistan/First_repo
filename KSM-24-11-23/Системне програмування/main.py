# memory_info_windows_stdlib.py
import ctypes

class MEMORYSTATUSEX(ctypes.Structure):
    _fields_ = [
        ("dwLength", ctypes.c_ulong),
        ("dwMemoryLoad", ctypes.c_ulong),
        ("ullTotalPhys", ctypes.c_ulonglong),
        ("ullAvailPhys", ctypes.c_ulonglong),
        ("ullTotalPageFile", ctypes.c_ulonglong),
        ("ullAvailPageFile", ctypes.c_ulonglong),
        ("ullTotalVirtual", ctypes.c_ulonglong),
        ("ullAvailVirtual", ctypes.c_ulonglong),
        ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
    ]

def gib(x: int) -> float:
    return x / (1024 ** 3)

def main() -> None:
    stat = MEMORYSTATUSEX()
    stat.dwLength = ctypes.sizeof(MEMORYSTATUSEX)

    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat)):
        raise OSError("Не вдалося отримати інформацію про пам'ять.")

    used_phys = stat.ullTotalPhys - stat.ullAvailPhys
    used_pagefile = stat.ullTotalPageFile - stat.ullAvailPageFile

    print("=== ОЗП (RAM) ===")
    print(f"Загальний обсяг:  {gib(stat.ullTotalPhys):.2f} GiB")
    print(f"Доступний обсяг:  {gib(stat.ullAvailPhys):.2f} GiB")
    print(f"Використано:      {gib(used_phys):.2f} GiB")
    print(f"Завантаження RAM: {stat.dwMemoryLoad}%")

    print("\n=== Віртуальна пам'ять (Pagefile) ===")
    print(f"Загальний обсяг:  {gib(stat.ullTotalPageFile):.2f} GiB")
    print(f"Доступний обсяг:  {gib(stat.ullAvailPageFile):.2f} GiB")
    print(f"Використано:      {gib(used_pagefile):.2f} GiB")

if __name__ == "__main__":
    main()
