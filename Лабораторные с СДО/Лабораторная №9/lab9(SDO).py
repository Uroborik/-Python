import socket
import threading
import tkinter as tk

PORT = 9000


class Messenger(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.conn = None
        self.pack(fill=tk.BOTH, expand=1)
        self.init_ui()

    def init_ui(self):
        self.chat = tk.Text(self, state=tk.DISABLED, height=15)
        self.chat.pack(fill=tk.BOTH, expand=1)

        self.entry = tk.Entry(self)
        self.entry.pack(fill=tk.X)
        tk.Button(self, text="Отправить", command=self.send).pack(fill=tk.X)

        self.ip = tk.Entry(self)
        self.ip.insert(0, "127.0.0.1")
        self.ip.pack(fill=tk.X)
        tk.Button(self, text="Создать чат (сервер)", command=self.start_server).pack(fill=tk.X)
        tk.Button(self, text="Подключиться (клиент)", command=self.start_client).pack(fill=tk.X)

    def show(self, text):
        self.chat.config(state=tk.NORMAL)
        self.chat.insert(tk.END, text + "\n")
        self.chat.config(state=tk.DISABLED)

    def start_server(self):
        self.show(f"Ожидание подключения на порту {PORT}...")
        threading.Thread(target=self._server, daemon=True).start()

    def _server(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(("0.0.0.0", PORT))
        server.listen(1)
        self.conn, addr = server.accept()
        self.show("Подключился " + addr[0])
        self.receive()

    def start_client(self):
        threading.Thread(target=self._client, daemon=True).start()

    def _client(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((self.ip.get(), PORT))
        self.show("Подключено к " + self.ip.get())
        self.receive()

    def receive(self):
        while True:
            data = self.conn.recv(1024)
            if not data:
                break
            self.show("Собеседник: " + data.decode("utf-8"))

    def send(self):
        text = self.entry.get()
        if self.conn and text:
            self.conn.sendall(text.encode("utf-8"))
            self.show("Я: " + text)
            self.entry.delete(0, tk.END)


root = tk.Tk()
root.title("Мессенджер")
root.geometry("400x400")
Messenger(root)
root.mainloop()
