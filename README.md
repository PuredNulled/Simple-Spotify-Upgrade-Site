# Simple-Spotify-Upgrade-Site
Shitty (ATM Being worked on to be way better) API for spotify upgrade services.

Thanks to @xannyyyy for the Original Key System. https://github.com/xannyyyy/Hwid-Auth-Verify 
How this works:
You insert spotify invite links and the country into a db. You can also make keys.
You send a request to the API with your key and the CN. If the key is valid, it'll return the invite link, cn, address and the ID from the DB.
If the key is valid it will delete from the DB and the invite so it can't be reused.

This is beta and pretty shit with bugs but ya being worked on

add this to db and config in main.py
``
CREATE TABLE `links` (
  `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `link` varchar(255) NOT NULL,
  `cn` varchar(255) NOT NULL,
  `address` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `key` ( `key` varchar(255) NOT NULL ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
``
Whats being added:
- Instead of links, you will be able to enter accounts and it will auto check them.
- Wayyy better key system as it is shitty atm
- Hella fixed bugs 

DONATE BTC:  1GB4rLLG71eWqAXe6Dj1ZSpZdFwnFcg6VT
