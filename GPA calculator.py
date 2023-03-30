from tkinter import *
import tkinter.messagebox


def gpa_calculator(grades):
    points = 0
    grade_c = {"A+": 4, "A": 4, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67, "C+": 2.33, "C": 2.0, "C-": 1.67,
               "D+": 1.33,
               "D": 1.0, "F": 0}
    if grades:
        for grade in grades:
            if grade not in grade_c:
                return "Invalid"
            points += grade_c[grade]
        gpa = points / len(grades)
        return gpa
    else:
        return None


class App:
    def __init__(self, parent):
        self.parent = parent
        self.frame_1 = Frame(parent)
        self.frame_1.pack()
        self.sub_count = 1
        self.subs = []
        self.grade_labels = []

        Label(self.frame_1, text="Enter Grade :").grid(row=self.sub_count - 1, column=0)
        self.subs.append(Entry(self.frame_1))
        self.subs[self.sub_count - 1].grid(row=self.sub_count - 1, column=1)

        self.btn_1 = Button(parent, text="Add Courses",
                            command=self.add_courses)
        self.btn_1.pack(pady=8)

        self.btn_2 = Button(parent, text="Remove Course", command=self.remove_course)
        self.btn_2.pack(pady=8)

        self.btn_3 = Button(parent, text="Calculate GPA", command=self.calc_cg)
        self.btn_3.pack(pady=8)

    def add_courses(self):
        self.sub_count += 1
        lbl = Label(self.frame_1, text="Enter Grade :")
        lbl.grid(row=self.sub_count - 1, column=0)
        self.grade_labels.append(lbl)

        sub = Entry(self.frame_1)
        sub.grid(row=self.sub_count - 1, column=1)
        self.subs.append(sub)

    def remove_course(self):
        if self.sub_count > 1:
            self.sub_count -= 1
            self.subs[-1].grid_forget()
            self.grade_labels[-1].grid_forget()
            self.subs.pop()
            self.grade_labels.pop()

    def calc_cg(self):
        grades = []
        for sub in self.subs:
            if sub.get() != "":
                grades.append(sub.get())
        tkinter.messagebox.showinfo("Predicted CGPA ", str(gpa_calculator(grades)))


root = Tk()
app = App(root)
root.mainloop()
