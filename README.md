# make-gui.py - Makefile Execution GUI

This script provides a simple graphical user interface (GUI) for executing `make` commands with optional arguments. It allows users to select a Makefile, specify additional arguments, and view the output in a scrollable text area.

## Features

* **Makefile Selection:** A file dialog allows users to easily select the Makefile to be executed.
* **Argument Input:** An entry field for specifying additional arguments to the `make` command.
* **Output Display:** A scrollable text area displays the standard output and standard error from the `make` command.
* **Error Handling:** Catches and displays any errors that occur during the `make` execution.
* **Icon Support:** Displays a custom icon for the application window.

## Prerequisites

* Python 3
* `tkinter` library (usually included with Python)
* `make` command-line tool (must be installed and available in the system's PATH)
* An optional icon file located at `./make-gui.png`. If the icon file is missing, the script will still function correctly without displaying a custom icon.

## Usage

1.  **Save the script:** Save the code as `make-gui.py`.
2.  **Make it executable:** If necessary, make the script executable by running `chmod +x make-gui.py` in your terminal.
3.  **Run the script:** Execute the script from your terminal using `python3 make-gui.py` or `./make-gui.py` (if you made it executable).
4.  **Select Makefile:** Click the "Select Makefile" button and choose the Makefile you want to execute.
5.  **Enter arguments (optional):** Enter any additional arguments you want to pass to the `make` command in the "Additional arguments" field. Separate multiple arguments with spaces.
6.  **Run Make:** Click the "Make!" button to execute the `make` command.
7.  **View output:** The output of the `make` command will be displayed in the scrollable text area.

## Script Details

### Dependencies

* `tkinter`: Used for creating the GUI.
* `subprocess`: Used for executing the `make` command.
* `os`: Used to get the directory of the selected Makefile.

### Functions

* `select_makefile()`:
    * Opens a file dialog to allow the user to select a Makefile.
    * Updates the `makefile_path` `StringVar` with the selected file path.
* `run_make_with_args()`:
    * Retrieves the additional arguments from the `extra_args_entry` `Entry` widget.
    * Clears the `output_text` `ScrolledText` widget.
    * Constructs the `make` command with the specified arguments.
    * Executes the `make` command using `subprocess.run()`, capturing the standard output and standard error.
    * Inserts the output into the `output_text` widget.
    * Handles any exceptions that occur during the `make` execution and displays an error message.

### GUI Elements

* `root`: The main application window.
* `frame`: A frame to contain the "Select Makefile" button and the selected Makefile path label.
* `makefile_path`: A `StringVar` to store the selected Makefile path.
* "Select Makefile" button: Triggers the `select_makefile()` function.
* `extra_args_entry`: An `Entry` widget for entering additional arguments.
* "Make!" button: Triggers the `run_make_with_args()` function.
* `output_text`: A `ScrolledText` widget to display the output of the `make` command.
* Icon: The icon is loaded from `/usr/local/share/icons/make-gui.png`. If this file is not found, no icon will be shown.

### Example

1.  Select the Makefile located at `/home/user/myproject/Makefile`.
2.  Enter `clean all` in the "Additional arguments" field.
3.  Click the "Make!" button.

The script will execute `make clean all` in the `/home/user/myproject/` directory and display the output in the text area.

## Icon Installation (Optional)

1.  Create or obtain an icon file named `make-gui.png`.
2.  Place the icon file in the same directory as `make-gui.py`.

## Notes

* The script assumes that the `make` command is available in the system's PATH.
* The script does not provide any advanced features, such as target selection or progress indicators. It aims to provide a basic GUI for running `make` commands.
* The script handles basic exceptions, but more robust error handling can be implemented if needed.
