class TrieNode
    attr_accessor :fullword, :children

    def initialize
        @fullword = false
        @children = {}
    end
end

class Trie
    def initialize
        @root = TrieNode.new
    end

    def insert(word)
        node = @root
        word.each_char { |char| node = (node.children[char] ||= TrieNode.new) }
        node.fullword = true; nil
    end

    def search(word)
        _search_(@root, word.chars, 0)
    end

    private def _search_(node, chars, idx)
        chars[idx..-1].each do |char|
            if char == '.'
                node.children.values.each do |cnode|
                    return true if _search_(cnode, chars, idx + 1)
                end
                return false
            end

            return false unless node.children.key?(char)
            node = node.children[char]
            idx += 1
        end
        return node.fullword
    end
end

class WordDictionary
    def initialize
        @tree = Trie.new
    end

    # @param {String} word
    # @return {Void}
    # Adds a word into the data structure.
    def add_word(word)
        @tree.insert(word)
    end

    # @param {String} word
    # @return {Boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(word)
        @tree.search(word)
    end
end

class TrieNode
    attr_accessor :value, :is_end, :nexts

    def initialize(value, is_end=false)
      @value, @is_end = value, is_end
      self.nexts = {}
    end
end

class WordDictionary
    attr_accessor :texts

    def initialize()
        self.texts = {}
    end

    def add_word(text)
        if self.texts[text.length]
            self.texts[text.length].push(text)
        else
            self.texts[text.length] = [text]
        end
    end

    def search(text)
        if self.texts[text.length]
            regexp = Regexp.new(text)
            self.texts[text.length].each do |value|
                return true if value.match(regexp)
            end
        end
        false
    end
end