class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = -1

class FileSystem:

    def __init__(self):
        self.root = TrieNode()
        

    def createPath(self, path: str, value: int) -> bool:
        paths = path.split('/')[1:]
        parent_path = "/" + "/".join(paths[:-1])
        if len(paths) > 1 and self.get(parent_path) == -1:
            return False
        if self.get(path) != -1:
            return False

        curr = self.root
        for p in paths[:-1]:
            curr = curr.children[p]
        
        new_node = TrieNode()
        new_node.value = value
        curr.children[paths[-1]] = new_node
        return True

    def get(self, path: str) -> int:
        if not path or path == "/":
            return -1
        paths = path.split('/')[1:]
        curr = self.root
        for p in paths:
            if p not in curr.children:
                return -1

            curr = curr.children[p]
        
        return curr.value
