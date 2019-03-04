PowerShell
==========

**Head and Tail**

::

    gc log.txt -head 10
    gc log.txt -tail 10


**The number of lines**

::

    Get-Content .\BindingDB_ChEMBL.tsv | Measure-Object -Line


