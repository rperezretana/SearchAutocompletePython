from SeearchTree import SearchTree


class TestCommonHelpers:

    def test_string_insert_1(self):
        content = SearchTree()
        assert content.add_word("facebook")
        assert content.add_word("facetime")
        assert content.add_word("facepalm")
        assert content.add_word("google")
        assert content.add_word("777")
        assert "f" in content.word_tree
        assert "g" in content.word_tree
        assert "k" not in content.word_tree
        assert "a" in content.word_tree["f"].children
        assert "g" not in content.word_tree["f"].children
        assert "7" not in content.word_tree["f"].children
        assert "7" in content.word_tree["7"].children["7"].children

    def test_string_insert_2(self):
        content = SearchTree()
        assert content.add_word("facebook")
        assert content.add_word("facetime")
        assert content.add_word("msft")
        assert 'f' in content.word_tree
        assert 'm' in content.word_tree
        assert 'z' not in content.word_tree

    def test_string_search(self):
        content3 = SearchTree()
        content3.add_word("facebook")
        content3.add_word("facetime")
        content3.add_word("fun")
        content3.add_word("front")
        content3.add_word("fanta")
        content3.add_word("google")
        content3.add_word("googl")
        content3.add_word("macros")
        content3.add_word("mass")
        content3.add_word("goog")
        content3.add_word("microsoft")
        content3.print_tree()
        assert content3.search("Long useless text then facebook appears also googles")[0] == "facebook"
        assert content3.search("Long useless text then facebook appears also googles")[1] == "goog"
        assert content3.search("Long useless text then facebook appears also googles")[2] == "googl"
        assert content3.search("Long useless text then facebook appears also googles")[3] == "google"
        assert content3.search("amicrosofter")[0] == "microsoft"
        assert content3.search("goog")[0] == "goog"
        assert len(content3.search("amicrosoter")) == 0, "should have no results"

    def test_autocomplete_mode(self):
        pass
