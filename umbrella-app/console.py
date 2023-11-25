import cmd
import json
from models.basemodel import Base

class UmbrellaCommand(cmd.Cmd):
    """ Console definiton for Umbrella"""
    prompt = '$umbrella >> '
    def do_quit(self, arg):
        """ Type 'quit' to exit the command line """
        return True
    
    def do_EOF(self, arg):
        """ Type 'EOF' to exit the command line """
        return True
    
    def emptyline(self):
        """ Where no input, do nothing """
        pass

    def do_create(self, arg):
        """Type 'create {classname}' to create a new instance of the BaseModel"""
        if not arg:
            print("** class name missing **")
        if arg:
            try:
                # Split user input to get the class name
                class_name = arg.split()[0]

                # Dynamically import the class from basemodel module
                class_module = __import__('models.basemodel', fromlist=[class_name])
                my_class = getattr(class_module, class_name)

                instance = my_class()
                print(instance.id)
            except ImportError:
                print(f'** class {class_name} doesn\'t exist **')
            except AttributeError:
                print(f'** class {class_name} doesn\'t exist **')

    def do_show(self, arg):
        """ Type 'show {class name} {id} to print the string representation of an instance"""
        args = arg.split()

        if not args:
            print('** class name missing **')

        class_name = args[0]

        try:
            class_module = __import__('umbrella_app.models.basemodel', fromlist=[class_name])
            my_class = getattr(class_module, class_name)

            if len(args) < 2:
                print('** instance id missing **')
                return
            
            instance_id = args[1]
            # Load instances from the JSON file
            with open("storage.json", "r") as file:
                obj_dict = json.load(file)

            # Find the instance based on the id
            instance = obj_dict.get(instance_id)

            if instance:
                # Use the __str__ method to get the string representation of the instance
                print(instance.__str__())
            else:
                print('** no instance found **')

        except ImportError:
            print(f'** class {class_name} doesn\'t exist **')
        except AttributeError:
            print(f'** class {class_name} doesn\'t exist **')

        except:
            pass


if __name__ == "__main__":
    UmbrellaCommand().cmdloop()