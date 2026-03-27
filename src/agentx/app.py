"""AgentX - AI Chat GUI Application."""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from datetime import datetime


class AgentXApp:
    """Main application window."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("AgentX - AI Assistant")
        self.root.geometry("800x600")
        self.root.minsize(600, 400)

        # Configure colors
        self.colors = {
            "bg": "#1a1a2e",
            "fg": "#eaeaea",
            "accent": "#4a90d9",
            "user_bg": "#2d3748",
            "ai_bg": "#1e3a5f",
            "input_bg": "#2d2d44",
            "button": "#4a90d9",
        }

        self.root.configure(bg=self.colors["bg"])

        self._setup_styles()
        self._create_widgets()
        self._bind_events()

    def _setup_styles(self):
        """Configure ttk styles."""
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "Dark.TFrame",
            background=self.colors["bg"],
        )
        style.configure(
            "Dark.TLabel",
            background=self.colors["bg"],
            foreground=self.colors["fg"],
            font=("Segoe UI", 10),
        )
        style.configure(
            "Title.TLabel",
            background=self.colors["bg"],
            foreground=self.colors["accent"],
            font=("Segoe UI", 16, "bold"),
        )
        style.configure(
            "Send.TButton",
            background=self.colors["button"],
            foreground="white",
            font=("Segoe UI", 10, "bold"),
            padding=(20, 10),
        )

    def _create_widgets(self):
        """Create all GUI widgets."""
        # Main container
        main_frame = ttk.Frame(self.root, style="Dark.TFrame", padding=10)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Header
        header_frame = ttk.Frame(main_frame, style="Dark.TFrame")
        header_frame.pack(fill=tk.X, pady=(0, 10))

        title = ttk.Label(
            header_frame,
            text="🤖 AgentX AI Assistant",
            style="Title.TLabel",
        )
        title.pack(side=tk.LEFT)

        clear_btn = tk.Button(
            header_frame,
            text="Clear Chat",
            command=self._clear_chat,
            bg=self.colors["input_bg"],
            fg=self.colors["fg"],
            relief=tk.FLAT,
            padx=15,
            pady=5,
        )
        clear_btn.pack(side=tk.RIGHT)

        # Chat display area
        chat_frame = ttk.Frame(main_frame, style="Dark.TFrame")
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            bg=self.colors["bg"],
            fg=self.colors["fg"],
            font=("Consolas", 11),
            relief=tk.FLAT,
            padx=10,
            pady=10,
            state=tk.DISABLED,
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)

        # Configure text tags for styling
        self.chat_display.tag_configure(
            "user",
            background=self.colors["user_bg"],
            foreground="#90cdf4",
            spacing1=5,
            spacing3=5,
            lmargin1=10,
            lmargin2=10,
            rmargin=10,
        )
        self.chat_display.tag_configure(
            "ai",
            background=self.colors["ai_bg"],
            foreground="#68d391",
            spacing1=5,
            spacing3=5,
            lmargin1=10,
            lmargin2=10,
            rmargin=10,
        )
        self.chat_display.tag_configure(
            "timestamp",
            foreground="#718096",
            font=("Consolas", 9),
        )

        # Input area
        input_frame = ttk.Frame(main_frame, style="Dark.TFrame")
        input_frame.pack(fill=tk.X)

        self.input_field = tk.Text(
            input_frame,
            height=3,
            bg=self.colors["input_bg"],
            fg=self.colors["fg"],
            font=("Consolas", 11),
            relief=tk.FLAT,
            padx=10,
            pady=10,
            insertbackground=self.colors["fg"],
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        send_btn = tk.Button(
            input_frame,
            text="Send ➤",
            command=self._send_message,
            bg=self.colors["button"],
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief=tk.FLAT,
            padx=25,
            pady=15,
            cursor="hand2",
        )
        send_btn.pack(side=tk.RIGHT, fill=tk.Y)

        # Welcome message
        self._add_ai_message(
            "Hello! I'm AgentX, your AI assistant. How can I help you today?\n\n"
            "I'm running as a native compiled binary - no Python source exposed!"
        )

    def _bind_events(self):
        """Bind keyboard events."""
        self.input_field.bind("<Return>", self._on_enter)
        self.input_field.bind("<Shift-Return>", self._on_shift_enter)

    def _on_enter(self, event):
        """Handle Enter key - send message."""
        self._send_message()
        return "break"  # Prevent newline

    def _on_shift_enter(self, event):
        """Handle Shift+Enter - new line."""
        pass  # Allow default behavior

    def _send_message(self):
        """Send user message and get AI response."""
        message = self.input_field.get("1.0", tk.END).strip()
        if not message:
            return

        # Clear input
        self.input_field.delete("1.0", tk.END)

        # Add user message
        self._add_user_message(message)

        # Generate AI response (placeholder - add your AI logic here)
        response = self._generate_response(message)
        self._add_ai_message(response)

    def _add_user_message(self, message: str):
        """Add a user message to the chat."""
        self._add_message("You", message, "user")

    def _add_ai_message(self, message: str):
        """Add an AI message to the chat."""
        self._add_message("AgentX", message, "ai")

    def _add_message(self, sender: str, message: str, tag: str):
        """Add a message to the chat display."""
        self.chat_display.configure(state=tk.NORMAL)

        timestamp = datetime.now().strftime("%H:%M")
        header = f"\n[{timestamp}] {sender}:\n"

        self.chat_display.insert(tk.END, header, "timestamp")
        self.chat_display.insert(tk.END, f"{message}\n", tag)

        self.chat_display.configure(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def _generate_response(self, user_message: str) -> str:
        """Generate AI response. Replace with actual AI logic."""
        # Placeholder responses - integrate your AI here
        user_lower = user_message.lower()

        if "hello" in user_lower or "hi" in user_lower:
            return "Hello! Great to chat with you. What would you like to know?"

        if "help" in user_lower:
            return (
                "I can help you with:\n"
                "• Answering questions\n"
                "• Having conversations\n"
                "• Providing information\n\n"
                "Just type your message and press Enter!"
            )

        if "who are you" in user_lower or "what are you" in user_lower:
            return (
                "I'm AgentX, a native compiled AI assistant.\n\n"
                "Built with Python + Tkinter, compiled to machine code with Nuitka.\n"
                "No source files visible - just pure native binary!"
            )

        if "bye" in user_lower or "goodbye" in user_lower:
            return "Goodbye! Have a great day! 👋"

        # Default response
        return (
            f"You said: \"{user_message}\"\n\n"
            "This is a placeholder response. Connect me to an AI backend "
            "(OpenAI, Anthropic, local LLM, etc.) for real intelligence!"
        )

    def _clear_chat(self):
        """Clear the chat history."""
        self.chat_display.configure(state=tk.NORMAL)
        self.chat_display.delete("1.0", tk.END)
        self.chat_display.configure(state=tk.DISABLED)
        self._add_ai_message("Chat cleared. How can I help you?")


def main():
    """Launch the AgentX application."""
    root = tk.Tk()

    # Set icon if available
    try:
        root.iconbitmap("icon.ico")
    except tk.TclError:
        pass

    app = AgentXApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
