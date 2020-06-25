import sys


class SearchTree:
    word_tree = {}

    def __init__(self):
        self.word_tree = {}

    def add_word(self, word):

        last_character = None
        navigator_tree = self.word_tree
        level = 0

        word_index = 0
        char = word[word_index]
        while char in navigator_tree:
            level += 1
            last_character = navigator_tree[char]
            navigator_tree = navigator_tree[char].children
            word_index += 1
            if word_index >= len(word):
                last_character.set_complete(word)
                return True
            char = word[word_index]

        while word_index < len(word):
            char = word[word_index]
            navigator_tree[char] = SearchNode(char, word)
            last_character = navigator_tree[char]
            navigator_tree = navigator_tree[char].children
            word_index += 1
            level += 1

        last_character.set_complete(word)
        return True

    def search(self, phrase):
        results_found = []
        current_search = []
        for character_in_phrase in phrase:
            # search in the main tree for new searches:
            new_search = False
            if character_in_phrase in self.word_tree:
                current_search.insert(0, self.word_tree[character_in_phrase].children)
                new_search = True

            # continue looking for ongoing search
            search_cursor = 0
            for c_search in current_search:
                if c_search is None or new_search:
                    # search was deactivated/died.
                    search_cursor += 1
                    new_search = False
                    continue

                if character_in_phrase in c_search:
                    if c_search[character_in_phrase].complete:
                        results_found.append(c_search[character_in_phrase].word_complete)
                    # go deep and replace it by the children
                    current_search[search_cursor] = c_search[character_in_phrase].children
                else:
                    # character not found, so search died
                    current_search[search_cursor] = None
                search_cursor += 1
        return results_found

    def print_tree(self, target=None, padding=""):
        # TODO: pending
        if target is None:
            cursor = self.word_tree
        else:
            cursor = target

        for key in cursor:
            sys.stdout.write(key)
            self.print_tree(cursor[key].children, padding + "-")
            if len(cursor[key].children) > 1:
                sys.stdout.write(padding)
            else:
                print("")


class SearchNode:
    char = None
    word_result = set()
    # dictionary where key is a char and value is search node.
    children = None
    complete = False
    word_complete = None

    def __init__(self, char_value, for_word):
        self.char = char_value
        # for autocomplete options
        self.word_result.add(for_word)
        self.children = {}
        self.word_result = set()
        self.word_complete = None

    def set_complete(self, word):
        self.word_complete = word
        self.complete = True

    def print(self):
        sys.stdout.write(" - [" + self.char + "]")
        for key in self.children:
            self.children[key].print()

