# Better-MURA
In this repository new csv files are provided that fixes 500+ mislabeled MURA x-rays for all categories.
The mislabeled x-rays mainly had hardware in them. This project only fixes the false negatives.

| Category  | Total negative x-rays test  | Wrongly classified  | Total negative x-rays valid  | Wrongly classified  |
|---|---|---|---|---|
| Elbow | 2925  | 65  | 235  | 4  |
| Finger  | 3138  | 31 | 214  | 7  |
| Forearm  | 1164  | 43  | 150  | 4  |
| Hand  | 4059  | 15  | 271  | 3  |
| Humerus  | 673  | 28  | 148  | 15  |
| Shoulder  | 4211  | 241  | 285  | 12  |
| Wrist  | 4072  | 73  | 364  | 8  |
| Total  | 20242  | 496  | 1667  | 53  |

Code is provided to fix the directory names with the new labels.
## Usage
1. Download or GIT clone repository.
2. Put MURA folders in this directory.
3. python renamer.py
4. When programm finishes the directorie are now named according to the new csv files


## Contribution
Help with this project will be greatly appreciated! If you see a false positive or false negative that isn't already in changed_studies.txt, it would be appreciated if you made a pull request fixing them. 
Right now this project focusses only on false negatives, so if someone who is qualified and is willing to help fix the false positives, you can send me a message.
Together we can make MURA better :)

