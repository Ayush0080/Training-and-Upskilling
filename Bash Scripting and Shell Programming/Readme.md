### shell-scripting

- The first line of a shell script typically starts with a shebang, followed by the path to an interpreter that will be used to execute the  commands in the script.

 ##### Variable Usage
 - use variable value using `${VARIABLE_NAME}`
 - Assign command output to a variable `VARIABLE_NAME=$(command)

    ```bash
    #!/bin/bash
    HOST_NAME=$(hostname) 
    echo "This script is running on ${HOST_NAME}."
    ```  
     ![alt text](image.png)


 ##### File Test Operators in Bash

| Operator | Description | Example | Result |
|-----------|--------------|----------|---------|
| `-e` | **Exists:** True if the file or directory exists. | `[ -e my_file.txt ]` | True if `my_file.txt` exists. |
| `-f` | **Regular File:** True if the path exists and is a regular file (not a directory or special file). | `[ -f config.ini ]` | True if `config.ini` is a file. |
| `-d` | **Directory:** True if the path exists and is a directory. | `[ -d /home/user/data ]` | True if `/home/user/data` is a folder. |
| `-r` | **Readable:** True if the file exists and the user running the script has read permission. | `[ -r important.log ]` | True if the user can read `important.log`. |
| `-w` | **Writable:** True if the file exists and the user has write permission. | `[ -w script.sh ]` | True if the user can modify `script.sh`. |
| `-x` | **Executable:** True if the file exists and the user has execute permission. | `[ -x install.sh ]` | True if the user can run `install.sh`. |
| `-s` | **Not Empty:** True if the file exists and its size is greater than zero. | `[ -s output.txt ]` | True if `output.txt` contains data. |


##### Arithmetic Test Operators in Bash

| Operator | Description | Example | Result |
|-----------|--------------|----------|---------|
| `-eq` | **Equal to:** True if two numbers are equal. | `[ 5 -eq 5 ]` | True |
| `-ne` | **Not equal to:** True if two numbers are not equal. | `[ 5 -ne 10 ]` | True |
| `-gt` | **Greater than:** True if the first number is greater than the second. | `[ 8 -gt 3 ]` | True |
| `-lt` | **Less than:** True if the first number is less than the second. | `[ 2 -lt 7 ]` | True |
| `-ge` | **Greater than or equal to:** True if the first number is greater than or equal to the second. | `[ 6 -ge 6 ]` | True |
| `-le` | **Less than or equal to:** True if the first number is less than or equal to the second. | `[ 4 -le 9 ]` | True |

```bash
    Write a shell script to check to see if the file "/etc/shadow" exists. If it does exist, display "Shadow passwords are enabled." Next, check to see if you can write to the file. If you can, display "You have permissions to edit /etc/shadow." If you cannot, display "You do NOT have permissions to edit /etc/shadow."
    
    #!/bin/bash

    FILE="/etc/shadow"

    if [ -e "$FILE" ]
    then
    echo "Shadow passwords are enabled."
    fi
   
    if [ -w "$FILE" ]
    then
    echo "You have permissions to edit ${FILE}."  
    else
    echo "You do NOT have permissions to edit ${FILE}."
    fi
 ```
 ![alt text](image-1.png)
 ![alt text](image-2.png)



```bash
  - Write a shell script that displays "man", "bear", "pig", "dog", "cat", and "sheep" to the screen with each appearing on a separate line. Try to do this in as few lines as possible.

    #!/bin/bash
    for ANIMAL in man bear pig dog cat sheep
    do
    echo "$ANIMAL"
    done 
```

  ![alt text](image-3.png)



```bash
- Write a shell script that prompts the user for a name of a file or directory and reports if it is a regular file, a directory, or other type of file. Also perform an ls command against the file or directory with the long listing option.
    #!/bin/bash

    read -p "Enter the path to a file or a directory: " FILE

    if [ -f "$FILE" ]
    then
    echo "$FILE is a regular file."
    elif [ -d "$FILE" ]
    then
    echo "$FILE is a directory."
    else
    echo "$FILE is something other than a regular file or directory."
    fi

    ls -l $FILE
```

![alt text](image-4.png)

```bash
- Modify the previous script so that it accepts the file or directory name as an argument instead of prompting the user to enter it.

    #!/bin/bash

    FILE=$1

    if [ -f "$FILE" ]
    then
    echo "$FILE is a regular file."
    elif [ -d "$FILE" ]
    then
    echo "$FILE is a directory."
    else
    echo "$FILE is something other than a regular file or directory."
    fi

    ls -l $FILE

```

![alt text](image-5.png)


### exit statuses and return codes

- When a command or process finishes running in Linux, it returns an exit status (also called a return code or exit code) to the shell.

    | Exit Code            | Meaning                                                                                   |
    | -------------------- | ----------------------------------------------------------------------------------------- |
    | **0**                |  **Success** – The command executed without errors.                                      |
    | **Non-zero (1–255)** | **Failure** – Something went wrong. The specific number can indicate the type of error. |

  ```bash
     ls /etc
     echo $?
     0

  ```

##### && and ||

- && = AND - command2 runs only if command1 exits with status 0 (success).

    ```bash
    #!/bin/bash
    HOST="google.com"
    ping -c 1 $HOST && echo "$HOST reachable."

  ```
  ![alt text](image-6.png)

- || = OR - Run command2 only if command1 fails

    ```bash
    #!/bin/bash
    HOST="google.com"
    ping -c 1 $HOST || echo "$HOST unreachable."
    ```
  ![alt text](image-7.png)


- `;` - Separating Commands on a Single Line

    ```bash
    echo "Starting cleanup"; rm -f *.tmp; echo "Cleanup finished"
    # all three commands run even if rm -f *.tmp fails.
    ```

    ```bash
    - Write a shell script that accepts a file or directory name as an argument. Have the script report
    if it is a regular file, a directory, or other type of file. If it is a regular file, exit with a 0 exit status.
    If it is a directory, exit with a 1 exit status. If it is some other type of file, exit with a 2 exit status.

        #!/bin/bash

        FILE=$1

        if [ -f "$FILE" ]
        then
        echo "$FILE is a regular file."
        exit 0
        elif [ -d "$FILE" ]
        then
        echo "$FILE is a directory."
        exit 1
        else
        echo "$FILE is something other than a regular file or directory."
        exit 2
        fi
    ```
  ![alt text](image-8.png)


    ```bash
    - Write a script that executes the command "cat /etc/shadow". If the command returns a 0 exit
    status report "Command succeeded" and exit with a 0 exit status. If the command returns a
    non­zero exit status report "Command failed" and exit with a 1 exit status.

    #!/bin/bash
    cat /etc/shadow
    if [ "$?" -eq "0" ]
    then
    echo "Command succeeded"
    exit 0
    else
    echo "Command failed"
    exit 1
    fi
    ```
    ![alt text](image-9.png)

 ### Shell Functions

 - Functions are blocks of code that perform a specific, reusable task.

    ```bash
    function function_name {
        echo "This code is inside the function."
    }

    ```

- Positional Parameters (Arguments)
Functions use the same positional parameters ($1, $2, $@, $#) that were previously discussed for the main script, but they are local to the function itself.

  - $1, $2, etc., refer to the arguments passed to the function, not the arguments passed to the entire script.


    ```bash  
    func () {
        # $1 is the first argument passed to the function
        echo "Hello, $1! Welcome to the script."
    }

   
     func ALl
    ```
    ![alt text](image-10.png)


  #### Variable Scope

    - By default, variables are global
    -  Variables have to be defined before used

    ```bash
    #!/bin/bash
    my_function() {
    GLOBAL_VAR=1
    }
    # GLOBAL_VAR not available yet.
    echo $GLOBAL_VAR
    my_function
    # GLOBAL_VAR is NOW available.
    echo $GLOBAL_VAR

    ```

   ##### Local Variables
    - Can only be accessed within the function.
    - Create using the local keyword.
    - local LOCAL_VAR=1
    - Only functions can have local variables.
    - Best practice to keep variables local in 
    functions


        ```bash
        #!/bin/bash

        my_function() {
            local LOCAL_VAR=1
            echo "LOCAL_VAR can be accessed inside of the function: $LOCAL_VAR"
        }

        my_function

        # LOCAL_VAR is not available outside of the function.
        echo "LOCAL_VAR can NOT be accessed outside of the function: $LOCAL_VAR"

        ```  
   


        ```bash
                - Write a shell script that consists of a function that display the number of files in the present working directory. Name this function "file_count" and call it in your script. If you use a variable in your function, remember to make it a local variable.


        #!/bin/bash

        function file_count() {
        local NUMBER_OF_FILES=$(ls | wc -l)
        echo "$NUMBER_OF_FILES"
        }
        
        file_count
        ``` 
        ![alt text](image-11.png) 


      ```bash
        - Modify the script from the previous exercise. Make the "file_count" function accept a directory as an argument. Next have the function display the name of the directory followed by a colon. Finally, display the number of files to the screen on the next line. Call the function three times.First, on the "/etc" directory, next on the "/var" directory and finally on the "/usr/bin" directory.

        #!/bin/bash

        function file_count() {
        local DIR=$1
        local NUMBER_OF_FILES=$(ls $DIR | wc -l)
        echo "${DIR}:"
        echo "$NUMBER_OF_FILES"
        }

        file_count /etc
        file_count /var
        file_count /usr/bin

      ```  
      ![alt text](image-12.png)


### Wildcards

- Wildcards are great when you want to work 
on a group of files or directories.


    ```bash

    #!/bin/bash

    cd /var/www
    for FILE in *.html
    do
        echo "Copying $FILE"
        cp $FILE /var/
    done
    ```
