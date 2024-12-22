import qrcode
from tkinter import *
from tkinter import filedialog, messagebox

def shrut():  # Function to generate QR code
    text = shrut1.get()
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter text to generate QR Code.")
        return
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    shrut2(img)

def shrut2(img):  # Function to save the QR code as a PNG
    file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG Files", "*.png")])
    file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                             filetypes=[("jpg Files", "*.jpg")])
    file_path = filedialog.asksaveasfilename(defaultextension=".py",
                                             filetypes=[("Python Files", "*.py")])
    if file_path:
        img.save(file_path)
        messagebox.showinfo("Success", "QR Code saved successfully!")

def shrut3():  # Function to set up the GUI
    global shrut1
    root = Tk()
    root.title("QR Code Generator")
    root.geometry("400x300")
    root.resizable(False, False)

    Label(root, text="Enter Text for QR Code:", font=("Arial", 12)).pack(pady=10)
    shrut1 = Entry(root, width=40, font=("Arial", 12))
    shrut1.pack(pady=5)

    Button(root, text="Generate QR Code", command=shrut, font=("Arial", 12), bg="green", fg="white").pack(pady=10)
    root.mainloop()

if __name__ == "__main__":
    shrut3()
