import psutil
import tkinter

root = tkinter.Tk()
root.title("System Monitor")

cpu_label = tkinter.Label(root, text="CPU Usage: ", font=("Arial", 14))
cpu_label.pack(pady=10)
cpu_label.pack(padx=10)

mem_label = tkinter.Label(root, text="Memory Usage: ", font=("Arial", 14))
mem_label.pack(pady=10)
mem_label.pack(padx=10)


def update_stats():
    cpu_usage = psutil.cpu_percent(interval=0.5)
    mem_usage = psutil.virtual_memory().percent

    cpu_label.config(text=f"CPU Usage: {cpu_usage}%")
    mem_label.config(text=f"Memory Usage: {mem_usage}%")

    # refresh every 1000 ms
    root.after(1000, update_stats)


update_stats()
root.mainloop()
