"""Exemplo básico de objetos serealizados em disco."""
import pickle

# Pickle no arquivo
with open('pickle.pkl', 'wb') as w_file:
    pickle.dump(list('Python'), w_file)

# Unpickle
with open('pickle.pkl', 'rb') as r_file:
    obj_a = pickle.load(r_file)
    print(obj_a)
