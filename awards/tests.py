from django.test import TestCase
from .models import Project

# Create your tests here.

class ProjectTestCase(TestCase):
    
    def setUp(self):
        
        # Set up method
        self.new_project= Project(project_title = 'Awards', project_image ='media/images/default.jpg', project_description = 'Awards Descriptions', country = 'KE')
       

     # Testing  instance
    def test_is_instance(self):
        self.assertTrue(isinstance(self.new_project,Project))

    # Testing  saveinf
    def test_save_method(self):
        self.new_project.save_project()
        all_objects = Project.objects.all()
        self.assertTrue(len(all_objects)>0)

    #  Testing  deleting
    def test_delete_method(self):
        self.new_project.save_project()
        filtered_object = Project.objects.filter(project_title = 'Awards')
        Project.delete_project(filtered_object)
        all_objects = Project.objects.all()
        self.assertTrue(len(all_objects) == 0)