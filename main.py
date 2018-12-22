import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from graphviz import Digraph
from tkinter import *
from ua_parser import user_agent_parser
import getopt
import ujson

DATA = "global"

# Dict Constants
country_to_cont = {
    'AF': 'AS',
    'AX': 'EU',
    'AL': 'EU',
    'DZ': 'AF',
    'AS': 'OC',
    'AD': 'EU',
    'AO': 'AF',
    'AI': 'NA',
    'AQ': 'AN',
    'AG': 'NA',
    'AR': 'SA',
    'AM': 'AS',
    'AW': 'NA',
    'AU': 'OC',
    'AT': 'EU',
    'AZ': 'AS',
    'BS': 'NA',
    'BH': 'AS',
    'BD': 'AS',
    'BB': 'NA',
    'BY': 'EU',
    'BE': 'EU',
    'BZ': 'NA',
    'BJ': 'AF',
    'BM': 'NA',
    'BT': 'AS',
    'BO': 'SA',
    'BQ': 'NA',
    'BA': 'EU',
    'BW': 'AF',
    'BV': 'AN',
    'BR': 'SA',
    'IO': 'AS',
    'VG': 'NA',
    'BN': 'AS',
    'BG': 'EU',
    'BF': 'AF',
    'BI': 'AF',
    'KH': 'AS',
    'CM': 'AF',
    'CA': 'NA',
    'CV': 'AF',
    'KY': 'NA',
    'CF': 'AF',
    'TD': 'AF',
    'CL': 'SA',
    'CN': 'AS',
    'CX': 'AS',
    'CC': 'AS',
    'CO': 'SA',
    'KM': 'AF',
    'CD': 'AF',
    'CG': 'AF',
    'CK': 'OC',
    'CR': 'NA',
    'CI': 'AF',
    'HR': 'EU',
    'CU': 'NA',
    'CW': 'NA',
    'CY': 'AS',
    'CZ': 'EU',
    'DK': 'EU',
    'DJ': 'AF',
    'DM': 'NA',
    'DO': 'NA',
    'EC': 'SA',
    'EG': 'AF',
    'SV': 'NA',
    'GQ': 'AF',
    'ER': 'AF',
    'EE': 'EU',
    'ET': 'AF',
    'FO': 'EU',
    'FK': 'SA',
    'FJ': 'OC',
    'FI': 'EU',
    'FR': 'EU',
    'GF': 'SA',
    'PF': 'OC',
    'TF': 'AN',
    'GA': 'AF',
    'GM': 'AF',
    'GE': 'AS',
    'DE': 'EU',
    'GH': 'AF',
    'GI': 'EU',
    'GR': 'EU',
    'GL': 'NA',
    'GD': 'NA',
    'GP': 'NA',
    'GU': 'OC',
    'GT': 'NA',
    'GG': 'EU',
    'GN': 'AF',
    'GW': 'AF',
    'GY': 'SA',
    'HT': 'NA',
    'HM': 'AN',
    'VA': 'EU',
    'HN': 'NA',
    'HK': 'AS',
    'HU': 'EU',
    'IS': 'EU',
    'IN': 'AS',
    'ID': 'AS',
    'IR': 'AS',
    'IQ': 'AS',
    'IE': 'EU',
    'IM': 'EU',
    'IL': 'AS',
    'IT': 'EU',
    'JM': 'NA',
    'JP': 'AS',
    'JE': 'EU',
    'JO': 'AS',
    'KZ': 'AS',
    'KE': 'AF',
    'KI': 'OC',
    'KP': 'AS',
    'KR': 'AS',
    'KW': 'AS',
    'KG': 'AS',
    'LA': 'AS',
    'LV': 'EU',
    'LB': 'AS',
    'LS': 'AF',
    'LR': 'AF',
    'LY': 'AF',
    'LI': 'EU',
    'LT': 'EU',
    'LU': 'EU',
    'MO': 'AS',
    'MK': 'EU',
    'MG': 'AF',
    'MW': 'AF',
    'MY': 'AS',
    'MV': 'AS',
    'ML': 'AF',
    'MT': 'EU',
    'MH': 'OC',
    'MQ': 'NA',
    'MR': 'AF',
    'MU': 'AF',
    'YT': 'AF',
    'MX': 'NA',
    'FM': 'OC',
    'MD': 'EU',
    'MC': 'EU',
    'MN': 'AS',
    'ME': 'EU',
    'MS': 'NA',
    'MA': 'AF',
    'MZ': 'AF',
    'MM': 'AS',
    'NA': 'AF',
    'NR': 'OC',
    'NP': 'AS',
    'NL': 'EU',
    'NC': 'OC',
    'NZ': 'OC',
    'NI': 'NA',
    'NE': 'AF',
    'NG': 'AF',
    'NU': 'OC',
    'NF': 'OC',
    'MP': 'OC',
    'NO': 'EU',
    'OM': 'AS',
    'PK': 'AS',
    'PW': 'OC',
    'PS': 'AS',
    'PA': 'NA',
    'PG': 'OC',
    'PY': 'SA',
    'PE': 'SA',
    'PH': 'AS',
    'PN': 'OC',
    'PL': 'EU',
    'PT': 'EU',
    'PR': 'NA',
    'QA': 'AS',
    'RE': 'AF',
    'RO': 'EU',
    'RU': 'EU',
    'RW': 'AF',
    'BL': 'NA',
    'SH': 'AF',
    'KN': 'NA',
    'LC': 'NA',
    'MF': 'NA',
    'PM': 'NA',
    'VC': 'NA',
    'WS': 'OC',
    'SM': 'EU',
    'ST': 'AF',
    'SA': 'AS',
    'SN': 'AF',
    'RS': 'EU',
    'SC': 'AF',
    'SL': 'AF',
    'SG': 'AS',
    'SX': 'NA',
    'SK': 'EU',
    'SI': 'EU',
    'SB': 'OC',
    'SO': 'AF',
    'ZA': 'AF',
    'GS': 'AN',
    'SS': 'AF',
    'ES': 'EU',
    'LK': 'AS',
    'SD': 'AF',
    'SR': 'SA',
    'SJ': 'EU',
    'SZ': 'AF',
    'SE': 'EU',
    'CH': 'EU',
    'SY': 'AS',
    'TW': 'AS',
    'TJ': 'AS',
    'TZ': 'AF',
    'TH': 'AS',
    'TL': 'AS',
    'TG': 'AF',
    'TK': 'OC',
    'TO': 'OC',
    'TT': 'NA',
    'TN': 'AF',
    'TR': 'AS',
    'TM': 'AS',
    'TC': 'NA',
    'TV': 'OC',
    'UG': 'AF',
    'UA': 'EU',
    'AE': 'AS',
    'GB': 'EU',
    'US': 'NA',
    'UM': 'OC',
    'VI': 'NA',
    'UY': 'SA',
    'UZ': 'AS',
    'UK': 'EU',
    'VU': 'OC',
    'VE': 'SA',
    'VN': 'AS',
    'WF': 'OC',
    'EH': 'AF',
    'YE': 'AS',
    'ZM': 'AF',
    'ZW': 'AF'
}


# generates a histogram of the countries of the viewers of a document
def load_task2a(visit_array):
    # task2a
    letter_counts = Counter(visit_array)
    df = pd.DataFrame.from_dict(letter_counts, orient='index')
    df.plot(kind='bar', title='Document View By Country', legend=False)

    plt.show()


# gets data of the countries of the viewers of a document
def get_task2_data(doc_id):
    visit_record = []

    for record in DATA:
        if record['event_type'] == 'read':
            if record['env_doc_id'] == doc_id:
                visit_record.append(record["visitor_country"])

    return visit_record


# generates a histogram of the continents of the viewers of a document
def load_task2b(cont_count):
    # task2b
    letter_counts2 = Counter(cont_count)
    df = pd.DataFrame.from_dict(letter_counts2, orient='index')
    df.plot(kind='bar', title='Document View By Continent', legend=False)

    plt.show()


# gets data of the the continents of the viewers of a document
def get_task2b_data(doc_id):
    visit_array = get_task2_data(doc_id)
    cont_count = []
    for country in visit_array:
        cont_count.append(country_to_cont[country])
    return cont_count


# generate histogram for all identified browsers frequency
def load_task_3a():
    browser_array = []

    for record in DATA:
        if record['event_type'] == 'read':
            browser_array.append(record["visitor_useragent"])

    letter_counts3 = Counter(browser_array)
    df = pd.DataFrame.from_dict(letter_counts3, orient='index')
    df.plot(kind='bar', title='Browser Frequency', legend=False)

    plt.show()


# generate histogram for main browser frequency
def load_task3b():
    browser_array_split = []

    for record in DATA:
        if (record['event_type'] == 'read'):
            ua_string = record["visitor_useragent"]
            parsed_string = user_agent_parser.Parse(ua_string)
            browser_array_split.append(parsed_string.get('user_agent').get('family'))

    browser_counts = Counter(browser_array_split)
    df = pd.DataFrame.from_dict(browser_counts, orient='index')
    df.plot(kind='bar', title='Browser Frequency Split', legend=False)
    plt.show()


# generates bar graph for the external and internal count
def load_task8(view_source, title_header):
    # task8
    df = pd.DataFrame.from_dict(view_source, orient='index')
    df.plot(kind='bar', title=title_header, legend=False)

    plt.show()


# this returns a dictionary with the count for external and internal for all document views in the file
def get_task8_data_all():
    visit_source = [0, 0]

    for record in DATA:
        if record['event_type'] == 'read':
            if record['visitor_source'] == "internal":
                visit_source[0] = visit_source[0] + 1
            else:
                visit_source[1] = visit_source[1] + 1

    visit_source_dic = {"internal": visit_source[0], "external": visit_source[1]}

    return visit_source_dic


# This returns a dictionary with the count for external and internal document views
def get_task8_data_specific(doc_id):
    visit_source = [0, 0]

    for record in DATA:
        if record['event_type'] == 'read':
            if record['env_doc_id'] == doc_id:
                if record['visitor_source'] == "internal":
                    visit_source[0] = visit_source[0] + 1
                else:
                    visit_source[1] = visit_source[1] + 1

    visit_source_dic = {"internal": visit_source[0], "external": visit_source[1]}

    return visit_source_dic


def get_viewers_of_document(doc_id):
    doc_data = []

    for record in DATA:
        if record['event_type'] == 'read':
            if record['env_doc_id'] == doc_id:
                doc_data.append(record["visitor_uuid"])

    s1 = set([])

    for word in doc_data:
        s1.add(word)

    return s1


def get_read_documents_from_user_id(user_id):
    s2 = set([])

    user_read = []

    for record in DATA:
        if record['event_type'] == 'read':
            if record['visitor_uuid'] == user_id:
                user_read.append(record['env_doc_id'])

    for word in user_read:
        s2.add(word)

    return s2


def sort_like(list_of_documents):
    return Counter(list_of_documents)


# draws the 'also like' graph
def draw_graph(user_id, doc_id, viewers_set, most_common_list, file_type=None):
    if file_type is None or file_type is "":
        file_type = "ps"

    fname = 'alsoLike' + doc_id + ".gv"
    g = Digraph('G', filename=fname, format=file_type)

    # if no user id given then green identification is not required
    if user_id is not None:
        g.node(get_last_4_chars(user_id), style='filled', color='green', shape='square')
        g.node(get_last_4_chars(doc_id), style='filled', color='green')
        g.edge(get_last_4_chars(user_id), get_last_4_chars(doc_id))

    # draw node for each user
    for user in viewers_set:
        g.node(get_last_4_chars(user), shape='square')

    # for each user node, connect an edge to the documents in the top 10 they have read
    for user in viewers_set:

        user_docs = get_read_documents_from_user_id(user)

        for doc in user_docs:
            if doc in most_common_list:
                g.node(get_last_4_chars(doc))
                g.edge(get_last_4_chars(user), get_last_4_chars(doc))

    g.view()


# returns (and draws graph if required) a tuple of the top 10 documents read by other user's of a given document
def also_like(doc_id, func, file_type=None, user_id=None, draw=False):
    viewers_set = get_viewers_of_document(doc_id)

    # Remove provided userID from list so does not recommend from users own history
    if user_id is not None:
        viewers_set.discard(user_id)

    list_of_documents = []

    # for each viewer, get their read documents and add to list
    for user in viewers_set:
        list_of_documents.extend(get_read_documents_from_user_id(user))

    cnt = func(list_of_documents)

    # Uncomment below to print full list of related documents
    # print("full list")
    # print(cnt)

    most_common_list_tuple = cnt.most_common(11)
    # creates list of the most common documents
    most_common_list = [i[0] for i in most_common_list_tuple]

    if draw:
        draw_graph(user_id, doc_id, viewers_set, most_common_list, file_type)

    # removes original document from return list as it seems to only be used in the visualisation from emailed tests
    most_common_list_tuple = [i for i in most_common_list_tuple if i[0] != doc_id]

    print(most_common_list_tuple)
    return most_common_list_tuple


def get_last_4_chars(doc_id):
    return doc_id[-4:]


FILETYPE = "global"


class BuildGUI:

    def __init__(self, master):
        def task2a():
            executeTask("", entry_1.get().strip(), "2a")

        def task2b():
            executeTask("", entry_1.get().strip(), "2b")

        def task3a():
            executeTask("", "", "3a")

        def task3b():
            executeTask("", "", "3b")

        def task4d():
            executeTask(entry_2.get().strip(), entry_1.get().strip(), "4d")

        def task5():
            executeTask(entry_2.get().strip(), entry_1.get().strip(), "5", file_type.get())

        def task8():
            executeTask("", entry_1.get().strip(), "8")

        def confirm_file():
            global DATA
            DATA = [ujson.loads(line) for line in open(entry_3.get().strip())]

        label_1 = Label(master, text="Enter Document ID")
        label_2 = Label(master, text="Enter visitor ID (Optional)")
        label_3 = Label(master, text="Enter File Name")
        entry_1 = Entry(master)
        entry_2 = Entry(master)
        entry_3 = Entry(master)

        button_confirm_file = Button(master, text="Confirm File", command=confirm_file)
        button_task2a = Button(master, text="Task 2a", command=task2a)
        button_task2b = Button(master, text="Task 2b", command=task2b)
        button_task3a = Button(master, text="Task 3a", command=task3a)
        button_task3b = Button(master, text="Task 3b", command=task3b)
        button_task4d = Button(master, text="Task 4d", command=task4d)
        button_task5 = Button(master, text="Task 5", command=task5)
        button_task8 = Button(master, text="Task 8", command=task8)

        file_type = StringVar()
        file_type.set("ps")
        r1 = Radiobutton(master, text="PS File", variable=file_type, value="ps")
        r2 = Radiobutton(master, text="PDF File", variable=file_type, value="pdf")

        # places gui elements on grid
        label_1.grid(row=0, sticky=E)
        label_2.grid(row=1, sticky=E)
        label_3.grid(row=5, sticky=E)
        entry_1.grid(row=0, column=1)
        entry_2.grid(row=1, column=1)
        entry_3.grid(row=5, column=1)
        button_confirm_file.grid(row=6, column=1)
        button_task2a.grid(row=0, column=2)
        button_task2b.grid(row=0, column=3)
        button_task3a.grid(row=1, column=2)
        button_task3b.grid(row=1, column=3)
        button_task4d.grid(row=2, column=2)
        button_task5.grid(row=2, column=3)
        button_task8.grid(row=3, column=2)
        r1.grid(row=1, column=4)
        r2.grid(row=2, column=4)


def executeTask(user, doc, task, file_type2=None):
    """Takes a user uuid, doc uuid and a task and returns the output for the specific task"""
    if task == "2a":
        if doc != "":
            visitArray = get_task2_data(doc)
            return load_task2a(visitArray)
        else:
            print("DOC UUID needs to be specified")
            return "DOC UUID needs to be specified"
    elif task == "2b":
        if doc != "":
            cont_count = get_task2b_data(doc)
            return load_task2b(cont_count)
        else:
            print("DOC UUID needs to be specified")
            return "DOC UUID needs to be specified"
    elif task == "3a":
        return load_task_3a()
    elif task == "3b":
        return load_task3b()
    elif task == "4d":
        if doc != "":
            if (len(user) > 0):
                return also_like(doc, sort_like, user_id=user, file_type=None, draw=False)
            else:
                return also_like(doc, sort_like, draw=False)
        else:
            print("DOC UUID needs to be specified")
            return "DOC UUID needs to be specified"
    elif task == "5":
        if doc != "":
            if len(user) > 0:
                return also_like(doc, sort_like, user_id=user, file_type=file_type2, draw=True)
            else:
                return also_like(doc, sort_like, file_type=file_type2, draw=True)
        else:
            print("DOC UUID needs to be specified")
            return "DOC UUID needs to be specified"
    elif task == "8":
        if doc != "":
            visit_source_dic = get_task8_data_specific(doc)
            load_task8(visit_source_dic, "Visitor Source of Document With UUID Ending In : " + get_last_4_chars(doc))
        else:
            visit_source_dic = get_task8_data_all()
            load_task8(visit_source_dic, "Visitor Source of All Documents")
    else:
        print("NO SUCH TASK")
        return "NO SUCH TASK"


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:d:t:f:")
    except getopt.GetoptError as err:
        print(str(err))
        sys.exit(0)
    user = ""
    doc = ""
    task = ""

    for o, a in opts:
        if o == "-u":
            user = a
        elif o == "-d":
            doc = a
        elif o == "-t":
            task = a
        elif o == "-f":
            DATA = [ujson.loads(line) for line in open(a)]
        else:
            assert False, "unhandled option"
    if (user == "") and (doc == "") and (task == ""):
        root = Tk()
        b = BuildGUI(root)
        root.mainloop()
    else:
        executeTask(user, doc, task)
