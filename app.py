import streamlit as st
import numpy as np
import pandas as pd

'''
Convert any code into snippet format
'''

## * Input tasks
st.markdown("""
    ### 📋 Enter your code
    """)

list_with_weights_percent = {}

with st.form(key='submit_tasks'):
    block = st.text_input('Enter your code block with each line ended by a ;',
                              '')
    st.form_submit_button('Submit')


def snippet_transformer(block):
    lines = block.split(';')
    results = []
    # lines = [x.strip() for x in block.split(';')]
    for line in lines:
        if line.startswith(' '):
            spaces = ' ' * 4
            # results.append(f'"{spaces}{line}",')
            results.append((' ' * 4) + line)

        else:
            results.append(f'"{line}",')

    return results

results = snippet_transformer(block)

st.write(results)
for line in results:
    st.write(line)

st.write(snippet_transformer(block))


# ## * Assign weights in percent
# st.markdown("""
#     ### ⚖️ Assign importance of tasks
#     """)

# for task in todolist:
#     if sum(list_with_weights_percent.values()) < 100:
#         list_with_weights_percent[task] = st.slider(f'How important is {task} today?',
#                                             0, 100 - sum(list_with_weights_percent.values(), 0))
#     else:
#         list_with_weights_percent[task] = 0
#         "You have reached the maximum weight of 20. The remaining tasks will be assigned a weight of 0."


# ## * Pick a task percent
# st.markdown("""
#     ### 🎲 Choose how to pick your task
#     """)

# st.write("How to you want to pick your task?")

# if st.checkbox('Roll my own die'):

#     die_numbers = st.radio('How many sides does your die have?', (6, 10, 20))


#     if st.button('Submit'):
#         numbers_dice = np.arange(1, die_numbers + 1)
#         tasks_weights_percent = []
#         for key, value in list_with_weights_percent.items():
#             tasks_weights_percent += [key] * math.ceil((value / 100) * die_numbers)

#         if len(tasks_weights_percent) > die_numbers:
#             tasks_weights_percent = tasks_weights_percent[:die_numbers]

#         weighted_tasks = pd.DataFrame(numbers_dice, columns=["Number"])
#         weighted_tasks['Task'] = tasks_weights_percent
#         hidden_index_df = weighted_tasks.assign(hack='').set_index('hack')

#         with st.spinner('Wait for it...'):
#             time.sleep(1)
#         st.success('Done!')
#         hidden_index_df

# if st.checkbox('Roll the die for me'):
#     with st.spinner('Rolling the die...'):
#         time.sleep(1)

#         twenty_numbers = np.arange(1,101)
#         tasks_weights_percent = []
#         for key, value in list_with_weights_percent.items():
#             tasks_weights_percent += [key] * value
#     todo = np.random.choice(tasks_weights_percent)
#     st.success(f'Your task is: {todo} 🎉')
