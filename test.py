from luckyhomenumber import Homenumber

# normal case
hm = Homenumber('1488/186')
hm.is_good_address()
# bad case
hm = Homenumber('/')
hm.is_good_address()
