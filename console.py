#!/usr/bin/python3
""" Command Interpreter """

from models.base_model import BaseModel
from models import storage
import cmd


class HBNBCommand(cmd.Cmd):
    ''' Entry point of console program and commands center '''

    intro = ''
    prompt = '(hbnb) '

    def do_create(self, arg):
        """ creates new object """

        if self.validate_class(arg):
            base_model = BaseModel()
            base_model.save()
            print(base_model.id)

    def do_show(self, arg):
        """ shows object of given id """

        args = arg.split()
        if self.validate_class(args[0]):
            if not ".".join(args) in storage.all().keys():
                print("Not Found")
            else:
                print(storage.all()[".".join(args)])

    def emptyline(arg):
        """ when no command given """

        pass

    def do_EOF(self, arg):
        '''Quit command to exit the program
        '''

        print("")
        return True

    def do_quit(self, arg):
        '''Quit command to exit the program
        '''

        return True

    def validate_class(self, arg):
        """ validates the given class name """

        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif not arg == str(type(BaseModel()).__name__):
            print("** class doesn't exist **")
            return False
        else:
            return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
