import pathlib
import tkinter as tk
import tkinter.ttk as ttk

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "UiImages2PDF.ui"


class UiImages2PDF(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(UiImages2PDF, self).__init__(master, **kw)
        self.FrameTitle = ttk.Frame(self)
        self.LabelFrameName = ttk.Label(self.FrameTitle)
        self.LabelFrameName.configure(font='{Microsoft YaHei UI} 16 {bold}', text='Images to PDF')
        self.LabelFrameName.pack(side='left')
        self.FrameTitle.configure(height='200', padding='10', width='200')
        self.FrameTitle.pack(fill='x', side='top')
        self.FrameImageList = ttk.Labelframe(self)
        self.TreeViewImageList = ttk.Treeview(self.FrameImageList)
        self.TreeViewImageList_cols = ['ColumnDirName', 'ColumnFileName']
        self.TreeViewImageList_dcols = ['ColumnDirName', 'ColumnFileName']
        self.TreeViewImageList.configure(
            columns=self.TreeViewImageList_cols, displaycolumns=self.TreeViewImageList_dcols
            )
        self.TreeViewImageList.column('ColumnDirName', anchor='w', stretch='true', width='150', minwidth='20')
        self.TreeViewImageList.column('ColumnFileName', anchor='w', stretch='true', width='300', minwidth='20')
        self.TreeViewImageList.heading('ColumnDirName', anchor='w', text='Folder')
        self.TreeViewImageList.heading('ColumnFileName', anchor='w', text='File Name')
        self.TreeViewImageList.pack(expand='true', fill='both', padx='4', pady='4', side='left')
        self.ScrollbarImagesList = ttk.Scrollbar(self.FrameImageList)
        self.ScrollbarImagesList.configure(orient='vertical')
        self.ScrollbarImagesList.pack(fill='y', side='left')
        self.ButtonAddImages = ttk.Button(self.FrameImageList)
        self.ButtonAddImages.configure(text='Add Images')
        self.ButtonAddImages.pack(fill='x', padx='4', pady='4', side='top')
        self.ButtonAddImages.configure(command=self.add_images)
        self.ButtonRemoveImage = ttk.Button(self.FrameImageList)
        self.ButtonRemoveImage.configure(text='Remove Image')
        self.ButtonRemoveImage.pack(fill='x', padx='4', pady='4', side='top')
        self.ButtonRemoveImage.configure(command=self.remove_images)
        self.ButtonRemoveAll = ttk.Button(self.FrameImageList)
        self.ButtonRemoveAll.configure(text='Remove All')
        self.ButtonRemoveAll.pack(fill='x', padx='4', pady='4', side='top')
        self.ButtonRemoveAll.configure(command=self.remove_all)
        self.ButtonMoveTop = ttk.Button(self.FrameImageList)
        self.ButtonMoveTop.configure(text='Move to First')
        self.ButtonMoveTop.pack(fill='x', padx='4', pady='4', side='top')
        self.ButtonMoveTop.configure(command=self.move_top)
        self.ButtonMoveUp = ttk.Button(self.FrameImageList)
        self.ButtonMoveUp.configure(text='Move Up')
        self.ButtonMoveUp.pack(fill='x', padx='4', pady='4', side='top')
        self.ButtonMoveUp.configure(command=self.move_up)
        self.ButtonMoveDown = ttk.Button(self.FrameImageList)
        self.ButtonMoveDown.configure(text='Move Down')
        self.ButtonMoveDown.pack(fill='x', padx='4', pady='4', side='top')
        self.ButtonMoveDown.configure(command=self.move_down)
        self.ButtonMoveBottom = ttk.Button(self.FrameImageList)
        self.ButtonMoveBottom.configure(text='Move to Last')
        self.ButtonMoveBottom.pack(fill='x', padx='4', pady='4', side='top')
        self.ButtonMoveBottom.configure(command=self.move_bottom)
        self.FrameImageList.configure(height='200', text='Image List', width='200')
        self.FrameImageList.pack(expand='true', fill='both', padx='4', pady='4', side='top')
        self.FramePDFFile = ttk.Labelframe(self)
        self.EntryPDFFile = ttk.Entry(self.FramePDFFile)
        self.pdf_file = tk.StringVar(value='')
        self.EntryPDFFile.configure(state='readonly', textvariable=self.pdf_file)
        self.EntryPDFFile.pack(expand='true', fill='x', padx='4', pady='4', side='left')
        self.ButtonPDFFile = ttk.Button(self.FramePDFFile)
        self.ButtonPDFFile.configure(text='Browser')
        self.ButtonPDFFile.pack(padx='4', pady='4', side='left')
        self.ButtonPDFFile.configure(command=self.set_pdf_file)
        self.FramePDFFile.configure(height='200', text='PDF File', width='200')
        self.FramePDFFile.pack(fill='x', padx='4', pady='4', side='top')
        self.FrameProcess = ttk.Labelframe(self)
        self.LabelAppInfo = ttk.Label(self.FrameProcess)
        self.app_info = tk.StringVar(value='')
        self.LabelAppInfo.configure(textvariable=self.app_info)
        self.LabelAppInfo.pack(padx='4', pady='4', side='left')
        self.LabelProcessInfo = ttk.Label(self.FrameProcess)
        self.process_info = tk.StringVar(value='')
        self.LabelProcessInfo.configure(textvariable=self.process_info)
        self.LabelProcessInfo.pack(expand='true', fill='x', padx='4', pady='4', side='left')
        self.ButtonProcess = ttk.Button(self.FrameProcess)
        self.ButtonProcess.configure(state='disabled', text='Convert')
        self.ButtonProcess.pack(padx='4', pady='4', side='left')
        self.ButtonProcess.configure(command=self.process)
        self.FrameProcess.configure(height='200', text='Images to PDF', width='200')
        self.FrameProcess.pack(fill='x', padx='4', pady='4', side='top')

    def add_images(self):
        pass

    def remove_images(self):
        pass

    def remove_all(self):
        pass

    def move_top(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_bottom(self):
        pass

    def set_pdf_file(self):
        pass

    def process(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    widget = UiImages2PDF(root)
    widget.pack(expand=True, fill='both')
    root.mainloop()
