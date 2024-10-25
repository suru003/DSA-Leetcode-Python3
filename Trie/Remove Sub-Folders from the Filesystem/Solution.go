package main

import (
	"fmt"
	"strings"
)

type TrieNode struct {
	val      string
	isEnd    bool
	children map[string]*TrieNode
}

func NewTrieNode(val string) *TrieNode {
	return &TrieNode{
		val:      val,
		isEnd:    false,
		children: make(map[string]*TrieNode),
	}
}

type Trie struct {
	root *TrieNode
}

func NewTrie() *Trie {
	return &Trie{
		root: NewTrieNode("/"),
	}
}

func (t *Trie) AddFolder(path string) {
	folders := strings.Split(path, "/")
	ptr := t.root

	for _, folder := range folders {
		if folder == "" {
			continue // Skip empty strings due to split on "/"
		}
		if _, exists := ptr.children[folder]; !exists {
			ptr.children[folder] = NewTrieNode(folder)
		}
		ptr = ptr.children[folder]
	}
	ptr.isEnd = true
}

func (t *Trie) GetParentPaths() []string {
	var paths []string

	var dfs func(*TrieNode, []string)
	dfs = func(ptr *TrieNode, folders []string) {
		if ptr.isEnd {
			paths = append(paths, "/"+strings.Join(folders, "/"))
			return
		}

		for childFolder, childNode := range ptr.children {
			folders = append(folders, childFolder)
			dfs(childNode, folders)
			folders = folders[:len(folders)-1]
		}
	}

	dfs(t.root, []string{})
	return paths
}

func removeSubfolders(folder []string) []string {
	trie := NewTrie()

	for _, path := range folder {
		trie.AddFolder(path)
	}

	return trie.GetParentPaths()
}
