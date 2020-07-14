#!/bin/bash
name=$1;
echo -n "
    def get${name^}(self):
        return self.__$name

    def set${name^}(self, $name):
        self.__$name = $name"