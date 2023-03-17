#!/usr/bin/env python

from user import User
import ipdb

import random

class Teacher(User):

    knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
        "AAAAAAAAAAAAAAAAAAAAAA",
        "AAAAAHHHHHHHH!!!!!!!!!"
    ]    

    def teach(self):

        ran_idx = random.randint(0, (len(self.knowledge) - 1))
        pass

        return self.knowledge[ran_idx]