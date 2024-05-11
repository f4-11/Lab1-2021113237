import string


class graph:
    def __init__(self, file_path):
        text = self.__read_file(file_path)
        self.__nodes = []
        self.__edges = {}
        self.__weights = {}
        self.__create_graph(text)
        # print(self.__nodes)
        # print(self.__edges)
        # print(self.__weights)

    def get_nodes(self):
        return self.__nodes.copy()

    def get_edges(self):
        return self.__edges.copy()

    def get_weights(self):
        return self.__weights.copy()

    def draw_graph(self):
        G = nx.DiGraph()
        G.add_nodes_from(dict_1)
        for i in range(len_dic):
            for j in range(len_dic):
                if matix[i][j] > 0:
                    G.add_edge(dict_2[i], dict_2[j], weight=matix[i][j])

        # 绘制图形
        pos = nx.spring_layout(G)  # 图形布局
        pos = nx.kamada_kawai_layout(G)
        nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', edge_color='gray')

    def __read_file(self, file_path):
        res_list = []
        with open("test.txt", "r") as f:  # 打开文件
            data = f.read()
            for i in data:
                if i in [' ', '\r', '\n'] or i in string.punctuation:
                    res_list.append(' ')
                elif i.isalpha():
                    res_list.append(i)
        return ''.join(res_list)

    def __create_graph(self, text):
        words = text.split()
        # print(words)
        for i in range(len(words) - 1):
            self.__add_edge(words[i], words[i + 1])

    def __add_edge(self, word_from, word_to):
        if word_from not in self.__nodes:
            self.__nodes.append(word_from)
            self.__edges[word_from] = []
        if word_to not in self.__nodes:
            self.__nodes.append(word_to)
            self.__edges[word_to] = []
        if word_to not in self.__edges[word_from]:
            self.__edges[word_from].append(word_to)
            self.__weights[(word_from, word_to)] = 1
        else:
            self.__weights[(word_from, word_to)] += 1