graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

torre_hanoi = {
    '0': ['1', '15'],
    '1': ['2'],
    '2': ['3', '17'],
    '3': ['4'],
    '4': ['5', '20'],
    '5': ['6'],
    '6': ['7', '8'],
    '7': ['8'],
    '8': ['9'],
    '9': ['10'],
    '10': ['11'],
    '11': ['12'],
    '12': ['13'],
    '13': ['14'],
    '14': [],
    '15': ['16'],
    '16': ['18', '19'],
    '17': [],
    '18': [],
    '19': ['22'],
    '20': ['24'],
    '21': ['25'],
    '22': ['21', '23'],
    '23': ['26'],
    '24': ['9', '10'],
    '25': ['11', '12'],
    '26': ['13', '14']
}

torre_hanoi_prof = {
    '0': ['1', '19'],
    '1': ['2'],
    '2': ['3'],
    '3': ['4'],
    '4': ['5'],
    '5': ['6'],
    '6': ['7'],
    '7': ['8'],
    '8': ['9'],
    '9': ['10'],
    '10': ['11'],
    '11': ['12'],
    '12': ['13'],
    '13': ['14'],
    '14': ['15'],
    '15': ['16'],
    '16': ['17'],
    '17': ['18'],
    '18': [],
    '19': ['20'],
    '20': ['21'],
    '21': ['22'],
    '22': ['23'],
    '23': ['24'],
    '24': ['25'],
    '25': ['26'],
    '26': ['18']
}

ilustracao1 = {
    'A': ['B', 'C', 'D', 'E'],
    'B': ['F', 'G'],
    'C': ['H'],
    'D': ['H', 'I'],
    'E': ['J'],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

ilustracao2 = {
    'A': ['B', 'S'],
    'B': ['C', 'G', 'H'],
    'C': ['D', 'F'],
    'D': ['E'],
    'E': [],
    'F': ['E'],
    'G': ['E'],
    'H': ['F'],
    'I': ['J'],
    'J': ['K', 'L'],
    'K': [],
    'L': [],
    'M': ['N', 'O'],
    'N': ['L'],
    'O': ['L', 'P'],
    'P': [],
    'Q': [],
    'R': ['Q'],
    'S': ['I', 'M', 'R']
}

ucs_arvore = {'A': {'filhos': ['B', 'C', 'D', 'E'], 'custos': {'B': 4, 'C': 3, 'D': 2, 'E': 10}},
              'B': {'filhos': ['F', 'G'], 'custos': {'A': 4, 'F': 5, 'G': 7}},
              'C': {'filhos': ['H'], 'custos': {'A': 3, 'H': 10}},
              'D': {'filhos': ['H', 'I'], 'custos': {'A': 2, 'H': 12, 'I': 8}},
              'E': {'filhos': ['J'], 'custos': {'A': 7, 'J': 10}},
              'F': {'filhos': [], 'custos': {'B': 5}},
              'G': {'filhos': [], 'custos': {'B': 7}},
              'H': {'filhos': [], 'custos': {'C': 10, 'D': 12}},
              'I': {'filhos': [], 'custos': {'D': 8}},
              'J': {'filhos': [], 'custos': {'E': 10}}
              }

ilustracao_a = {'A': {'h': 50, 'filhos': ['B', 'C', 'D', 'E'], 'custos': {'B': 4, 'C': 3, 'D': 2, 'E': 10}},
                'B': {'h': 9, 'filhos': ['F', 'G'], 'custos': {'A': 4, 'F': 5, 'G': 7}},
                'C': {'h': 4, 'filhos': ['H'], 'custos': {'A': 3, 'H': 10}},
                'D': {'h': 7, 'filhos': ['H', 'I'], 'custos': {'A': 2, 'H': 12, 'I': 8}},
                'E': {'h': 11, 'filhos': ['J'], 'custos': {'A': 7, 'J': 10}},
                'F': {'h': 7, 'filhos': [], 'custos': {'B': 5}},
                'G': {'h': 3, 'filhos': [], 'custos': {'B': 7}},
                'H': {'h': 0, 'filhos': [], 'custos': {'C': 10, 'D': 12}},
                'I': {'h': 13, 'filhos': [], 'custos': {'D': 8}},
                'J': {'h': 15, 'filhos': [], 'custos': {'E': 10}}
                }

ilustracao_b = {'A': {'h': 110,
                      'filhos': ['B', 'C'],
                      'custos': {'B': 21, 'C': 19}},
                'B': {'h': 99,
                      'filhos': ['D', 'E', 'F'],
                      'custos': {'A': 21, 'D': 11, 'E': 8, 'F': 10}},
                'C': {'h': 97,
                      'filhos': ['G', 'H', 'I'],
                      'custos': {'A': 19, 'G': 17, 'H': 10, 'I': 13}},
                'D': {'h': 11,
                      'filhos': ['J', 'KA'],
                      'custos': {'B': 11, 'J': 7, 'KA': 9}},
                'E': {'h': 12,
                      'filhos': ['L'],
                      'custos': {'B': 8, 'L': 8}},
                'F': {'h': 13,
                      'filhos': ['KB'],
                      'custos': {'B': 10, 'KB': 7}},
                'G': {'h': 9,
                      'filhos': ['M'],
                      'custos': {'C': 17, 'M': 6}},
                'H': {'h': 16,
                      'filhos': ['N', 'O'],
                      'custos': {'C': 10, 'N': 5, 'O': 5}},
                'I': {'h': 15,
                      'filhos': ['P'],
                      'custos': {'C': 13, 'P': 7}},
                'J': {'h': 4,
                      'filhos': ['L'],
                      'custos': {'D': 7, 'L': 7}},
                'KA': {'h': 7,
                       'filhos': ['L'],
                       'custos': {'D': 9, 'L': 4}},
                'KB': {'h': 7,
                       'filhos': ['L'],
                       'custos': {'F': 7, 'L': 3}},
                'L': {'h': 0,
                      'filhos': [],
                      'custos': {'J': 7, 'KA': 4, 'E': 8, 'KB': 3}},
                'M': {'h': 18,
                      'filhos': ['Q', 'R'],
                      'custos': {'G': 6, 'Q': 9, 'R': 2}},
                'N': {'h': 21,
                      'filhos': ['R'],
                      'custos': {'H': 5, 'R': 2}},
                'O': {'h': 27,
                      'filhos': ['R', 'S'],
                      'custos': {'H': 5, 'R': 3, 'S': 4}},
                'P': {'h': 37,
                      'filhos': [],
                      'custos': {'I': 7}},
                'Q': {'h': 23,
                      'filhos': [],
                      'custos': {'M': 9}},
                'R': {'h': 33,
                      'filhos': [],
                      'custos': {'M': 2, 'N': 2, 'O': 3}},
                'S': {'h': 35,
                      'filhos': [],
                      'custos': {'O': 4}}
                }
