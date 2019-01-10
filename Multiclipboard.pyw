# Multiclipboard.pyw Saves and load pieces of texxt to the clipboard
# Usage :   py.exe Multiclipboard.pyw save <keyword> - Saves clipboard to keyword
#           py.exe Multiclipboard.pyw <keyword> - Load keyword to clipboard
#           py.exe Multiclipboard.pyw list - Load all keyword to clipboard
#           py.exe Multiclipboard.pyw del <keyword> - Delete keyword from clipboard
#           py.exe Multiclipboard.pyw del - Delete all keyword from clipboard

import shelve, pyperclip, sys

MulticlipboardShelf = shelve.open('mcb')

# Save clipboard content
if(len(sys.argv)==3 and sys.argv[1].lower()== 'save'):
    MulticlipboardShelf[sys.argv[2]] = pyperclip.paste()

elif(len(sys.argv)==3 and sys.argv[1].lower()== 'del'):
    del MulticlipboardShelf[sys.argv[2]]

elif (len(sys.argv) == 2 and sys.argv[1].lower() == 'list'):
    pyperclip.copy(str(list(MulticlipboardShelf.keys())))
    print(pyperclip.paste())

elif (len(sys.argv) == 2 and sys.argv[1].lower() == 'del'):
    MulticlipboardShelf.clear()
    print("Clipboard Clear")

else:
    pyperclip.copy(MulticlipboardShelf[sys.argv[1]])
    print("Copied "+ MulticlipboardShelf[sys.argv[1]])

MulticlipboardShelf.close()
