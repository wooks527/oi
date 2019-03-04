PostgreSQL
===========

==========
Commands
==========

**Copy table contents to a csv file**

::

    copy (select * from table) to '/home/hwkim/data/data.csv' csv header