# Luckyhomenumber
My friend asked me, "Does the home address number matters?", well I don't know
So I googled, and found several websites saying the similar idea.
I created this library to let my friend check if his homeaddress number is good(lucky)

### Installation
`pip install --upgrade luckyhomenumber`

### Usage
```python
from luckyhomenumber import Homenumber
my_homenumber = '1488/186'
hm = Homenumber(my_homenumber)
hm.is_good_address()
```