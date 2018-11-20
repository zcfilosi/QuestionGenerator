from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.base import EventLoop
from kivy.core.window import Window
import csv
import os


EventLoop.window.clear_color=(.5,.5,.5,1)
 
class StudentListButton(ListItemButton):
    pass
 
 
class StudentDB(BoxLayout):
 
    # Connects the value in the TextInput widget to these
    # fields
    nombre = "./saved_names.txt"
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    students_list = ObjectProperty()
    file_write_list =[]
    
    print("beginning reading file")
    if os.path.exists(nombre):
        read_write = 'r'
        names_file = open(nombre, read_write)
        for f in names_file:
            print("reading saved_names file")
            f = f.rstrip()
            file_write_list.append(f)          
            print("First name appended to list")
            
    else:
        print("creating new saved_names file")
        read_write = 'w'
        names_file = open(nombre, read_write)
        names_file.write("")

    names_file.close()


    def load_previous_data(self, *args):
        for lin in self.file_write_list:
            self.students_list.adapter.data.extend([lin])
        self.students_list._trigger_reset_populate()

 
    def submit_student(self, *args):
        print("Submitting new student")
        # Get the student name from the TextInputs
        first_name_stripped = self.first_name_text_input.text.replace(" ", "")
        last_name_stripped = self.last_name_text_input.text.replace(" ","")
        student_name = first_name_stripped + " " + last_name_stripped
        
        # Add the student to the ListView
        self.students_list.adapter.data.extend([student_name])
        self.file_write_list.append(student_name)
        self.save_listt(self.file_write_list, self.nombre)
        # Reset the ListView
        self.students_list._trigger_reset_populate()
 
    def delete_student(self, *args):
        print("deleting student")
        # If a list item is selected
        if self.students_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.students_list.adapter.selection[0].text
 
            # Remove the matching item
            self.students_list.adapter.data.remove(selection)

            self.file_write_list.remove(selection)
            self.save_listt(self.file_write_list, self.nombre)
            # Reset the ListView
            self.students_list._trigger_reset_populate()
            
    def replace_student(self, *args):
        print("replacing student")
        # If a list item is selected
        if self.students_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.students_list.adapter.selection[0].text
 
            # Remove the matching item
            self.students_list.adapter.data.remove(selection)

 
            # Get the student name from the TextInputs
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
 
            # Add the updated data to the list
            self.students_list.adapter.data.extend([student_name])
            
            for i, x in enumerate(self.file_write_list):
                if x == selection:
                    self.file_write_list[i] = str(student_name)
                    
            self.save_listt(self.file_write_list, self.nombre)
            # Reset the ListView
            self.students_list._trigger_reset_populate()

    def save_listt(self, list_name, nombre):
        print("Saving names list to saved_names file")
        file_w = open(self.nombre, 'w')
        for x in list_name:
            file_w.write(x + '\n')
        file_w.close()
        
            
 
class StudentDBApp(App):

    def build(self):
        Window.clear_color=(0,1,2,1)
        return StudentDB()



 
 
dbApp = StudentDBApp()
 
dbApp.run()




