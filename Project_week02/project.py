import time
class TODO:
    todos = [
        {
            'id' : '',
            'desc' : '',
            'is_completed' : False
        }, {}, {}, {}
    ]
    
    def add_todo(self, desc):
        # 1. Take the desc from the user.
        desc = input('Enter a todo : ')
        if desc == "":
            print("Todo cannot be empty")
            return 
        # We have to create one dictionary in which we will add the todo desc.
        todo = {
            'id' : len(self.todos) + 1,
            'desc' : desc,
            'is_completed': False,
        }
        # We have to append that dictionary inside todos
        self.todos.append(todo)
        print(desc, "Added Successfully")
    
    def remove_todo(self, id):
        for todo in self.todos :
            if todo["id"] == "id":
                self.todos.remove(todo)
                print("Todo Removed")
                return
        print("Not Found")

    
    def display_todos(self):
        if len(self.todos) == 0: 
            print("No Todos available")
            return
        for i in self.todos:
            if i['is_completed']:
                status = "is_completed"
            else:
                status = "Pending"
            print(i["id"],",", i["desc"],"(",status,")")

    
    def update_todo(self, id, new_desc):
        for todo in self.todos:
            if todo["id"] == id:
                todo["desc"] = new_desc
                print("Todo Updated")
                return
        print("Todo Not Found")
    
    def toggle_mark_as_completed(self, id):
        for todo in self.todos:
            if todo["id"] == id:

                if todo["is_completed"]:
                    print("Todo already completed")
                else:
                    todo["is_completed"] = True
                    print("Todo marked as completed")

                return

        print("Todo not found")
    
    def completed_todos(self):
        if len(self.todos) == 0:return
        for i in self.todos:
            if i['is_completed']:
                print(f'--> {i}')
    
    def incompleted_todos(self):
        found = False

        for todo in self.todos:
            if not todo["is_completed"]:
                print(todo["id"], ".", todo["desc"])
                found = True

        if not found:
            print("No pending todos")
    
