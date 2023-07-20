import tkinter as tk
from tkinter import messagebox
from urllib.parse import urlencode, urljoin, parse_qs, urlparse
import validators

window = tk.Tk()
window.title("URL Builder")
window.configure(background="white")
window.iconbitmap("url_builder.ico")
base_url = tk.StringVar()
url_label = tk.Label(window, text="", font=("Arial", 12, "bold"), bg="white", fg="red")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"600x350+{int(screen_width/2-250)}+{int(screen_height*0.1)}")
window.resizable(False, True)

def estrai_parametri_da_url(url):
    parsed_url = urlparse(url.encode('utf-8'))
    query = parsed_url.query
    parametri = parse_qs(query)
    for p in parametri:
        parametri[p] = parametri[p][0]
    return parametri

def update_height_window():
    new_window_height = 350 + par_frame.__len__()*40
    window.geometry(f"600x{new_window_height}+{int(screen_width/2-250)}+{int(screen_height*0.1)}")

def generate_url():
    parsed_url = validators.url(base_url.get())
    if parsed_url:
        params = get_parameters()
        pra_base_url = estrai_parametri_da_url(base_url.get())
    params.update(pra_base_url)
    print(f"La Url inserita è {base_url.get()} ed è {parsed_url}")
    if parsed_url and params != {}:
        url_with_query_string = urljoin(base_url.get(), '?' + urlencode(params))
        url_label["text"] = url_with_query_string
        view_result()
    elif parsed_url and params == {}:
        messagebox.showerror("Errore", "Nessun parametro valido inserito")
    else:
        messagebox.showerror("Errore", "E' stata inserita un URL non valida")

def get_parameters():
    dic = {}
    for i in range(0,par_frame.__len__()):
        if par_entry[i-1].get() != "":
            dic[par_entry[i-1].get()] = val_entry[i-1].get()
    return dic

def copy_to_clipboard(event):
    window.clipboard_clear()  # Cancella gli appunti precedenti
    window.clipboard_append(url_label["text"])  # Copia il testo della label negli appunti
    messagebox.showinfo("Copia Negli Appunti", "Il testo è stato copiato negli appunti.")

def reset_ui():
    result_frame.pack_forget()
    base_url.set("")
    for i in range(1,par_frame.__len__()):
        par_frame[i].destroy()
    par_entry_str.set("")
    val_entry_str.set("")

def create_frame_0():
    par_frame.append(tk.Frame(parameters_frame, bg="#CCCCCC"))
    par_frame[0].pack(fill=tk.X)
    par_label.append(tk.Label(par_frame[0], text="Parametro: ", font=("Arial", 16, "bold"), bg="#CCC", fg="black"))
    par_label[0].grid(row=0, column=0, padx=10, pady=10)
    par_entry.append(tk.Entry(par_frame[0], width=15, font=("Arial", 16, "bold"),textvariable=par_entry_str))
    par_entry[0].grid(row=0, column=1, padx=10, pady=10)

    val_label.append(tk.Label(par_frame[0], text="valore: ", font=("Arial", 16, "bold"), bg="#CCC", fg="black"))
    val_label[0].grid(row=0, column=2, padx=10, pady=10)
    val_entry.append(tk.Entry(par_frame[0], width=15, font=("Arial", 16, "bold"),textvariable=val_entry_str))
    val_entry[0].grid(row=0, column=3, padx=10, pady=10)
    
def view_result():
    result_frame.pack(fill=tk.X)

def remove_frame(remove_frame):
    print(remove_frame)
    remove_frame = remove_frame
    par_frame[remove_frame].destroy()
    par_entry.remove(par_entry[remove_frame])
    val_entry.remove(val_entry[remove_frame])
    par_frame.remove(par_frame[remove_frame])
    print(par_frame.__len__())
    update_height_window()

def add_parameter():
    int_num = par_frame.__len__()
    par_frame.append(tk.Frame(parameters_frame, bg="#CCCCCC"))
    par_label.append(tk.Label(par_frame[par_frame.__len__()-1], text="Parametro: ", font=("Arial", 16, "bold"), bg="#CCC", fg="black"))
    par_label[par_label.__len__()-1].grid(row=0, column=0, padx=10, pady=10)
    par_entry.append(tk.Entry(par_frame[par_frame.__len__()-1], width=15, font=("Arial", 16, "bold")))
    par_entry[par_entry.__len__()-1].grid(row=0, column=1, padx=10, pady=10)

    val_label.append(tk.Label(par_frame[par_frame.__len__()-1], text="valore: ", font=("Arial", 16, "bold"), bg="#CCC", fg="black"))
    val_label[val_label.__len__()-1].grid(row=0, column=2, padx=10, pady=10)
    val_entry.append(tk.Entry(par_frame[par_frame.__len__()-1], width=15, font=("Arial", 16, "bold")))
    val_entry[val_entry.__len__()-1].grid(row=0, column=3, padx=10, pady=10)
   
    add_button.append(tk.Button(par_frame[par_frame.__len__()-1], image=remove_icon, bg="#CCC", command=lambda: remove_frame(int_num)))
    add_button[add_button.__len__()-1].grid(row=0, column=4, padx=10, pady=10)

    par_frame[par_frame.__len__()-1].pack(fill=tk.X)
    update_height_window()

header_frame = tk.Frame(window, bg="red", height=50)
header_frame.pack(fill=tk.X)
header_label = tk.Label(header_frame, text="Compila i campi sottostanti", font=("Arial", 18, "bold"), bg="red", fg="white")
header_label.pack(fill=tk.X, pady=20)
body_frame = tk.Frame(window, bg="white", height=150)
body_frame.pack(fill=tk.X)
body_label = tk.Label(body_frame, text="BaseURL: ", font=("Arial", 18, "bold"), bg="white", fg="black")
body_label.pack(pady=20, padx=10, side=tk.LEFT)
base_url = tk.StringVar()
base_url.set("https://www.example.com")
body_entry = tk.Entry(body_frame, width=35, font=("Arial", 14, "bold"),textvariable=base_url)
body_entry.pack(side=tk.LEFT)

parameters_frame = tk.Frame(window, bg="red", height=150)
parameters_frame.pack(fill=tk.X)

par_frame = []
par_label = []
par_entry = []
val_label = []
val_entry = []
add_button = []
par_entry_str = tk.StringVar()
val_entry_str = tk.StringVar()


create_frame_0()

remove_icon =tk.PhotoImage(file="remove.png")
remove_icon = remove_icon.subsample(2)

add_icon =tk.PhotoImage(file="add.png")
add_icon = add_icon.subsample(2)
add_button.append(tk.Button(par_frame[0], image=add_icon, bg="#CCC", command=lambda: add_parameter()))
add_button[0].grid(row=0, column=4, padx=10, pady=10)

bottons_frame = tk.Frame(window, bg="white", height=50)
bottons_frame.pack(pady=20)

generate_button = tk.Button(bottons_frame, text="Genera URL", font=("Arial", 14, "bold"), bg="white", fg="black", width=10, height=2, command=generate_url)
generate_button.grid(row=0, column=0, padx=10, pady=10)


reset_button = tk.Button(bottons_frame, text="Reset", font=("Arial", 14, "bold"), bg="white", fg="black", width=10, height=2,command=reset_ui)
reset_button.grid(row=0, column=1, padx=10, pady=10)



result_frame = tk.Frame(window, bg="red", height=250)
# result_frame.pack(fill=tk.X)
result_label = tk.Label(result_frame, text="URL generata: ", font=("Arial", 18, "bold"), bg="red", fg="white")
result_label.pack(pady=0, padx=10,)
icon = tk.PhotoImage(file="copy_icon.png")

url_label = tk.Label(result_frame,text=" ",width=55, wraplength=590, font=("Arial", 16, "bold"), bg="red", fg="white")
url_label.pack(pady=10, padx=10, side=tk.LEFT)
url_label.bind("<Button-1>", copy_to_clipboard)
url_label.bind("<Button-2>", copy_to_clipboard)
url_label.bind("<Button-3>", copy_to_clipboard)

icon = tk.PhotoImage(file="copy_icon.png")
icon = icon.subsample(2)
icon_label = tk.Label(result_frame, image=icon, bg="red")
icon_label.pack(side=tk.LEFT)
icon_label.bind("<Button-1>", copy_to_clipboard)
icon_label.bind("<Button-2>", copy_to_clipboard)
icon_label.bind("<Button-3>", copy_to_clipboard)


window.mainloop()
