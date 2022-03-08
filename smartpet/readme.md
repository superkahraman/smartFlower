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

```python
from django.db import migrations, models
from django.contrib.auth.models import User
```

```
TODO :

* Pet'in petType'ı petBreed'ten çek. Bir Pet için petBreed belirtilmemiş/bilinmiyor ise. her petType için default gelecek "Unknown" ya da "Empty" bir petBreed tanımla.

* User modeli kesinlikle yeniden yap. Mevcut User model'in özellikle username ve email fieldları çok sorunlu.
Konuyla ilgili bilgi için aşağıdaki linkleri kullan.

https://simpleisbetterthancomplex.com/article/2021/07/08/what-you-should-know-about-the-django-user-model.html
https://stackoverflow.com/questions/48030567/how-to-customize-username-validation
https://www.codingforentrepreneurs.com/blog/how-to-create-a-custom-django-user-model/
https://www.youtube.com/watch?v=HshbjK1vDtY&t=2s

```
***
Project started at 02/28/2022 16:30 (GMT+3)
##### Mesut Schwarz<br />Coder
