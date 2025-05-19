import tkinter as tk
from tkinter import messagebox
from detection import detect_deadlock
from visualization import draw_graph

class DeadlockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Deadlock Detection Simulator")

        tk.Label(root, text="Enter Edges (e.g., P1->R1, R1->P2, ...)").pack()
        self.entry = tk.Entry(root, width=80)
        self.entry.pack(pady=10)

        tk.Button(root, text="Run Detection", command=self.run).pack(pady=5)

    def run(self):
        edge_text = self.entry.get()
        edges = [e.strip() for e in edge_text.split(',') if '->' in e]
        graph = {}

        for edge in edges:
            u, v = map(str.strip, edge.split('->'))
            graph.setdefault(u, []).append(v)

        wfg = self.to_wait_for_graph(graph)
        is_deadlock = detect_deadlock(wfg)

        # Show popup
        if is_deadlock:
            messagebox.showerror("Deadlock Detected", "⚠️ Deadlock has been detected in the system.")
        else:
            messagebox.showinfo("No Deadlock", "✅ No deadlock detected.")

        draw_graph(graph, is_deadlock)

    def to_wait_for_graph(self, rag):
        wfg = {}
        for u in rag:
            if u.startswith('P'):
                for v in rag[u]:
                    if v.startswith('R'):
                        for p in rag.get(v, []):
                            if p.startswith('P'):
                                wfg.setdefault(u, []).append(p)
        return wfg

if __name__ == "__main__":
    root = tk.Tk()
    app = DeadlockApp(root)
    root.mainloop()
