#test_to_do_list.py
#Jacen Piatt

import unittest
from to_do_list import ToDoManager

class TestToDoManager(unittest.TestCase):
    
    #start new instance of todo list
    def setUp(self):
        self.todo_manager = ToDoManager()
        
    def test_add_task(self):
        #test that tasks can be added to list
        self.todo_manager.add_task("Buy food")
        self.assertEqual(len(self.todo_manager.tasks), 1)
        self.assertEqual(self.todo_manager.tasks[0]['task'], "Buy food")
        self.assertFalse(self.todo_manager.tasks[0]["completed"])
        
    def test_remove_task(self):
        #test that tasks can be removed from list
        self.todo_manager.add_task("Buy food")
        self.todo_manager.remove_task(0)
        self.assertEqual(len(self.todo_manager.tasks), 0)
        
    def test_mark_task_as_completed(self):
        #test that a task can be marked as completed
        self.todo_manager.add_task("Buy food")
        self.todo_manager.mark_task_as_completed(0)
        self.assertTrue(self.todo_manager.tasks[0]["completed"])
        
    def test_save_and_load_tasks(self):
        self.todo_manager.add_task("Buy food")
        self.todo_manager.add_task("Clean room")
        self.todo_manager.mark_task_as_completed(0)
        self.todo_manager.save_tasks("test_tasks.txt")

        new_manager = ToDoManager()
        new_manager.load_tasks("test_tasks.txt")
        self.assertEqual(len(new_manager.tasks), 2)
        self.assertTrue(new_manager.tasks[0]["completed"])
        self.assertFalse(new_manager.tasks[1]["completed"])
        
if __name__ == '__main__':
    unittest.main()
    
        