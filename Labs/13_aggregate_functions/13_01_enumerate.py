'''
Demonstrate the use of the .enumerate() function.
'''
m_names = ['Mason', 'Mia', 'Mila', 'Michael', 'Madison', 'Matthew', 'Mateo', 'Muhammad', 'Maya']

for i,y in enumerate(m_names):
    print(f'{i} - {y}')

m_dict = dict(enumerate(m_names))
print(m_dict)