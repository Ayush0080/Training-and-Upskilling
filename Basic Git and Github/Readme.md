# Git and Github


## Git
- Git is a distributed version control system (VCS) that allows multiple developers to:
  - Track changes to files over time
  - Create branches for parallel development 
  - Merge updates efficiently
  - Work offline and sync later using repositories
  - It uses snapshots of your code (called commits) and stores them in a local repository.

- Alternative of Git : SVN, Mercurial, Perforce

## GitHub 
 - GitHub is a cloud-based hosting service for Git repositories that provides:

   - Remote repository management
   - Collaboration tools (pull requests, issues, code reviews)
   - CI/CD workflows (GitHub Actions)
   - Access control and version history tracking
   - It integrates directly with Git to sync local changes to a remote repository.

- Alternative of GitHub : GitLab, Bitbucket, AWS CodeCommit, Azure Repos




  ```bash
  git clone <repo-link>  # used to make a copy of a remote repository (like from GitHub, GitLab, or Bitbucket) onto your local computer.

  git remote -v # display the link to the remote repository

  git <command> -h # check parameters
  
  git push

  git fetch

  ```


### commit

- commit : It saves a snapshot of your project’s files at a specific moment in time, along with a message describing what you changed.

   -  every commit has a unique hash key 

  ```bash
   git add . # adds all the file changes to rhe staging area
   git commit -m "commit1" # allows us to create a commit
   git log # gives us an overview of commits
  ```

### Staging

- The staging area (also called the index) is an intermediate space where Git keeps track of which file changes will go into your next commit.
   - Staging in Git means preparing your changes before you officially save them with a commit.

  ```bash
     git add <file-name>  # Stage one specific file (Single file)
     git add . # Stage all changes in current folder (Current directory + subfolders)
     git add -A # Stage all changes (across repo) (Entire repository)
     git status # It shows which files are ready to be committed.(stage or unstage state)
     git reset <file-name> # is used to unstage a file that you previously added with git add.
  ```


  ### Branches
- A branch is basically a pointer (or reference) to a specific commit in your repository’s history.
   - Git’s default branch is usually called main (or master).

   - When you create a new branch, Git creates a new pointer that moves forward independently as you make new commits.

    | Command | Description |
    |----------|--------------|
    | `git branch` | Shows all branches |
    | `git branch <branch-name>` | Creates a new branch |
    | `git checkout <branch-name>` | Switches to another branch |
    | `git switch <branch-name>` | (Modern alternative to checkout) |
    | `git merge <branch-name>` | Merges another branch into the current one |
    | `git branch -d <branch-name>` | Deletes a branch |



  ```bash
   git show <commit-hash> # exactly what changed in that commit.
   git show --name-only <commit-hash> # shows which files were changed in a specific commit — but without showing the actual line-by-line changes.
   git reflog # gives info about all commits on all branches

  ```  

### Push and pull

#### git push

  - Sends your local changes to the remote repository (like GitHub, GitLab, etc.)
    - Transfers commits from your local branch to a remote branch.
    - Updates the remote repo to match your local changes.
 
    ``` bash
     git push origin main # Pushes your local main branch to the remote repository named origin.
    ```

#### git pull
- Brings the latest changes from the remote repository into your local system.
     - It first fetches changes from the remote branch
     - then merges them into your current local branch.    

     ```bash
     git pull origin main # Downloads the latest changes from origin/main and merges them into your local main.
     ```

###  Undo and redo changes  


  #### git revert

  - Used when you want to undo changes but keep your commit history clean.
 
    ```bash
    git revert <commit-hash>

    A -- B -- C  ← current HEAD
              ↑
          (bad commit)
     
     # After git revert C: 
     A -- B -- C -- C'  ← (C' undoes C)      
    ```

 #### git reset

 - Used to move the branch pointer backward in time — it changes where HEAD points.

    ```bash
       git reset --hard <commit-hash>
    ```   

    | Command | Purpose 
    |----------|-----------
    | `git revert` | Undo commit by adding a new commit 
    | `git reset` | Move branch pointer to previous commit 


#### Pull requests and code reviews

 - A Pull Request (PR) is a way to propose changes to a codebase.
It allows developers to notify others that they’ve pushed new commits to a branch and want those changes to be reviewed and merged into another branch


 ##### Example Pull Request (PR) Workflow

- Create a new branch
```bash
git checkout -b feature/login
```

- Make changes and commit
```bash
git add .
git commit -m "Add login feature"
```

- Push the branch

```bash
  git push origin feature/login
```
- Open a Pull Request (PR) on GitHub
   - Compare: feature/login → main
   - Reviewers check your code
   - Once approved, it’s merged


   