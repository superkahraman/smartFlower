# <img src="static/assets/images/logo.svg" width="32" height="32" align="left">smartPET back-end

`smartPET` django application will be do all-off server-side things.

## models

- **User** for pet owners information. It has still default fields.
    - username
    - first_name
    - last_name
    - email
- **Pet** for pets info. (Milkie,Dog,Boxer,Brown,22-06-2019,Barren,Pet Owner etc.....)
    - name
    - pettype  `'petType'` (Foreign Key)
    - petbreed `'petBreed'`(Foreign Key)
    - color
    - birthday
    - isbarren
    - owner `'User'`(Foreign Key)
    - updated
    - created
- **petType** (Cat,Dog,Fish,Bird,Snake etc.)
    - name
- **petBreed** (each petBreed should have a petType)
    - name
    - pettype `'petType'` (Foreign Key)
- **petPhoto** (photo urls for pets)
    - url
    - pet `'Pet'` (Foreign Key)


***
Project started at 02/28/2022 16:30 (GMT+3)
##### Mesut Schwarz<br />Coder
