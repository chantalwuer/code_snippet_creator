

def get_inputs():
    title = input('What is the title of your snippet? ')
    prefix = input('What is the prefix of the snippet? ')
    # body = input('Please enter your code divided by ; after each line: ')

    print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
    body = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        body.append(line)
    description = input('Describe your code snippet: ')

    breakpoint()
    return title, prefix, body, description

def snippet_transformer(block):
    lines = block.split('# ')[1:]
    results = []

    for line in lines:
        leading_space = len(line) - len(line.lstrip())
        space = leading_space * ' '
        results.append(f'"{space}{line.strip()}",')

    return results

def print_snippet(title, prefix, body, description):
    results = snippet_transformer(body)

    print(f'"{title}": {{')
    print(f'  "prefix": "{prefix}",')
    print(f'  "body": [')
    for line in results:
        print(f'    {line}')

    print(f'  ],')
    print(f'  "description": "{description}"')
    print(f'}}')

    return ""


if __name__ == '__main__':
    # print(main())
    print(print_snippet(*get_inputs()))
