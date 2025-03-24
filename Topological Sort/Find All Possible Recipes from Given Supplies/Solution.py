"""
Link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
Time Complexity: O((Supplies + Recipes) + Ingred)
Space Complexity: O(V + E)
"""
from typing import List
from collections import defaultdict, deque


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(set)
        indegrees = defaultdict(int)
        targets = set(recipes)

        for index, recipe in enumerate(recipes):
            for ingredient in ingredients[index]:
                graph[ingredient].add(recipe)
                indegrees[recipe] += 1

        # set to list for better iterations
        for key in graph.keys():
            graph[key] = list(graph[key])

        answer = []
        dq = deque()

        # supplies
        for item in supplies:
            dq.append(item)

        # topological sort
        while dq:
            ingred = dq.popleft()
            if ingred in targets:
                answer.append(ingred)

            for target in graph[ingred]:
                indegrees[target] -= 1

                if indegrees[target] == 0:
                    dq.append(target)

        return answer
