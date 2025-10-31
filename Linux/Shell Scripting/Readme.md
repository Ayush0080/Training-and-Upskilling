- variables

``` bash
   VARIABLE_NAME="value"  # by convention variables are uppercase
```


- shell script variable uasge

``` bash
    #! /bin/bash
    MY_SHELL="bash"
    echo "i lik the ${MY_SHELL} shell."
```

- Assign command output to a variable

``` bash
    #! /bin/bash
    MY_SHELL=$(hostname)
    echo "i lik the ${MY_SHELL} shell."
```

- Arithmetic operators 

    - arg1 -eq arg2 = equal
    - arg1 -ne arg2 = not equal
    - arg1 -lt arg2 = less than
    - arg1 -le arg2 = less than or equal to
    - arg1 -gt arg2 = greater than
    - arg1 -ge arg2 = greater than or equal to


- if statement
  ``` bash
    if [condtion-is-true]
    then
       command 1
       command 2
       command 3
       command n
    fi
  ```


- if/else
 
  ```bash
   #!/bin/bash
    NUMBER=15

    if [ $NUMBER -gt 10 ]; then
        echo "The number $NUMBER is greater than 10."
    else
        echo "The number $NUMBER is NOT greater than 10."
    fi

  ```

- if/elif/else

    ```bash
      #!/bin/bash

    FILE_PATH="/etc/passwd" 

    if [ -f "$FILE_PATH" ]; then
        echo "$FILE_PATH is a regular file."
    elif [ -d "$FILE_PATH" ]; then
        echo "$FILE_PATH is a directory."
    else
        echo "$FILE_PATH is neither a file nor a directory."
    fi
    
    ```


 - for loop

    ```bash
        #!/bin/bash

        echo "--- Example 1: Looping through fruits ---"

        for FRUIT in apple banana cherry orange; do
            echo "I like to eat a $FRUIT."
        done

        echo "Loop complete."
    ```   




