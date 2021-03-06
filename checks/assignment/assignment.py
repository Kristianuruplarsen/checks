
"""
Generic assignment class which can be invoked with any number of questions.
"""
import nbformat as nbf
import os 
import re 
from requests import get, post

from .questionChecker import QuestionChecker
from .resultMessager import ResultMessenger

# Inheritance is purely for code segmentation for now (rework?)
class Assignment(QuestionChecker):
    """
    Generic assignment

    Parameters
    ----------
    *questions: Question
        A sequence of questions (from the questionLibrary) ordered by their 
        intended appearance in the final exercise set. 
    """

    def __init__(self, *questions, 
                        leadmd = None, 
                        leadcode = None
                ):

        self.leadmd = leadmd 
        self.leadcode = leadcode

        if self.leadmd is not None:
            self.leadmd = self._clean_string(leadmd)
            
        if self.leadcode is not None:
            self.leadcode = self._clean_string(leadcode)

        self.questions = {i + 1: q for i,q in enumerate(questions)}
        self.correctly_ans = {k: None for k in self.questions.keys()}          

        # For server com
        self.online = False
        self.conn = None
        self.user = None
        self.ip = None

    def make_notebook(self, filename):
        """
        Build the exercise notebook.
        """
        nb = nbf.v4.new_notebook()

        # add lead code and markdown if they exist
        if self.leadmd is not None:
            nb['cells'] += [nbf.v4.new_markdown_cell(self.leadmd)]
        if self.leadcode is not None:
            nb['cells'] += [nbf.v4.new_code_cell(self.leadcode)]

        # add questions
        for num, question in self.questions.items():
            md = self._clean_string(self._make_markdown(num, question))

            nb['cells'] += [nbf.v4.new_markdown_cell(md), 
                            nbf.v4.new_code_cell(f"# [Answer to problem {num} here]")]

        print(f'Building notebook in {os.getcwd()}')
        nbf.write(nb, f'{filename}.ipynb')


    def _make_markdown(self, num, question):
        qtext = question().markdown
        s = f'# Problem {num} \n' + qtext
        
        return s


    def _clean_string(self, s):
        """ Remove whitespace in all string lines in a multiline string.
        """
        lines = s.split('\n')
        lines = [l.strip() for l in lines]
        return '\n'.join(lines).strip()


    def setup(self, user, ip):
        self.conn = ResultMessenger(user, ip)
        self.online = True

        # self.user = user
        # self.ip = ip

        # Print which problems have already been answered and submitted
        progress = self.conn.get_full_status()
        correct = ', '.join([k for k,v in progress.items() if v])

        print(f"Set up checker for student {user}")
        if len(correct)>1:
            print(f"You have correctly answered: {correct}")

        return self



    # def depr_setup(self, user, ip):
    #     """ Set up an assignment session to work with the server.

    #     Parameters
    #     ----------
    #     user: str
    #         A student id, it is hard coded to comply 
    #         with the UCPH id format AAADDD.
    #     ip: str
    #         The ip of the Pi, including port.
    #     """
        
    #     self._check_id_with_re(user)

    #     progress = self._student_in_database(user, ip)
    #     self.correctly_ans =  {int(k): bool(v) for k,v in dict(progress).items()}  # Overwrite status if connected to the ip.

    #     correct = ', '.join([k for k,v in progress.items() if v])

    #     self.online = True
    #     self.user = user
    #     self.ip = ip

    #     print(f"Set up checker for student {user}")
    #     if len(correct)>1:
    #         print(f"You have correctly answered: {correct}")

    #     return self


    # def depr_check_id_with_re(self, ident):
    #     if not re.match(r'[A-Za-z]{3}\d{3}', ident):
    #         raise ValueError(f'User ID {ident} is invalid. KU ident must be 3 letters and 3 digits.')


    # def depr_student_in_database(self, ident, ip):
    #     student_exists = get(f"http://{ip}/student/{ident}")

    #     if not student_exists.ok:
    #         raise ValueError(f"Student ID {ident} not in ip database.")
    #     return student_exists.json()        

