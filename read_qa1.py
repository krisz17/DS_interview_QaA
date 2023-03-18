
# https://pynative.com/python-find-position-of-regex-match-using-span-start-end/

"""
Plik zawiera kod do zaciągnięcia Q&A ze strony 
https://www.gangboard.com/blog/machine-learning-interview-questions-and-answers
Z której niestety nie można dokonywać WebScrapingu, copy-paste ale bezczelne przeniesienie kodu zadziałało :)

mój regex na pytanie, uznam, że dopełnienie od znaku koniec+ 1 do start-1 to będzie odpowiedź, jedynie wykasuje 
Q\d+.+\?

"""

import os 
import re
import pandas as pd

path_files = "E:\page_ds\DS_interview_QaA\materialy"

plik_path = os.path.join(path_files, "Qa1.txt")


with open(plik_path, mode="r") as f:
    lines = f.read()

count = 0

for match in re.finditer(r'Q\d+.+\?', lines):
    count += 1
    print("match", count, match.group(), "start index", match.start(), "End index", match.end())