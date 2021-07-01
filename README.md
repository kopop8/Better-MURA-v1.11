# Better-MURA
In this repository new csv files are provided that fixes 500+ mislabeled MURA x-rays for all categories.
The mislabeled x-rays mainly had hardware in them.

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
Download or GIT clone repository.
Put MURA folders in this directory.
python renamer.py

