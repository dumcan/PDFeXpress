import pathlib
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "UiRotatePDF.ui"


class UiRotatePDF(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(UiRotatePDF, self).__init__(master, **kw)
        self.FrameTitle = ttk.Frame(self)
        self.LabelFrameName = ttk.Label(self.FrameTitle)
        self.LabelFrameName.configure(font='{Microsoft YaHei UI} 16 {bold}', text='Rotate PDF')
        self.LabelFrameName.pack(side='left')
        self.FrameTitle.configure(height='200', padding='10', width='200')
        self.FrameTitle.pack(fill='x', side='top')
        self.FramePDFFile = ttk.Labelframe(self)
        self.EntryPDFFile = ttk.Entry(self.FramePDFFile)
        self.pdf_file = tk.StringVar(value='')
        self.EntryPDFFile.configure(state='readonly', textvariable=self.pdf_file)
        self.EntryPDFFile.pack(expand='true', fill='x', padx='4', pady='4', side='left')
        self.ButtonPDFFile = ttk.Button(self.FramePDFFile)
        self.ButtonPDFFile.configure(text='Browser')
        self.ButtonPDFFile.pack(padx='4', pady='4', side='right')
        self.ButtonPDFFile.configure(command=self.get_pdf_file)
        self.FramePDFFile.configure(height='200', text='PDF File', width='200')
        self.FramePDFFile.pack(fill='x', padx='4', pady='4', side='top')
        self.FrameRotatedPDFFile = ttk.Labelframe(self)
        self.EntryRotatedPDFFile = ttk.Entry(self.FrameRotatedPDFFile)
        self.rotated_pdf_file = tk.StringVar(value='')
        self.EntryRotatedPDFFile.configure(state='readonly', textvariable=self.rotated_pdf_file)
        self.EntryRotatedPDFFile.pack(expand='true', fill='x', padx='4', pady='4', side='left')
        self.ButtonRotatedPDFFile = ttk.Button(self.FrameRotatedPDFFile)
        self.ButtonRotatedPDFFile.configure(text='Browser')
        self.ButtonRotatedPDFFile.pack(padx='4', pady='4', side='left')
        self.ButtonRotatedPDFFile.configure(command=self.set_rotated_pdf_file)
        self.FrameRotatedPDFFile.configure(height='200', text='Rotated PDF File', width='200')
        self.FrameRotatedPDFFile.pack(fill='x', padx='4', pady='4', side='top')
        self.FrameOption = ttk.Labelframe(self)
        self.RadiobuttonCW90 = ttk.Radiobutton(self.FrameOption)
        self.rotate_degree = tk.IntVar(value=90)
        self.RadiobuttonCW90.configure(text='CW90°', value='90', variable=self.rotate_degree)
        self.RadiobuttonCW90.pack(padx='4', pady='4', side='left')
        self.Radiobutton180 = ttk.Radiobutton(self.FrameOption)
        self.Radiobutton180.configure(text='180°', value='180', variable=self.rotate_degree)
        self.Radiobutton180.pack(padx='4', pady='4', side='left')
        self.RadiobuttonCCW90 = ttk.Radiobutton(self.FrameOption)
        self.RadiobuttonCCW90.configure(text='CCW90°', value='270', variable=self.rotate_degree)
        self.RadiobuttonCCW90.pack(padx='4', pady='4', side='left')
        self.FrameOption.configure(height='200', text='Option', width='200')
        self.FrameOption.pack(fill='x', padx='4', pady='4', side='top')
        self.FrameProcess = ttk.Labelframe(self)
        self.LabelAppInfo = ttk.Label(self.FrameProcess)
        self.app_info = tk.StringVar(value='')
        self.LabelAppInfo.configure(textvariable=self.app_info)
        self.LabelAppInfo.pack(padx='4', pady='4', side='left')
        self.LabelProcessInfo = ttk.Label(self.FrameProcess)
        self.LabelProcessInfo.pack(expand='true', fill='x', padx='4', pady='4', side='left')
        self.ButtonProcess = ttk.Button(self.FrameProcess)
        self.ButtonProcess.configure(state='disabled', text='Roate')
        self.ButtonProcess.pack(padx='4', pady='4', side='left')
        self.ButtonProcess.configure(command=self.process)
        self.FrameProcess.configure(height='200', text='Rotate PDF', width='200')
        self.FrameProcess.pack(fill='x', padx='4', pady='4', side='top')

    def get_pdf_file(self):
        pass

    def set_rotated_pdf_file(self):
        pass

    def process(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    widget = UiRotatePDF(root)
    widget.pack(expand=True, fill='both')
    root.mainloop()
