

def get_inputs():
    '''
    This method gets and returns the user's input for title, prefix,
    body and description.
    '''

    title = input('What is the title of your snippet?\n')
    prefix = input('What is the prefix of the snippet?\n')
    # body = input('Please enter your code divided by ; after each line: ')

    print("Enter/Paste your code block. Ctrl-D or Ctrl-Z (Win) to save it.\n")
    body = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        body.append(line)
    description = input('\nDescribe your code snippet:\n')

    return title, prefix, body, description

def snippet_transformer(body):
    # lines = body.split('# ')[1:]
    results = []

    for line in body:
        # line.strip('#')
        leading_space = len(line) - len(line.lstrip())
        space = leading_space * ' '
        results.append(f'"{space}{line.strip()}",')

    return results

def print_snippet(title, prefix, body, description):
    results = snippet_transformer(body)

    print('\nDone. ✅')
    print('\nCopy and paste this into your snippet .json file: \n')
    print('⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️\n')
    print(f'"{title}": {{')
    print(f'  "prefix": "{prefix}",')
    print(f'  "body": [')
    for line in results:
        print(f'    {line}')

    print(f'  ],')
    print(f'  "description": "{description}"')
    print(f'}}')

    print('\n⬆️ ⬆️ ⬆️ ⬆️ ⬆️ ⬆️ ⬆️ ⬆️ ⬆️ ⬆️ ')
    return ""


if __name__ == '__main__':
    # print(main())
    print(print_snippet(*get_inputs()))
