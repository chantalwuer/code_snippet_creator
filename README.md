# Code Snippet Creator

## Description

Some code blocks can be reused in various projects and it can increase the efficiency of the workflow to have them saved as snippets for easy access. 
One way of doing that when working in VS Code is using the build-in user snippets. When configured, it is enough to type a pre-defined prefix and a whole code block will be automatically inserted into the code.

To set up the code snippets, however, each code block must be correctly formatted and added to a `.json` file within VS Code. This can get quite tedious, especially with longer code blocks. 

This program does the formatting for you. It takes as input the title, prefix, code and description and returns a fully formatted block that can be added to the `.json` file.

## Getting Started

The program can be run from the CLI. Either by simply executing it with
```zsh
python <file_path>
```

Alternatively, creating an alias in the `.zshrc` file can make access even simpler. 
```zsh
cd ~
code .zshrc
```

Add to the .zshrc file: 
```
alias code-snippet="python <file_path>/snippet_converter.py"
```

Save the file and restart the terminal.

Now, running `code-snippet` in the CLI will be enough to start the program.

## Creating a code snippet

To create a snippet, the program will prompt inputs. 
- **Title:** The title of your code snippet
- **Prefix:** The text you write in VS Code to trigger the code snippet 
- **Code Block:** Your code block
- **Description:** A description of what the snippet does

The output will then look like this: 

<img width="792" alt="image" src="https://user-images.githubusercontent.com/112972472/218088455-57dbba8d-995c-4f3f-a5f5-def1d21cc1dd.png">


## Adding snippets to VS Code

To add the formatted snippet to VS Code, open `Code/Preferences/Configure User Snippets` and pick a programming language. A `.json` file will open and the formatted snippet can be pasted into the file, following the example given in the file. 

