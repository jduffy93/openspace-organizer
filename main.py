from src.openspace import OpenSpace
import pandas as pd

filepath = 'colleagues.xlsx'

if __name__ == "__main__":

    df = pd.read_excel(filepath)
    names = df['Names'].tolist()

    openspace = OpenSpace(6)
    openspace.organize(names)
    openspace.display()
    openspace.store()  # Can change the default output file with filename='test_output.txt'

