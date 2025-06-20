# Learning Python 🐍

## 📅 Day 1: Basics

### 🗃️ Variables
- **Types:** `string`, `integer`, `float`, `boolean`

### 🖊️ Multiple Assignments
- Assign multiple variables at once.

### 🔤 String Methods
- `len()`, `find()`, `replace()`, `capitalize()`, `upper()`, `lower()`, `isdigit()`, `isalpha()`, `count()`

### 🔄 Type Casting
- `type(variable)`

### ⌨️ User Input
- `input("...")`

### ➕ Math Functions
- `round()`, `math.ceil()`, `math.floor()`, `abs()`, `math.sqrt()`, `max()`, `min()`

### ✂️ String Slicing
- Two methods:
  - **Indexing operator**
  - **Slice**

### ⚖️ If Statements
- For decision making.

---

## 📅 Day 2: Loops & Logic

### 🔁 Loops
- Repeat a block of code:
  - `for` loop
  - `while` loop

### ⚙️ Logical Operators
- For condition checking:
  - `and`, `or`, `not`

---

## 📅 Day 3: Conditions & Collections

### 🗂️ Conditional Expression
- Syntax: `X if condition else Y`

### ✏️ Format Specifier
- To format a line.

### 📦 Collections
- `list`, `set`, `tuple`

### 🛒 Project: Shopping Cart Program

---

## 📅 Day 4: 2D Collections & Dictionaries

### 🗺️ 2D Collections
- In form of a two-dimensional grid.
- The collection can be a `list`, `set`, `tuple`, or mix.

### ❓ Project: Quiz Game

### 📖 Dictionary
- Stores `key:value` pairs.
- Common methods:
  - `get()`, `update()`, `pop()`, `popitem()`, `keys()`, `values()`, `items()`

---

## 📅 Day 5: Fun with Randomness

### 🍴 Project: Concession Program
- Shows menu of a restaurant.

### 🎲 Random Number Generator
- Importing `random` module.
  - `random.randint()`
  - `random.choice()`
  - `random.random()`
  - `random.shuffle()`

### 🎯 Project: Number Guessing Game

### 🎲 Project: Dice Roller Game
- Learned about **ASCII arts**.

---

## 📅 Day 6: Functions & Arguments

### 🧩 Functions
- Block of reusable code.

### ⚙️ Default Arguments
- Default value should be assigned **from right to left**.

### 🗝️ Keyword Arguments
- Position of the argument does not matter

### 👓 Arbitary Arguments
- *args = allows you to pass multiple non-key arguments (stores in tuple)
- **kwargs = allows you to pass multiple keyword-arguments (stores in dictionary)

---

## Day 7

### 🔁 Iterables
- An object/collection that can return its elements one at a time allowing it to be iterable over in a loop

### 🛒 Membership Operators
-  Used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dict)

### 🗜️ List Comprehension
- A concise way to create lists in Python compact and easier to read than traditional loops
- Syntax: [expression for value in iterable if condition]

### 🤲 Match Case Statement
- An alternative to using many 'elif' statements

### 🎒 Module in Python
-  A file containing code you want to include in your program use 'import' to include a module(built-in or your own)

### 👀 Variable Scope Resolution
- Scope where a variable is visible and accessible
- Priority: (LEGB) Local > Enclosed > Global > Built-in

### 🔗 if __name__ == '__main__':
- The if __name__ == '__main__': block ensures main() only runs if you run this file directly.
- It allows the file to be used both as a script and as an importable module without accidentally running code when imported.

---

## Day 8

### 💳 Banking Program
- A program showcasing basic features available while banking. You can login, create account, check balance, deposit and withdraw.
- A simple guideline is provide so users can navigate with ease.
- You can have multiple users.
- The data is temporary stored using dictionary. Username acts like foreign key(for authentication and balance).

---

## Day 9

### 🚃 Basic OOP
- Class: Collection of object
- Object: Entity having attribute and methods

### 👨‍🏫 Class Variable
- Class variable is shared among all objects(instances of a class)

---

## Day 10

### 👪 Inheritance
- Allows a class to inherit attributes and methods from another class
- Helps with code reusability and extensibility

### Multiple and Multilevel Inheritance 
- Multiple: A class can inherit from more than one parent class
- Multilevel: A class inherits form a parent which inherits from another parent

### super()
- It is function used in a child class to call methods from a parent class (super class).
- It allows you to extend the functionality of the inherited methods.

---

## Day 11
Started learning tkinter for a project.

### Tk Basics
- How to open a window?
- Set a title, dimension and background of window.

### Tk Labels
- Label is a widget that can holds text and/or an image within a window.
- Different properties of label was explored.

### Tk Buttons
- Button is a widget that does something when clicked.
- Different properties of button was explored.

### Tk Entry Widget
- Entry widget is a textbox that accepts a sigle line of user input.
- How to manipulate user input was learned.
- Basic properties were explored.

---

## Day 12

### Checkbutton (Checkbox)
- Used for multiple selection options.
- Example: Enable/disable multiple features.

### Radiobutton (Radio)
- Used for single selection from a group.
- Example: Select gender or mode.

### Scale
- Lets user select a value from a range.
- Example: Volume or brightness control.

### Listbox
- Displays a list of selectable items.
- Supports single or multiple selection.

### Messagebox
- Shows pop-up dialogs like:
  - `showinfo()`
  - `showwarning()`
  - `showerror()`

### Colorchooser
- Opens a color selection dialog.
- Returns RGB and HEX values.

### Textarea (`Text` widget)
- Multi-line text field.
- Used for notes, code, or longer input.

### Menubar
- Adds a dropdown menu to your app.
- Common menus: File, Edit, Help.

## File Dialogs
- Open File
  - Use `filedialog.askopenfilename()` to open and read files.

- Save File
  - Use `filedialog.asksaveasfilename()` to write and save files.

## Frames
- Logical containers for grouping widgets.
- Helps structure layout better.




✨ **Keep learning!** ✨
