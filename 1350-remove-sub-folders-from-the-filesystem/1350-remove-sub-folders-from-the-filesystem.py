class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.is_end = False

    def __init__(self):
        self.root = self.TrieNode()

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        for path in folder:
            folders = path.split('/')
            cur = self.root
            for folder_name in folders:
                if folder_name == "":
                    continue
                if folder_name not in cur.children:
                    cur.children[folder_name] = self.TrieNode()
                cur = cur.children[folder_name]
            cur.is_end = True

        res = []
        for path in folder:
            folders = path.split('/')
            cur = self.root
            is_subfolder = False
            
            for i, folder_name in enumerate(folders):
                if folder_name == "":
                    continue
                next_node = cur.children[folder_name]
                if next_node.is_end and i != len(folders) - 1:
                    is_subfolder = True
                cur = next_node
            
            if not is_subfolder:
                res.append(path)

        return res