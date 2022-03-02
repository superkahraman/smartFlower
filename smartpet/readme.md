# :sunflower: smartPET back-end

`smartPET` django application will be do all-off server-side things.

## models
:alien: = Foreign Key
- **User** for pet owners information. It has still default fields.
    - username
    - first_name
    - last_name
    - email
- **Pet** for pets info. (Milkie,Dog,Boxer,Brown,22-06-2019,Barren,Pet Owner etc.....)
    - name
    - pettype  `'petType'` :alien:
    - petbreed `'petBreed'` :alien:
    - color
    - birthday
    - isbarren
    - owner `'User'` :alien:
    - updated
    - created
- **petType** (Cat,Dog,Fish,Bird,Snake etc.)
    - name
- **petBreed** (each petBreed should have a petType)
    - name
    - pettype `'petType'` :alien:
- **petPhoto** (photo urls for pets)
    - url
    - pet `'Pet'` :alien:


***
Project started at 02/28/2022 16:30 (GMT+3)
##### Mesut Schwarz<br />Coder
