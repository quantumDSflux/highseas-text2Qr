import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import qrcode

def generate_qr():
    # Get the text from the entry field
    qr_data = data_entry.get()
    
    if not qr_data.strip():
        messagebox.showwarning("Input Error", "Please enter some text to encode in the QR code.")
        return

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)

    # Create the QR code image
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image temporarily
    qr_img.save("temp_qr.png")
    display_qr("temp_qr.png")

def display_qr(path):
    # Load and display the QR code image
    qr_image = Image.open(path)
    qr_image.thumbnail((200, 200))
    qr_photo = ImageTk.PhotoImage(qr_image)

    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

def save_qr():
    # Save the generated QR code
    if qr_label.image:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            qr_image = Image.open("temp_qr.png")
            qr_image.save(save_path)
            messagebox.showinfo("QR Code Saved", f"QR code saved as {save_path}")
    else:
        messagebox.showwarning("No QR Code", "Please generate a QR code first.")

# Create main application window
root = tk.Tk()
root.title("Text to QR Code Generator")
root.geometry("400x400")

# Instruction label
instruction_label = tk.Label(root, text="Enter text to encode in QR code:")
instruction_label.pack(pady=10)

# Data entry field
data_entry = tk.Entry(root, width=40)
data_entry.pack(pady=5)

# Generate QR code button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# QR code display area
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# Save QR code button
save_button = tk.Button(root, text="Save QR Code", command=save_qr)
save_button.pack(pady=10)

# Run the main loop
root.mainloop()
