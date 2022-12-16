============
SQL Alchemy
============

Important points to note
=========================

- **session.add**: Registers transaction operations, but **doesn't yet communicated them to the database**. We can see the added/updated details using **session.new** or **session.dirty**.
- **session.flush**: 
    - Communicates a series of operations to the database. Database maintains them as **pending operations in a transaction**. The changes can no longer visible in **session.new** or in **session.dirty**. You can' see them in DB as well as they are not yet committed! You can see the DB process using `SELECT * FROM information_schema.PROCESSLIST`. However, you will not get any info from the process list.
    - flush occurs before any individual query is issued as well as within the commit() call before the transaction is committed.

- **session.commit**: 
    - will commit all pending transactions.
    - session.flush() will be called implicitly.
    - Releases all Transaction and Connection resources, and goes back to the “begin” state,
    - **COMMIT WILL NOT TERMINATE A SESSION. IT JUST COMMITS THE CURRENT TRANSACTION**. You can still issue additional queries after you commit. A transaction will be started automatically if you do. 
- **session.query()** will perform an **implicit flush** of the session to ensure it is getting the most up-to-date information.
- **session.expunge()**: will remove entry from session.new/session.dirty/session.deleted so the changes will not be flushed.
- **session.new**: A set that contain the newly added instances which are **not yet flushed**.
- **session.dirty**: A set that contain the **updates** added to existing instances which are **not yet flushed**.
- **session.deleted**: A set that contain the deleted instances which are **not yet flushed**.


Session States
---------------

- "BEGIN STATE": Initially session is in begin state. No communication with DB.
- "TRANSACTIONAL STATE": session.query()/flush()/execute()/.. will change the state to transactional state. Commit/Rollback will make the session return back to BEGIN state.

commit() vs flush()
--------------------

Flush() will communicate a series of operations to the db and db maintains then as pending for transactions.

Commit() will first do a flush() and then commit all pending transactions so that they become persistent in the DB. Releases all Transaction and Connection resources.

flush() vs query()
-------------------

A flush() occurs before all individual queries.



Tips
=====

To get all primary keys
------------------------

::

    [key.name for key in inspect(model).primary_key]