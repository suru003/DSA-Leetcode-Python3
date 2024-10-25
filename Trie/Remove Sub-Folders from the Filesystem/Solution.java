class TrieNode {
    String val;
    boolean isEnd;
    Map<String, TrieNode> children;

    TrieNode(String val) {
        this.val = val;
        this.isEnd = false;
        this.children = new HashMap<>();
    }
}

class Trie {
    TrieNode root;

    Trie() {
        this.root = new TrieNode("/");
    }

    void addFolder(String path) {
        String[] folders = path.split("/");
        TrieNode ptr = root;

        for (String folder : folders) {
            if (!ptr.children.containsKey(folder)) {
                ptr.children.put(folder, new TrieNode(folder));
            }
            ptr = ptr.children.get(folder);
        }
        ptr.isEnd = true;
    }

    List<String> getParentPaths() {
        List<String> paths = new ArrayList<>();

        dfs(root, new ArrayList<>(), paths);
        return paths;
    }

    private void dfs(TrieNode node, List<String> folders, List<String> paths) {
        if (node.isEnd) {
            paths.add(String.join("/", folders));
            return; // Stop traversing if this is a parent folder
        }

        for (String childFolder : node.children.keySet()) {
            folders.add(childFolder);
            dfs(node.children.get(childFolder), folders, paths);
            folders.remove(folders.size() - 1);
        }
    }
}

class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Trie trie = new Trie();

        for (String path : folder) {
            trie.addFolder(path);
        }

        return trie.getParentPaths();
    }
}
