import re
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class CNCParsingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CNC Tool Parser")
        self.root.geometry("600x520")
        
        self.current_file_path = ""
        self.tools_results = {}

        # --- Елементи інтерфейсу ---
        self.lbl_file = tk.Label(root, text="Файл не вибрано", fg="blue", wraplength=550, font=("Arial", 10))
        self.lbl_file.pack(pady=10)

        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        self.btn_open = tk.Button(btn_frame, text="Відкрити файл", command=self.select_file, width=20)
        self.btn_open.grid(row=0, column=0, padx=5)

        self.btn_save = tk.Button(btn_frame, text="Зберегти звіт як...", command=self.save_as, width=20, state=tk.DISABLED)
        self.btn_save.grid(row=0, column=1, padx=5)

        # Таблиця
        columns = ("name", "dia")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        self.tree.heading("name", text="Назва інструменту")
        self.tree.heading("dia", text="Діаметр (мм)")
        self.tree.column("name", width=350)
        self.tree.column("dia", width=120, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def extract_cnc_tools(self, file_path):
        # Паттерни для Heidenhain (.H) та Sinumerik (.MPF)
        heid_def = re.compile(r';\s*TOOL DEF\s+(.*?)\s+R([\d.]+)', re.IGNORECASE)
        heid_call = re.compile(r'TOOL CALL\s+"([^"]+)"', re.IGNORECASE)
        sinu_call = re.compile(r'T\s*=\s*"([^"]+)"', re.IGNORECASE)
        dia_comment = re.compile(r'DIA\.-?\s*([\d.]+)\s*MM', re.IGNORECASE)

        tools_data = {}
        last_found_dia = None

        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    dia_match = dia_comment.search(line)
                    if dia_match:
                        last_found_dia = float(dia_match.group(1))
                    
                    def_match = heid_def.search(line)
                    if def_match:
                        name = def_match.group(1).strip()
                        tools_data[name] = {'dia': float(def_match.group(2)) * 2}
                    
                    call_match = heid_call.search(line) or sinu_call.search(line)
                    if call_match:
                        name = call_match.group(1).strip()
                        if name not in tools_data:
                            tools_data[name] = {'dia': last_found_dia}
                        last_found_dia = None
            return tools_data
        except Exception as e:
            return str(e)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Виберіть файл ЧПК",
            filetypes=[("CNC Files", "*.H *.MPF *.txt"), ("All files", "*.*")]
        )
        if file_path:
            self.current_file_path = file_path
            self.lbl_file.config(text=f"Відкрито: {os.path.basename(file_path)}")
            
            results = self.extract_cnc_tools(file_path)
            if isinstance(results, dict):
                self.tools_results = results
                self.update_table(results)
                self.btn_save.config(state=tk.NORMAL)
            else:
                messagebox.showerror("Помилка", f"Не вдалося прочитати файл: {results}")

    def update_table(self, data):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for name, info in data.items():
            dia = f"{info['dia']:.2f}" if info['dia'] else "???"
            self.tree.insert("", "end", values=(name, dia))

    def save_as(self):
        if not self.tools_results:
            return

        # Пропонуємо назву файлу за замовчуванням
        original_name = os.path.basename(self.current_file_path)
        default_name = os.path.splitext(original_name)[0] + "_tools.txt"

        # Відкриваємо діалог вибору шляху збереження
        save_path = filedialog.asksaveasfilename(
            title="Зберегти звіт",
            initialfile=default_name,
            defaultextension=".txt",
            filetypes=[("Text documents", "*.txt"), ("All files", "*.*")]
        )

        if save_path:
            try:
                with open(save_path, 'w', encoding='utf-8') as f:
                    f.write(f"ЗВІТ ПО ІНСТРУМЕНТАХ\n")
                    f.write(f"Вихідний файл: {original_name}\n")
                    f.write("-" * 55 + "\n")
                    f.write(f"{'Назва інструменту':<35} | {'Діаметр (мм)':<15}\n")
                    f.write("-" * 55 + "\n")
                    for name, info in self.tools_results.items():
                        dia = f"{info['dia']:.2f}" if info['dia'] else "???"
                        f.write(f"{name:<35} | {dia:<15}\n")
                
                messagebox.showinfo("Успіх", f"Звіт успішно збережено!")
            except Exception as e:
                messagebox.showerror("Помилка збереження", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CNCParsingApp(root)
    root.mainloop()