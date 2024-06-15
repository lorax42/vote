# vote
**Don't use this for voting! E-voting is not secure!**\
This is just a hobby project.

## Structure
- enter choice
    - tui/gui
    - when selection confirmed, clear screen, to hide previous entry
    - unique person id (hash of name? random string?)

- gets written to a JSON file
    - checksum

- can load file
    - enter file checksum to view results

### Sequenz

1. start program with file containing option names
    1.1. generate JSON template
        1.1.1. generate hash
2. enter UID
    2.1. check for UID in list
        2.1.1. password encrypted
    2.2. put used UID in list 
3. select option
    3.1.
        ```bash
        1. OptionA
        2. OptionB
        3. OptionC
        > 2
        ```
4. confirm option
    4.1.
        ```bash
        You selected OptionB.
        Do you want to continue? (y/n)
        > y
        Vote has been successfully cast.
        ```
5. update JSON, generate new hash
    5.1. options{option{votes=uint}}
6. clear screen, make sound, time out

