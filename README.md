# TextFSM Tester GUI

A simple Tkinter-based GUI for rapidly iterating on [TextFSM](https://github.com/google/textfsm) parsing templates. Paste a device or command output alongside a template to immediately see the parsed rows and iterate quickly on your pattern.

## Requirements

- Python 3.9+ (Tkinter included with most distributions)
- `textfsm` library (`pip install textfsm`)

## Getting started

1. Install the `textfsm` dependency:

   ```bash
   pip install textfsm
   ```

2. Launch the GUI from the project directory:

   ```bash
   python textfsm_tester_GUI.py
   ```

3. Paste sample device output into the **Target Output** pane and your TextFSM template into the **TextFSM Template** pane.
4. Click **Parse Output** to view parsed rows in the **Parsing Result** pane and the total row count in the status label.

## Tips for effective use

- Keep template expressions as specific as possible to avoid unintended matches.
- Use the selection count indicator to validate your regex groups or highlight sections of output you want to capture.
- If you encounter a syntax error, the parser status will report **TextFSM Syntax Error!**—review your template for missing braces, unescaped characters, or incorrect variable names.

## Project structure

- `textfsm_tester_GUI.py` — Tkinter application providing the parsing interface.
- `README.md` — This guide.

## Contributing

Feel free to open issues or submit pull requests with improvements. When proposing changes, please include a brief description of the feature or fix and how to validate it.
